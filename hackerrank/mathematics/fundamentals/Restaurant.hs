main :: IO ()
main =
    fmap (solveTestCase . fmap read . words)
        .   tail
        .   lines
        <$> getContents
        >>= mapM_ print

solveTestCase :: [Int] -> Int
solveTestCase dims = (l * b) `div` gcd l b ^ 2
  where
    l = head dims
    b = last dims
