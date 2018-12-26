-- The main function
main :: IO ()
main =
    fmap (getPentagonalNum . read)
        .   tail
        .   lines
        <$> getContents
        >>= mapM_ print


-- Get the nth pentagonal number
getPentagonalNum :: Integer -> Integer
getPentagonalNum n = (3 * n ^ 2 - n) `div`  2
