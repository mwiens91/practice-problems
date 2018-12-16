main :: IO ()
main = fmap evens (lines <$> getContents) >>= mapM_ putStrLn


-- Filter out all odd positions in a list (1-indexed)
evens :: [a] -> [a]
evens [] = []
evens [x] = []
evens (e1 : e2 : xs) = e2 : evens xs
