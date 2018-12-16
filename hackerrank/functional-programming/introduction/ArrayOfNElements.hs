main :: IO ()
main = fmap (`replicate` 1) readLn >>= print
