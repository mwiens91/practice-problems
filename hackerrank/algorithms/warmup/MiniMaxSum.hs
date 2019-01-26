import           Data.List                      ( sort )

-- The main function
main :: IO ()
main =
    unwords
        .   fmap show
        .   findExtremeSeqs
        .   fmap read
        .   words
        <$> getContents
        >>= putStrLn

findExtremeSeqs :: [Int] -> [Int]
findExtremeSeqs l = [sum $ take 4 sorted, sum $ drop 1 sorted]
    where sorted = sort l
