import Data.Sequence (foldrWithIndex, fromList)

-- The main function
main :: IO ()
main = computeArea . parseInput <$> getContents >>= print

-- Parse the input
parseInput :: String -> [[Int]]
parseInput dump = tail $ (fmap . fmap) read (words <$> lines dump)

-- Compute term in area calculation
computeTerm :: [Int] -> [Int] -> Int
computeTerm x1 x2 = head x1 * x2 !! 1 - x1 !! 1 * head x2

-- Compute area given a list of points
computeArea :: [[Int]] -> Double
computeArea points = abs $ (/ 2) $ fromIntegral $ foldrWithIndex
    computeTermAccum
    0
    (fromList points)
  where
    computeTermAccum idx point accum
        | idx == 0  = computeTerm point (last points) + accum
        | otherwise = computeTerm point (points !! (idx - 1)) + accum
