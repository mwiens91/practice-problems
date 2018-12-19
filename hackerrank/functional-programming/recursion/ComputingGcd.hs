-- The main function
main :: IO ()
main = uncurry computeGCD . parseInput <$> getLine >>= print

-- Parse the input
parseInput :: String -> (Int, Int)
parseInput l = listToTuple $ read <$> words l
  where
    listToTuple (x : xs : _) | x > xs    = (x, xs)
                             | otherwise = (xs, x)

-- Compute GCD. Expects the largest number first.
computeGCD :: Int -> Int -> Int
computeGCD q 0 = q
computeGCD q r = computeGCD r (rem q r)
