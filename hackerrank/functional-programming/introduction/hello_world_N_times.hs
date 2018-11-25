-- print "Hello World" n times
printHelloWorld :: Int -> IO ()
printHelloWorld 0 = return ()
printHelloWorld n = do
    putStrLn "Hello World"
    printHelloWorld (n - 1)

main :: IO ()
main = do
    n <- readLn
    printHelloWorld n
