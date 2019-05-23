import qualified Data.Text as Text
import Data.List.Split
import Control.Monad

-- "the IO monad taints everything that uses it" - drumfire
-- https://stackoverflow.com/a/1675664/5732397

english :: IO [Text.Text]
english = do
    f <- readFile "english_words.txt"
    return (Text.lines (Text.pack f))
    
board :: IO [String]
board = do
    f <- readFile "board.txt"
    return (chunksOf 4 f)
   
-- TODO: Use consecutive-word optimization   
findEligible :: IO String -> Integer -> [Text.Text] -> IO Text.Text
findEligible s d words = s >>= (\str -> words >>= (\wds -> filter (Text.isPrefixOf (Text.pack str)) wds))

getAdjacentCoords :: (Integer, Integer) -> [(Integer, Integer)]
getAdjacentCoords (a,b) =  filter (\(y, x) -> (max x y) <= 3 && (min x y) >= 0 && (y,x) /= (a,b)) [(a+dy,b+dx) | dy <- [-1,0,1], dx <- [-1,0,1]]
    
findWords :: (Integer, Integer) -> IO [String] -> [(Integer, Integer)] -> Integer -> IO String -> IO [Text.Text] -> IO [Text.Text]
findWords (a,b) board path depth tempWord prevSubset = do
    let char = board >>= (\x -> x !! a !! b)
    let newTempWord = tempWord ++ [char]
    let newSubset = findEligible newTempWord 0 prevSubset
    let newPath = path ++ [a,b]
    if length newSubset > 0
        then do 
            let recursion = map (\(y,x) -> findWords (y,x) board newPath (depth+1) newTempWord newSubset) (getAdjacentCoords (a,b))
            return (if elem newTempWord newSubset then [newTempWord] ++ recursion else recursion)
        else do return []
        
        

--main = map putStrLn (findEligible "test" 0 (readFileLines "board.txt"))
