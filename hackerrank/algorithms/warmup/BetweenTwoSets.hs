main :: IO ()
main =
    solveProblem . fmap (fmap read . words) . lines <$> getContents >>= print


-- Solve the problem
solveProblem :: Integral a => [[a]] -> Integer
solveProblem l = do
    -- Unpack input
    let a    = l !! 1
    let b    = l !! 2

    -- Find LCM of a and GCD of b
    let lcmA = toInteger $ foldr1 lcm a
    let gcdB = toInteger $ foldr1 gcd b

    countMultiples lcmA gcdB 1 0


-- Count how many multiples of a divide b
countMultiples :: Integer -> Integer -> Integer -> Integer -> Integer
countMultiples a b i count
    | a * i > b = count
    | otherwise = if b `mod` (a * i) == 0
        then countMultiples a b (i + 1) (count + 1)
        else countMultiples a b (i + 1) count
