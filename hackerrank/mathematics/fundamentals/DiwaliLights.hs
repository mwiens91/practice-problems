-- Count the number of light permutations
numLights :: Integer -> Integer
numLights n = (2^n - 1) `mod` 100000

-- The main function
main :: IO ()
main = fmap (numLights . read) . tail . lines <$> getContents >>= mapM_ print
