import           Data.List                      ( elemIndex
                                                , group
                                                , nub
                                                , sort
                                                , sortBy
                                                )

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

-- Solve each test case
solveTestCase :: [[Int]] -> [Int]
solveTestCase l = sortBy compareIndex' duplicateNums
  where
    duplicateNums = hasNDuplicates (head l !! 1) (l !! 1)
    compareIndex' = compareIndex (l !! 1)

-- Print result of each test case
printTestCaseResult :: [Int] -> IO ()
printTestCaseResult [] = print noResult
printTestCaseResult l  = putStrLn $ unwords . fmap show $ l

-- Comparison function relative to index in a list
compareIndex :: [Int] -> Int -> Int -> Ordering
compareIndex l x y = compare (elemIndex x $ nub l) (elemIndex y $ nub l)

-- Return which elements have N duplicates
hasNDuplicates :: Int -> [Int] -> [Int]
hasNDuplicates n = concatMap (useIfTwoPlus n) . group . sort
    where useIfTwoPlus n l = if length l >= n then [head l] else mempty
