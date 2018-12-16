main :: IO ()
main = do
    -- Parse input
    (delimiter, array) <- fmap parseInputLines $ lines <$> getContents

    -- Filter the array
    let filteredArray = filter (< delimiter) array

    -- Print it!
    mapM_ print filteredArray


-- Parse our input
parseInputLines :: [String] -> (Int, [Int])
parseInputLines inputLines = (head x, tail x)
    where x = read <$> inputLines
