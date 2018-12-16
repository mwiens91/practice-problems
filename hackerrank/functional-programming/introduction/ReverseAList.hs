main :: IO ()
main = fmap reverseList (lines <$> getContents) >>= mapM_ putStrLn


-- Reverse a list
reverseList :: [a] -> [a]
reverseList [] = []
reverseList (x : xs) = reverseList xs ++ [x]
