-- The main function
main :: IO ()
main = reduceString [] <$> getLine >>= putStrLn

reduceString :: String -> String -> String
reduceString _ [] = mempty
reduceString seenList s
    | head s `elem` seenList = reduceString seenList (tail s)
    | otherwise = head s : reduceString (head s : seenList) (tail s)
