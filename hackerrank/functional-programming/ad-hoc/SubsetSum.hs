import           Data.List                      ( sortBy )
import           Data.Vector                    ( Vector
                                                , (!)
                                                )
import qualified Data.Vector                   as Vector

-- The main function
main :: IO ()
main = do
    -- Parse the input
    inputLines <-
        fmap (fmap read . words) . lines <$> getContents :: IO [[Integer]]

    let aList     = inputLines !! 1
    let testCases = concat $ drop 3 inputLines

    -- Sort the a list and make it an accumulated sums vector
    let aSums = Vector.fromList $ scanl1 (+) $ sortBy (flip compare) aList

    mapM_ print (binarySearch aSums <$> testCases)


-- Do a binary search. Return (index + 1) of number greater than the one
-- passed in. If not found, return -1.
binarySearch :: Vector Integer -> Integer -> Integer
binarySearch v x
    | x > Vector.last v
    = -1
    | otherwise
    = 1 + binarySearchIter v 0 (fromIntegral (Vector.length v) - 1) x

binarySearchIter :: Vector Integer -> Integer -> Integer -> Integer -> Integer
binarySearchIter v l r x | l < r     = binarySearchIter' v l r x
                         | otherwise = l

binarySearchIter' :: Vector Integer -> Integer -> Integer -> Integer -> Integer
binarySearchIter' v l r x = do
    let m    = (l + r) `div` 2
    let mVal = v ! fromIntegral m

    if mVal < x
        then binarySearchIter v (m + 1) r x
        else binarySearchIter v l m x
