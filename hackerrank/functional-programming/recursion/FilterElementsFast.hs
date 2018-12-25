import           Data.Map.Strict                ( Map
                                                , (!)
                                                )
import qualified Data.Map.Strict               as Map
import           Data.Set                       ( Set )
import qualified Data.Set                      as Set

-- Top level constants
noResult = -1

-- The main function
main :: IO ()
main =
    fmap solveTestCase
        .   getTestCases
        .   fmap (fmap read . words)
        .   tail
        .   lines
        <$> getContents
        >>= mapM_ printTestCaseResult

-- Parse input into test cases
getTestCases :: [[Int]] -> [[[Int]]]
getTestCases []             = mempty
getTestCases (l1 : l2 : ls) = [l1, l2] : getTestCases ls

-- Print result of each test case
printTestCaseResult :: [Int] -> IO ()
printTestCaseResult [] = print noResult
printTestCaseResult l  = putStrLn $ unwords . fmap show $ l

-- Solve each test case
solveTestCase :: [[Int]] -> [Int]
solveTestCase l = do
    -- Unpack test case
    let n        = head l !! 1
    let testNums = l !! 1

    -- Build frequency map
    let freqMap  = buildFrequencyMap testNums Map.empty

    -- Build the results list
    buildResultsList n freqMap Set.empty [] testNums

-- Build results list
buildResultsList :: Int -> Map Int Int -> Set Int -> [Int] -> [Int] -> [Int]
buildResultsList _ _       _       l       []       = l
buildResultsList n freqMap seenSet resList testList = do
    -- Unpack the value
    let val           = head testList

    -- Determine whether we're inserting an element
    let insertElement = freqMap ! val >= n && not (Set.member val seenSet)

    -- Update our results and seen containers
    let resList' = if insertElement then resList ++ [val] else resList
    let seenSet' = if insertElement then Set.insert val seenSet else seenSet

    -- Recurse
    buildResultsList n freqMap seenSet' resList' (tail testList)

-- Build frequency map
buildFrequencyMap :: [Int] -> Map Int Int -> Map Int Int
buildFrequencyMap [] m = m
buildFrequencyMap l  m = buildFrequencyMap (tail l) (updateMap m $ head l)

-- Update frequency of key in map
updateMap :: Map Int Int -> Int -> Map Int Int
updateMap freqMap k | Map.member k freqMap = Map.adjust (+ 1) k freqMap
                    | otherwise            = Map.insert k 1 freqMap
