main :: IO ()
main = listLength . lines <$> getContents >>= print


-- Find length of list without using built-in methods
listLength :: [a] -> Int
listLength [] = 0
listLength (x : xs) = cnt xs 1
    where cnt xs init
           | null xs = init
           | otherwise = cnt (tail xs) (init + 1)
