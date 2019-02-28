-- The main function
main :: IO ()
main =
    fmap (uncurry solveTestCase . tuplify . fmap read . words)
        .   tail
        .   lines
        <$> getContents
        >>= mapM_ (putStrLn . unwords . map show)
    where tuplify [x, y] = (x, y)


solveTestCase :: Int -> Int -> [Int]
solveTestCase n k
    | k == 0                           = [1 .. n]
    | n `mod` 2 == 0 && n `mod` k == 0 = solveFeasibleTestCase n k 1 1 []
    | otherwise                        = [-1]


solveFeasibleTestCase :: Int -> Int -> Int -> Int -> [Int] -> [Int]
solveFeasibleTestCase n k i sign perm
    | i == n + 1 = perm
    | i `mod` k == 0 = solveFeasibleTestCase n
                                             k
                                             (i + 1)
                                             (sign * (-1))
                                             (perm ++ [i + sign * k])
    | otherwise = solveFeasibleTestCase n
                                        k
                                        (i + 1)
                                        sign
                                        (perm ++ [i + sign * k])
