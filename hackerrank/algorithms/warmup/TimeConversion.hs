import           Data.Text                      ( pack
                                                , strip
                                                , unpack
                                                )

-- The main function
main :: IO ()
main = do
    -- Parse input
    timeStr <- unpack . strip . pack <$> getContents

    let timeStr'      = take 8 timeStr
    let meridian      = [timeStr !! 8, timeStr !! 9]
    let isTwelvthHour = take 2 timeStr == "12"

    -- Convert the time
    let result | meridian == "PM" && not isTwelvthHour = add12Hours timeStr'
               | meridian == "AM" && isTwelvthHour = "00" ++ drop 2 timeStr'
               | otherwise = timeStr'


    -- Output the result
    putStrLn result


add12Hours :: String -> String
add12Hours s = show hours ++ drop 2 s
    where hours = 12 + (read $ take 2 s :: Integer)
