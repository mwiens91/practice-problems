import           Data.IntMap.Strict             ( IntMap
                                                , (!)
                                                )
import qualified Data.IntMap.Strict            as IntMap
import           Data.List                      ( sort )


-- The main function
main :: IO ()
main =
    unwords
        .   fmap show
        .   uncurry findMissingNumbers
        .   parseInput
        <$> getContents
        >>= putStrLn


-- Parse input
parseInput :: String -> ([Int], [Int])
parseInput input = (inputLines !! 1, inputLines !! 3)
    where inputLines = fmap (fmap read . words) . lines $ input


-- Solve problem, recalling that B is a superset of A
findMissingNumbers :: [Int] -> [Int] -> [Int]
findMissingNumbers aList bList = do
    -- Compute frequency maps
    let aFreqMap     = computeFreqMap aList IntMap.empty
    let bFreqMap     = computeFreqMap bList IntMap.empty

    -- Get folding function
    let foldFunction = checkKeyFrequency aFreqMap bFreqMap

    -- Fold over keys
    sort $ IntMap.foldrWithKey foldFunction [] bFreqMap


computeFreqMap :: [Int] -> IntMap Int -> IntMap Int
computeFreqMap [] map = map
computeFreqMap l  map = do
    -- Test if we've seen this already
    let thisNum  = head l
    let haveSeen = IntMap.member thisNum map

    -- Update
    let map' = if haveSeen
            then IntMap.adjust (+ 1) thisNum map
            else IntMap.insert thisNum 1 map

    computeFreqMap (tail l) map'


checkKeyFrequency :: IntMap Int -> IntMap Int -> Int -> Int -> [Int] -> [Int]
checkKeyFrequency freqMapA freqMapB key _ list = do
    -- Test if the key is in the first map
    let keyExists = IntMap.member key freqMapA
    let valsEqual = keyExists && freqMapA ! key == freqMapB ! key

    if valsEqual then list else list ++ [key]
