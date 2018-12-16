main :: IO ()
main = sumOddElements <$> fmap read <$> lines <$> getContents >>= print

sumOddElements :: [Int] -> Int
sumOddElements array = sum $ filter odd array
