-- -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
--
-- File Name : solve.hs
--
-- Purpose :
--
-- Creation Date : 06-09-2011
--
-- Last Modified : Thu 15 Sep 2011 04:23:07 AM EEST
--
-- Created By : Greg Liras <gregliras@gmail.com>
--
--_._._._._._._._._._._._._._._._._._._._._.


import List
import Data.Set
 
import Data.List (intercalate)

data MyData = Words [String] Int



buildDataList ::[[String]]->[MyData]
buildDataList (wordList:rList) = Words wordList 0 : buildDataList rList
  





rInt x = read x :: Integer


getNM :: IO [Integer]
getNM =
  do
    inp <- getLine
    return (List.map rInt (Main.split inp ' '))
getLines   :: Integer->Integer ->[String]-> IO [String]
getLines n maX acc
  | n <= maX =
    do
      inp <- getLine
      getLines (n+1) maX (inp:acc)
  | otherwise = return (reverse acc)




    
filterByLength x ls = List.filter (\n -> length n == x) ls

filterByNotElem :: Char->[String]->[String]
filterByNotElem letter wordlist = List.filter (\x -> notElem letter x) wordlist

filterByElemIndices ::String->[String]->Char->[String]
filterByElemIndices word wordlist letter = 
  let
    indices = elemIndices letter word
  in
    List.filter (\x -> (elemIndices letter x) == indices) wordlist

filterByFirstOccurance :: [String]->[String]->String
filterByFirstOccurance (dict:ionary) answers =
  if elem dict answers
  then dict
  else filterByFirstOccurance ionary answers

filterByMaxInt answers =
  let
    (sstr,iint) = unzip answers
  in
    let
      (answer,_) = unzip (List.filter (\(x,y) -> y==(maximum iint)) answers)
    in
      answer

getLengthSists x ls = getLengthSistsH x ls []

getLengthSistsH [] _ acc = reverse acc
getLengthSistsH (x:xs) ls acc = getLengthSistsH xs ls ((filterByLength x ls):acc)

lengthSet :: [[a]]-> [Int]
lengthSet ls = toList (fromList (List.map length ls))

split :: String -> Char -> [String]
split [] delim = [""]
split (c:cs) delim
   | c == delim = "" : rest
   | otherwise = (c : head rest) : tail rest
         where
                rest = Main.split cs delim


groupByLength ls = 
  let
    lengthS = lengthSet ls
  in
    getLengthSists lengthS ls


findWordListSteps :: [String]->String->[(String,Int)]
findWordListSteps wordlist letters = [findSteps x wordlist 0 letters | x <- wordlist]

isInWordList letter wordlist = any (elem letter) wordlist

findSteps :: String->[String]->Int->String->(String,Int)
findSteps word _       counter [] = (word,counter)
findSteps word wordlist counter (letter:restLetters)
--  let
--    lettersSet = buildLetterSet wordlist
--  in
  | isInWordList letter wordlist =
      if elem letter word
      then
        let
          newWordList = filterByElemIndices word wordlist letter
        in
          findSteps word newWordList counter restLetters
      else 
        let
          newWordList = filterByNotElem letter wordlist
        in
          findSteps word newWordList (counter+1) restLetters
  | otherwise =  findSteps word wordlist counter restLetters


findMaxWordFast dictionary lettersList = 
  let
    groupedByLength = groupByLength dictionary
  in
    let
      allAnswers = [filterByFirstOccurance dictionary (countSteps groupedByLength x)  | x <- lettersList]
    in
      allAnswers --[filterByFirstOccurance x dictionary | x <- allAnswers]



countSteps ::[[String]]->String->[String]
countSteps wordListList [] = concat wordListList
countSteps wordListList (letter:s) = 
  let
    nextWordListList = List.filter (\x -> x/=[]) [filterByNotElem letter x | x <- wordListList]
  in
    if nextWordListList == []
      then countSteps wordListList s
      else
      let
        cleanNextWordListList = removeFound nextWordListList
      in
        if cleanNextWordListList == []
        then concat nextWordListList 
        else countSteps cleanNextWordListList s

        
getWordListsFromTuples tupleWordList = 
  let
    (a,b) = unzip tupleWordList
  in
    a
  

getElemIndicesForAllWords wordList letter= 
  [(x,y) | x <- wordList,let y = elemIndices letter x]

  
groupByElemIndices :: Char->[String]->[[String]]
groupByElemIndices letter wordList = 
  let
    toupleWordList = getElemIndicesForAllWords wordList letter
  in
    groupByElemIndicesH toupleWordList []

groupByElemIndicesH ::[(String,[Int])]->[[(String,[Int])]]->[[String]]
groupByElemIndicesH [] acc = List.map getWordListsFromTuples acc
groupByElemIndicesH ((a,b):leWordList) acc = 
  let
    first = List.filter (\(x,y) -> y==b) leWordList
    rest = List.filter (\(x,y) -> y/=b) leWordList
  in
    groupByElemIndicesH rest (((a,b):first):acc)

removeFound ls = List.filter (\x -> length x > 1) ls

--Finds Word

findMaxWord :: [[String]]->String->[(String,Int)]
findMaxWord dictionary letters = concat [findWordListSteps x letters | x <- dictionary]

findAllWords :: [String]->String->String
findAllWords dictionary sequence = 
  let
    wordlists = groupByLength dictionary
  in
    filterByFirstOccurance dictionary (filterByMaxInt (findMaxWord wordlists sequence))




getAll x cases
  | x<= cases =
    do
      nm <- getNM
      dictionary <- getLines 1 (head(nm)) []
      sequences <- getLines 1 (head(tail(nm))) []
      putStrLn ("Case #"++(show x)++": "++(intercalate " "(findMaxWordFast dictionary sequences)))
      getAll (x+1) cases
  | otherwise = return ()
                    
main = 
  do
    cases <- readLn
    --putStrLn (show cases)
    getAll 1 cases
