import           Data.Map.Strict                ( Map
                                                , (!)
                                                )
import qualified Data.Map.Strict               as Map


-- The main function
main :: IO ()
main = do
    -- Grab and parse input
    parsedLines <-
        fmap (fmap read . words) . lines <$> getContents :: IO [[Int]]
    let numLines  = head $ head parsedLines
    let testLines = concat $ tail parsedLines

    -- Get the minimum of each power and how many times we've seen each
    -- power
    let resMaps = getPowerMaps Map.empty Map.empty testLines
    let minMap    = fst resMaps
    let freqMap   = snd resMaps

    -- Convert min map to list
    let minList   = Map.toAscList minMap

    -- Print the answers
    printResults freqMap numLines minList
    putStrLn ""


-- Get the minimum of each power and how many times we've seen each
-- power
getPowerMaps
    :: Map Int Int -> Map Int Int -> [Int] -> (Map Int Int, Map Int Int)
getPowerMaps minMap freqMap []             = (minMap, freqMap)
getPowerMaps minMap freqMap (x1 : x2 : xs) = do
    -- Have we seen this prime before?
    let haveSeen = Map.member x1 minMap

    -- Update maps
    let minMap' = if haveSeen
            then Map.adjust (min x2) x1 minMap
            else Map.insert x1 x2 minMap
    let freqMap' = if haveSeen
            then Map.adjust (+ 1) x1 freqMap
            else Map.insert x1 1 freqMap

    getPowerMaps minMap' freqMap' xs


-- Print the answers
printResults :: Map Int Int -> Int -> [(Int, Int)] -> IO ()
printResults _       _          []       = mempty
printResults freqMap totalLines minPairs = do
    -- Unpack our input
    let pair = head minPairs
    let p    = fst pair
    let n    = snd pair

    -- Print the pair if it occured in every line
    if freqMap ! p == totalLines
        then putStr (unwords (fmap show [p, n])) >> putStr " "
        else mempty

    -- Next pair
    printResults freqMap totalLines $ tail minPairs
