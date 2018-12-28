import           Data.Map.Strict                ( Map )
import qualified Data.Map.Strict               as Map

-- The main function
main :: IO ()
main =
    fmap (uncurry solveProblem . toTuple . fmap read . words)
        .   tail
        .   lines
        <$> getContents
        >>= mapM_ print
    where toTuple (x1 : x2 : _) = (x1, x2)


-- Solve the problem here
solveProblem :: Integer -> Integer -> Integer
solveProblem x1 x2 =
    foldr (\x y -> (x + 1) * y) 1 (countPrimeFactors $ gcd x1 x2)


-- Build a map of prime factors of a number
countPrimeFactors :: Integer -> Map Integer Integer
countPrimeFactors n = countPrimeFactors' n Map.empty

countPrimeFactors' :: Integer -> Map Integer Integer -> Map Integer Integer
countPrimeFactors' 1 map = map
countPrimeFactors' n map = countPrimeFactors' (n `div` p) (addToFreqMap p map)
    where p = findPrimeFactor n

addToFreqMap :: Integer -> Map Integer Integer -> Map Integer Integer
addToFreqMap n map = do
    -- Test if we've seen this already
    let haveSeen = Map.member n map

    -- Update
    if haveSeen then Map.adjust (+ 1) n map else Map.insert n 1 map


-- Find a prime factor—not very efficient
findPrimeFactor :: Integer -> Integer
findPrimeFactor n = if null factors then n else head factors
    where factors = filter (\x -> (n `mod` x) == 0) [2 .. n - 1]
