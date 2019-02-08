main :: IO ()
main =
    fmap (numWorstSocks . read) . tail . lines <$> getContents >>= mapM_ print

numWorstSocks :: Int -> Int
numWorstSocks x = x + 1
