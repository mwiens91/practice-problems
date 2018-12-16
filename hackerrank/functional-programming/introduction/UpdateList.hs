main :: IO ()
main = fmap abs <$> fmap read <$> lines <$> getContents >>= mapM_ print
