-- Find a prime factor—not very efficient
findPrimeFactor :: Integer -> Integer
findPrimeFactor 1 = 1
findPrimeFactor 2 = 2
findPrimeFactor 3 = 3
findPrimeFactor n = if null factors then 1 else head factors
    where factors = filter (\x -> (n `mod` x) == 0) [2 .. n - 1]
