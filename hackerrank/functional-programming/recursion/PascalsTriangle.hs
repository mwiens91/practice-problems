-- The main function
main :: IO ()
main = read <$> getLine >>= printTriangle

-- Print Pascal's Triangle
printTriangle :: Int -> IO ()
printTriangle = printTriangle' 0
  where
    printTriangle' _ 0 = mempty
    printTriangle' rowNum rowRem =
        printTriangleRow rowNum >> printTriangle' (rowNum + 1) (rowRem - 1)

-- Print a row of the triangle
printTriangleRow :: Int -> IO ()
printTriangleRow r = putStrLn $ unwords $ show <$> getTriangleRow r

-- Get a list of numbers for one row of the triangle
getTriangleRow :: Int -> [Int]
getTriangleRow r = fmap nthTerm [0 .. r]
    where nthTerm n = factorial r `div` (factorial n * factorial (r - n))

-- Textbook factorial function
factorial :: (Integral a) => a -> a
factorial n = product [1 .. n]
