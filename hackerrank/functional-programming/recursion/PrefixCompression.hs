-- The main function
main :: IO ()
main = uncurry getAnswers . toTuple . lines <$> getContents >>= mapM_ putStrLn
    where toTuple (x1 : x2 : _) = (x1, x2)

-- Get the answers to print as a list of strings here
getAnswers :: String -> String -> [String]
getAnswers s1 s2 = do
    -- Split right before this index
    let splitIdx = findCommonPrefixIdx s1 s2 0

    -- Do splitting
    let prefix = take splitIdx s1
    let s1Rem = drop splitIdx s1
    let s2Rem = drop splitIdx s2

    -- Lengths as strings
    let prefixLenStr = show $ length prefix
    let s1RemLenStr = show $ length s1Rem
    let s2RemLenStr = show $ length s2Rem

    [prefixLenStr ++ " " ++ prefix, s1RemLenStr ++ " " ++ s1Rem, s2RemLenStr ++ " " ++ s2Rem]


-- Find the last index of the common prefix of two strings
findCommonPrefixIdx :: String -> String -> Int -> Int
findCommonPrefixIdx [] _  idx = idx
findCommonPrefixIdx _  [] idx = idx
findCommonPrefixIdx (x : xs) (y : ys) idx
    | x == y    = findCommonPrefixIdx xs ys (idx + 1)
    | otherwise = idx
