-- Top level constants
red = 'R'
grn = 'G'
yel = 'Y'
blu = 'B'

-- The main function
main :: IO ()
main = fmap isFullOfColors' . tail . lines <$> getContents >>= mapM_ print
    where isFullOfColors' = isFullOfColors 0 0 0 0

-- Determine if a given sequence ie "full of colors"
isFullOfColors :: Int -> Int -> Int -> Int -> String -> Bool
isFullOfColors numR numG numY numB [] | numR == numG && numY == numB = True
                                      | otherwise                    = False
isFullOfColors numR numG numY numB str =
    numR' - numG' < 2 && numY' - numB' < 2 && isFullOfColors numR'
                                                             numG'
                                                             numY'
                                                             numB'
                                                             (tail str)
  where
    [numR', numG', numY', numB'] =
        incrementCounts numR numG numY numB (head str)


-- Increase color counts
incrementCounts :: Int -> Int -> Int -> Int -> Char -> [Int]
incrementCounts numR numG numY numB chr
    | chr == red = [numR + 1, numG, numY, numB]
    | chr == grn = [numR, numG + 1, numY, numB]
    | chr == yel = [numR, numG, numY + 1, numB]
    | otherwise  = [numR, numG, numY, numB + 1]
