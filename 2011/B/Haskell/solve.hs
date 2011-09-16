-- -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
--
-- File Name : solve.hs
--
-- Purpose :
--
-- Creation Date : 06-09-2011
--
-- Last Modified : Thu 15 Sep 2011 07:18:32 PM EEST
--
-- Created By : Greg Liras <gregliras@gmail.com>
--
--_._._._._._._._._._._._._._._._._._._._._.


import List
import Data.Set
 
import Data.List (intercalate)




  





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


instance Show MyData where
  show (Words strings integer) = show strings ++ " , " ++ show integer

data MyData = Words [String] Int


buildDataList ::[[String]]->[MyData]
buildDataList [] = []
buildDataList (wordList:rList) = Words wordList 0 : buildDataList rList
  
    
filterByLength x ls = List.filter (\n -> length n == x) ls

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



findMaxWordFast dictionary lettersList = 
  let
    groupedByLength = groupByLength dictionary
  in
    let
      allAnswers = List.map (filterByFirstOccurance dictionary) (findEveryThing [(countSteps (buildDataList groupedByLength) x)  | x <- lettersList])
    in
      allAnswers --[filterByFirstOccurance x dictionary | x <- allAnswers]



findEveryThing :: [[MyData]]-> [[String]]
findEveryThing myDataLists =
  List.map (\x -> let max = getMaxCounter x 0 in filterByMaxCounter x max []) myDataLists


filterByMaxCounter :: [MyData] -> Int -> [[String]] -> [String]
filterByMaxCounter [] _ acc = concat acc
filterByMaxCounter ((Words string counter):rlist) max acc = 
  if (counter == max)
    then filterByMaxCounter rlist max (string:acc)
    else filterByMaxCounter rlist max acc

getMaxCounter [] max = max
getMaxCounter ((Words _ counter):rlist) max =
  if (max < counter) 
    then getMaxCounter rlist counter
    else getMaxCounter rlist max



countSteps ::[MyData]->String->[MyData]
countSteps wordListList [] = wordListList
countSteps wordListList (letter:s) = 
  let
    nextWordListList = concat [groupByElemIndices letter wordlist | wordlist <- wordListList]
  in
    countSteps nextWordListList s

        
getWordListsFromTuples tupleWordList = 
  let
    (a,b) = unzip tupleWordList
  in
    a
  

getElemIndicesForAllWords wordList letter= 
  [(x,y) | x <- wordList,let y = elemIndices letter x]




groupByElemIndices :: Char->MyData->[MyData]
groupByElemIndices letter (Words wordList counter) = 
  let
    toupleWordList = getElemIndicesForAllWords wordList letter
  in
    buildNextList (groupByElemIndicesH toupleWordList []) counter





buildNextList :: [[(String,[Int])]]->Int->[MyData]
buildNextList toupleWordLists prevCounter =
  let
    wordListsWithNoLetter = List.map getWordListsFromTuples (List.filter (any (\(x,y) -> y == [] )) toupleWordLists)
    wordListsWithLetter = List.map getWordListsFromTuples (List.filter (any (\(x,y) -> y /= [] ) ) toupleWordLists)
    wasIn = not (List.null wordListsWithLetter)
  in
    if wasIn
    then 
      let 
        nextDataWithout = [Words x (prevCounter+1) | x <- wordListsWithNoLetter]
        nextDataWith = [Words x prevCounter | x <- wordListsWithLetter]
      in
        nextDataWith++nextDataWithout
    else
      [Words x prevCounter | x <- wordListsWithNoLetter]


groupByElemIndicesH ::[(String,[Int])]->[[(String,[Int])]]->[[(String,[Int])]]
groupByElemIndicesH [] acc = acc
groupByElemIndicesH ((a,b):leWordList) acc = 
  let
    first = List.filter (\(x,y) -> y==b) leWordList
    rest = List.filter (\(x,y) -> y/=b) leWordList
  in
    groupByElemIndicesH rest (((a,b):first):acc)




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
