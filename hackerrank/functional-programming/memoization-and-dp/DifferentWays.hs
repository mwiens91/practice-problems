-- The main function
main :: IO ()
main = fmap ((`mod` 100000007) . nChoosek') <$> inputVals >>= mapM_ print
  where
    inputVals =
        tail . fmap (fmap read . words) . lines <$> getContents :: IO [[Integer]]
    nChoosek' l = nChoosek (head l) (l !! 1)

-- Binomial coefficient
nChoosek :: Integral p => p -> p -> p
nChoosek n 0 = 1
nChoosek n k =
    product [1 .. n] `div` product [product [1 .. k], product [1 .. n - k]]
