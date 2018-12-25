import           Data.Foldable                  ( toList )
import           Data.Monoid                    ( (<>) )


-- Top level constants
emptyNode = -1


-- Datatype for tree. Thanks to hololeap on HackerRank for the help!
data Tree a = Tree (Tree a) a (Tree a) | Empty deriving (Eq)

instance Foldable Tree where
    foldMap _ Empty        = mempty
    foldMap f (Tree l a r) = foldMap f l <> f a <> foldMap f r

findTreeDepth :: Tree a -> Int
findTreeDepth tree = findDepth tree 1
  where
    findDepth Empty        d = d
    findDepth (Tree l a r) d = max (findDepth l $ d + 1) (findDepth r $ d + 1)

showTree :: Show a => Tree a -> String
showTree = unwords . fmap show . toList

printTree :: Show a => Tree a -> IO ()
printTree tree = putStrLn $ showTree tree


-- The main function
main :: IO ()
main = do
    -- Get input
    inputLines <-
        fmap (fmap read . words) . lines <$> getContents :: IO [[Int]]

    -- Unpack input
    let numNodes  = head $ head inputLines
    let nodeLines = take numNodes $ tail inputLines
    let kVals     = concat $ drop (numNodes + 2) inputLines

    -- Build the tree
    let tree      = buildTree nodeLines 1

    -- Swap nodes and print trees
    let treeDepth = findTreeDepth tree
    let treeList  = swapThenFold treeDepth kVals [tree]

    mapM_ printTree (tail treeList)


-- Given a list of k values, swap nodes, keep the tree, and then fold
swapThenFold :: Int -> [Int] -> [Tree Int] -> [Tree Int]
swapThenFold _ [] l = l
swapThenFold d ks l = do
    let oldTree = last l
    let newTree = swapNodesWithK d (head ks) 1 oldTree

    swapThenFold d (tail ks) (l ++ [newTree])


-- Build a tree
buildTree :: [[Int]] -> Int -> Tree Int
buildTree _         (-1) = Empty
buildTree nodeLines i    = Tree (buildTree' $ head nodeLine)
                                i
                                (buildTree' $ nodeLine !! 1)
  where
    buildTree' = buildTree nodeLines
    nodeLine   = nodeLines !! (i - 1)


-- Swap tree nodes for a given k
swapNodesWithK :: Int -> Int -> Int -> Tree Int -> Tree Int
swapNodesWithK d k i tree = do
    let tree'    = swapNodes (k * i) 1 tree
    let i'       = i + 1
    let continue = k * i' < d

    if continue then swapNodesWithK d k i' tree' else tree'


-- Swap tree nodes at a specific depth
swapNodes :: Int -> Int -> Tree Int -> Tree Int
swapNodes _ _ Empty = Empty
swapNodes k d (Tree l a r)
    | k == d    = Tree r a l
    | otherwise = Tree (swapNodes k (d + 1) l) a (swapNodes k (d + 1) r)
