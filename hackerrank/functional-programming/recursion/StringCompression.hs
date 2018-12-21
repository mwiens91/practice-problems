-- The main function
main :: IO ()
main = compressString <$> getLine >>= putStrLn

-- Compress a string
compressString :: String -> String
compressString = compressString' 1

-- Perform the meat of string compression recursively
compressString' :: (Show a, Num a, Eq a) => a -> String -> String
compressString' n [x] = countRepeated n x
compressString' n (x : xs)
    | x == head xs = compressString' (n + 1) xs
    | otherwise    = countRepeated n x ++ compressString' 1 xs

-- Display compressed result of repeat characters
countRepeated :: (Eq a, Num a, Show a) => a -> Char -> String
countRepeated n x | n == 1    = [x]
                  | otherwise = x : show n
