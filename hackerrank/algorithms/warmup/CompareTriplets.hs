-- The main function
main :: IO ()
main =
    solveProblem
        .   fmap (fmap read . words)
        .   lines
        <$> getContents
        >>= putStrLn
        .   unwords
        .   map show


-- Solve the problem
solveProblem :: [[Int]] -> [Int]
solveProblem = solveProblem' 0 0

-- TODO: refactor repetitive code
solveProblem' :: Int -> Int -> [[Int]] -> [Int]
solveProblem' a b l
    | l == [[], []] = [a, b]
    | otherwise = if head (head l) > head (last l)
        then solveProblem' (a + 1) b (tail <$> l)
        else if head (head l) < head (last l)
            then solveProblem' a (b + 1) (tail <$> l)
            else solveProblem' a b (tail <$> l)
