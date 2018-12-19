-- The main function
main :: IO ()
main = getFibonacciNum . read <$> getLine >>= print

-- Get the nth fibonacci number
getFibonacciNum :: Int -> Int
getFibonacciNum = (map fib [0 ..] !!)
  where
    fib 1 = 0
    fib 2 = 1
    fib n = getFibonacciNum (n - 2) + getFibonacciNum (n - 1)
