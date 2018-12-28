import           Data.Map.Strict                ( Map )
import qualified Data.Map.Strict               as Map

-- The main function
main :: IO ()
main =
    fmap (uncurry solveProblem . toTuple . fmap read . words)
        .   tail
        .   lines
        <$> getContents
        >>= print
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
    where p = pollardRho n

addToFreqMap :: Integer -> Map Integer Integer -> Map Integer Integer
addToFreqMap n map = do
    -- Test if we've seen this already
    let haveSeen = Map.member n map

    -- Update
    if haveSeen then Map.adjust (+ 1) n map else Map.insert n 1 map


-- Pollard's rho algorithm for integer factorization
g :: Integer -> Integer -> Integer
g n x = x ^ 2 + 1 `mod` n

pollardSubStep :: Integer -> Integer -> Integer -> Integer
pollardSubStep n x y = do
    let x' = g n x
    let y' = g n $ g n y
    let d' = gcd (abs $ x' - y') n

    pollardInner n x' y' d'

pollardInner :: Integer -> Integer -> Integer -> Integer -> Integer
pollardInner n x y d | d == 1    = pollardSubStep n x y
                     | otherwise = d

pollardRho :: Integer -> Integer
pollardRho 1 = 1
pollardRho n = pollardInner n 2 2 1
