main :: IO ()
main =
    fmap (evaluateExp . read) . tail . lines <$> getContents >>= mapM_ print


-- Evaluate first 10 terms (0-indexed) of exponential Taylor series
evaluateExp :: Double -> Double
evaluateExp x = y x 0
  where
    y x termNum
        | termNum == 10 = 0
        | otherwise = x ^ termNum / fromIntegral (factorial termNum) + y
            x
            (termNum + 1)


-- Textbook factorial function
factorial :: (Integral a) => a -> a
factorial n = product [1 .. n]
