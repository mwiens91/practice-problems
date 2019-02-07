import           Data.Text                      ( pack
                                                , strip
                                                , unpack
                                                )

main :: IO ()
main = do
    -- Parse input
    inputNums <- words . unpack . strip . pack <$> getContents

    let n = read (head inputNums) :: Int
    let m = read (last inputNums) :: Int

    -- Process input
    let n' = n `div` 2 + if n `mod` 2 /= 0 then 1 else 0
    let m' = m `div` 2 + if m `mod` 2 /= 0 then 1 else 0

    -- Print result
    print $ n' * m'
