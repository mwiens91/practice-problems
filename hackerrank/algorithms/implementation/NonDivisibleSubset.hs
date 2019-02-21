import           Data.List                      ( splitAt )


-- Count remainders
countRemainders :: Int -> [Int] -> [Int] -> [Int]
countRemainders _ rems []   = rems
countRemainders k rems nums = do
    let rem          = head nums `mod` k
    let (l1, _ : l2) = splitAt rem rems

    countRemainders k (l1 ++ ((rems !! rem) + 1) : l2) (tail nums)


-- Perform the operation of finding the maximum occurances of the
-- remainders that add to k
maxOfRemPairs :: [Int] -> Int -> Int
maxOfRemPairs [] accum = accum
maxOfRemPairs s  accum = maxOfRemPairs s' (accum + max l r)
  where
    l  = head s
    r  = last s
    s' = tail $ init s


-- The main function
main :: IO ()
main = do
    -- Parse input
    inputLines <-
        fmap (fmap read . words) . lines <$> getContents :: IO [[Int]]

    let k             = last $ head inputLines
    let s             = last inputLines

    -- Count the remainder of all elements of s when divided by k
    let rems          = countRemainders k (replicate k 0) s

    -- If there are any number of numbers that k divides on its own,
    -- we'll include one of them. Same with numbers a such that k
    -- divides a * 2
    let kEven         = k `mod` 2 == 0
    let kHalf         = k `div` 2
    let remZeroTerm   = if head rems /= 0 then 1 else 0
    let remMiddleTerm = if kEven && rems !! kHalf /= 0 then 1 else 0

    -- Then for the remaining numbers of s, pick the maximum of the
    -- number of occurances of a, b such that k divides a/k + a/b
    let remainingRems = tail $ if kEven
            then take kHalf rems ++ drop (kHalf + 1) rems
            else rems

    -- Print the answer
    let answer = remZeroTerm + remMiddleTerm + maxOfRemPairs remainingRems 0

    print answer
