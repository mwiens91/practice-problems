-- The main function
main :: IO ()
main = solveCases . tail . lines <$> getContents >>= mapM_ putStrLn
    where solveCases = fmap permuteMe

-- Permute string as described by problem
permuteMe :: String -> String
permuteMe []             = []
permuteMe (x1 : x2 : xs) = [x2, x1] ++ permuteMe xs
