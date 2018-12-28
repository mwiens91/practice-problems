-- Top level constants
modulus = 1000000007

-- The main function
main :: IO ()
main =
    (`mod` modulus)
        .   uncurry computeGcd'
        .   parseInput
        <$> getContents
        >>= print

-- Parse input
parseInput :: String -> ([Integer], [Integer])
parseInput input = (inputLines !! 1, inputLines !! 3)
    where inputLines = fmap (fmap read . words) . lines $ input

-- Solve problem
computeGcd' :: [Integer] -> [Integer] -> Integer
computeGcd' as bs = computeGcd (product as) (product bs)

computeGcd :: Integer -> Integer -> Integer
computeGcd q 0 = q
computeGcd q r = computeGcd r (rem q r)
