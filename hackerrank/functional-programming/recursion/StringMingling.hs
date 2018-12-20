-- The main function
main :: IO ()
main = uncurry mangleStrings . toTuple . lines <$> getContents >>= putStrLn
    where toTuple (x1 : x2 : _) = (x1, x2)

-- Mangle the strings to produce the answer
mangleStrings :: String -> String -> String
mangleStrings a b = concat $ zipWith charCat a b
    where charCat x y = [x, y]
