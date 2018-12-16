main :: IO ()
main = do
    -- Parse input
    (multi, array) <- fmap parseInputLines $ lines <$> getContents

    -- Get our expanded array
    let expArray = expandArray multi array

    -- Print it!
    mapM_ print expArray


-- Parse our input
parseInputLines :: [String] -> (Int, [Int])
parseInputLines inputLines = (head x, tail x)
    where x = read <$> inputLines

-- Copy each array element multiple times
expandArray :: Int -> [Int] -> [Int]
expandArray multiplier array = array >>= replicate multiplier
