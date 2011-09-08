-- -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
--
-- File Name : solve.hs
--
-- Purpose :
--
-- Creation Date : 06-09-2011
--
-- Last Modified : Thu 08 Sep 2011 06:45:55 PM EEST
--
-- Created By : Greg Liras <gregliras@gmail.com>
--
--_._._._._._._._._._._._._._._._._._._._._.


import List
import Data.List
import Data.Set
import Data.Ord (comparing)
 
lsort :: [[a]] -> [[a]]
lsort = sortBy (comparing length)

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
  | otherwise = return acc




    
filterByLength x ls = List.filter (\n -> length n == x) ls

getLengthSists x ls = getLengthSistsH x ls []

getLengthSistsH [] _ acc = acc
getLengthSistsH (x:xs) ls acc = getLengthSistsH xs ls ((filterByLength x ls):acc)

lengthSet :: [[a]]-> [Int]
lengthSet ls = toAscList (fromAscList (List.map length ls))

split :: String -> Char -> [String]
split [] delim = [""]
split (c:cs) delim
   | c == delim = "" : rest
   | otherwise = (c : head rest) : tail rest
         where
                rest = Main.split cs delim


groupByElemIndices l ls = 


groupByElemIndicesH l word ls = 
  filter ind ls
  where
    ind x = x == elemIndices l word

  

findMaxWord :: [String]->String->String
findMaxWord dictionary letters = findMaxWordH (List.map (\x -> (x,x)) dictionary) (buildLetterSet dictionary) letters
    
deleteAllelements :: Char->(String,String)->(String,String)
deleteAllelements l (a,b) = ((concat (Main.split a l)),b)


makeNextDoubleDict doubleDict l = (List.map (deleteAllelements l) doubleDict)

findMaxWordH :: [(String,String)]->String->String->String
findMaxWordH [(_,ans)]    _         _         = ans   
findMaxWordH double_dict letterSet (l:etters) = 
  do
    if elem l letterSet
    then findMaxWordH  (makeNextDoubleDict double_dict l) (List.delete l letterSet) etters
    else findMaxWordH double_dict letterSet etters



buildLetterSet :: [String]->String
buildLetterSet ss = toList (fromList (intercalate "" ss))


getAll x cases
  | x<= cases =
    do
      nm <- getNM
      dictionary <- getLines 1 (head(nm)) []
      sequences <- getLines 1 (head(tail(nm))) []
      putStrLn ("Case #"++(show x)++": "++ ((show nm)++"\n"++(show (lsort dictionary)++"\n"++(show (lsort sequences)))))
      getAll (x+1) cases
  | otherwise = return ()
                    
--main = 
--  do
--    cases <- readLn
--    --putStrLn (show cases)
--    getAll 1 cases
