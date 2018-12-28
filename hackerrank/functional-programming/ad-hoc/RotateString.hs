-- The main function
main :: IO ()
main = fmap rotateString . tail . lines <$> getContents >>= mapM_ (putStrLn . unwords)

-- Rotate the string
rotateString :: String -> [String]
rotateString s = y [tail s ++ [head s]] (tail s ++ [head s]) (length s)
  where
    y l _ 1 = l
    y l s i = y (l ++ [tail s ++ [head s]]) (tail s ++ [head s]) (i - 1)
