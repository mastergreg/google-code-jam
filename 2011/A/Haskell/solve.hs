-- -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
--
-- File Name : solve.hs
--
-- Purpose :
--
-- Creation Date : 06-09-2011
--
-- Last Modified : Tue 06 Sep 2011 07:24:54 PM EEST
--
-- Created By : Greg Liras <gregliras@gmail.com>
--
--_._._._._._._._._._._._._._._._._._._._._.

rInt x = read x :: Integer

getStats :: IO [Integer]
getStats =
  do
    inp <- getLine
    return (map rInt (split inp ' '))

condition0 :: Integer->Integer->Bool
condition0 pD pG =
  do
    if pG == 0
    then
      if pD == 0
      then True
      else False
    else True
condition1 :: Integer->Integer->Bool
condition1 pD pG = 
  do
    if pG == 100 
    then 
      if pD == 100
      then True
      else False
    else True

isInt x = x == fromInteger (round x)


condition2 ::[Integer]->Integer->Integer->Bool
condition2 []     pD pG = False
condition2 (n:ns) pD pG =
  do
    if isInt (fromIntegral(n*pD)/100)
    then True
    else condition2 ns pD pG


checkStats :: [Integer] -> Bool
checkStats [n,pD,pG]  =  (condition0 pD pG ) && (condition1 pD pG) && (condition2 [1..n] pD pG)
checkStats _          = False
    

printStats :: Bool -> String
printStats True = "Possible"
printStats False = "Broken"



split :: String -> Char -> [String]
split [] delim = [""]
split (c:cs) delim
   | c == delim = "" : rest
   | otherwise = (c : head rest) : tail rest
         where
                rest = split cs delim
getAll x cases
  | x<= cases =
    do
      first <- getStats
      putStrLn ("Case #"++(show x)++": "++(printStats (checkStats first)))
      getAll (x+1) cases
  | otherwise = return ()
main = 
  do
    cases <- readLn
    --putStrLn (show cases)
    getAll 1 cases
