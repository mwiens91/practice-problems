import Data.Sequence (foldrWithIndex, fromList)

-- The main function
main :: IO ()
main = computePerimeter . parseInput <$> getContents >>= print

-- Parse the input
parseInput :: String -> [[Int]]
parseInput dump = tail $ (fmap . fmap) read (words <$> lines dump)

-- Distance between two points
getDistance :: [Int] -> [Int] -> Double
getDistance x1 x2 = sqrt $ sum $ zipWith y x1 x2
    where y a b = (fromIntegral a - fromIntegral b) ** 2

-- Compute perimeter given a list of points
computePerimeter :: [[Int]] -> Double
computePerimeter points = foldrWithIndex getDistance' 0 (fromList points)
  where
    getDistance' idx point accum
        | idx == 0  = getDistance point (last points) + accum
        | otherwise = getDistance point (points !! (idx - 1)) + accum
