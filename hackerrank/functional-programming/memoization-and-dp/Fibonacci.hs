-- The main function
main :: IO ()
main =
    fmap (mod' . getFibonacciNum . read)
        .   tail
        .   lines
        <$> getContents
        >>= mapM_ print
    where mod' = flip rem 100000007


-- Get the nth fibonacci number
getFibonacciNum :: Int -> Integer
getFibonacciNum = (map fib [0 ..] !!)
  where
    fib 0 = 0
    fib 1 = 1
    fib n = getFibonacciNum (n - 2) + getFibonacciNum (n - 1)
