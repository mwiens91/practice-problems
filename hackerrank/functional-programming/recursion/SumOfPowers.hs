-- The main function
main :: IO ()
main =
    uncurry findSolution
        .   toTuple
        .   fmap read
        .   lines
        <$> getContents
        >>= print
    where toTuple (x1 : x2 : _) = (x1, x2)

-- Kick of the recursion with this function
findSolution :: Int -> Int -> Int
findSolution x n = recurseSolution x n 0 startingNum
    where startingNum = floor $ fromIntegral x ** (1 / fromIntegral n)

-- Do the recursing here
recurseSolution :: Int -> Int -> Int -> Int -> Int
recurseSolution x n accum num
    | accum > x = 0
    | accum == x = 1
    | num == 0 = 0
    | otherwise = recurseSolution x n (accum + num ^ n) (num - 1)
    + recurseSolution x n accum             (num - 1)
