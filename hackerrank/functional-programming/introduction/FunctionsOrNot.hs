import Data.Set (fromList, toList)

-- The main function
main :: IO ()
main = getTestCases <$> getContents >>= mapM_ solveTestCase


-- Parse all input as a string and return test cases
getTestCases :: String -> [[[Int]]]
getTestCases inputString = do
    let parsedLines = (fmap . fmap) read (words <$> lines inputString)
    let numCases = (head . head) parsedLines

    unfoldTestCases numCases $ tail parsedLines


-- Recurse through parsed list of lines and get test cases
unfoldTestCases :: Int -> [[Int]] -> [[[Int]]]
unfoldTestCases 0 parsedLines = mempty
unfoldTestCases n parsedLines = take numLines remLines
    : unfoldTestCases (n - 1) (drop numLines remLines)
  where
    numLines = (head . head) parsedLines
    remLines = tail parsedLines


-- Get keys for each test case
getKeys :: [[Int]] -> [Int]
getKeys pairs = head <$> pairs


-- See if a key is uniquely mapped
keyIsUnique :: Int -> [[Int]] -> Bool
keyIsUnique key pairs =
    uniqueCheck $ (!! 1) <$> filter (\x -> head x == key) pairs

uniqueCheck :: [Int] -> Bool
uniqueCheck l = length ((toList . fromList) l) == 1


-- Solve each test case
solveTestCase :: [[Int]] -> IO ()
solveTestCase t = do
    let truths = keyIsUnique' <$> getKeys t
            where keyIsUnique' key = keyIsUnique key t

    if and truths then putStrLn "YES" else putStrLn "NO"
