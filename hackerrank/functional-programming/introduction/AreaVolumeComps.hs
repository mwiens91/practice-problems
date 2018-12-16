-- The main function
main :: IO ()
main = do
    -- Constants
    let step = 0.001

    -- Parse input
    aList <- parseInputLine
    bList <- parseInputLine
    [l, r] <- parseInputLine

    print $ estArea l r aList bList step
    print $ estVolume l r aList bList step


-- Grab and parse an input line
parseInputLine :: IO [Double]
parseInputLine = fmap read <$> fmap words getLine

-- Estimate area integral
estArea :: (Floating a, Enum a) => a -> a -> [a] -> [a] -> a -> a
estArea l r aVals bVals stepVal =
    sum $
    (* stepVal) . curveFn aVals bVals <$>
    [l, l + stepVal .. r]

-- Estimate volume integral
estVolume :: (Floating a, Enum a) => a -> a -> [a] -> [a] -> a -> a
estVolume l r aVals bVals stepVal =
    sum $
    (* pi) . (* stepVal) . (^ 2) . curveFn aVals bVals <$>
    [l, l + stepVal .. r]

-- Our curve function
curveFn :: Floating p => [p] -> [p] -> p -> p
curveFn aVals bVals xVal = sum $ curveTerm' <$> zip aVals bVals
    where curveTerm' (a, b) = curveTerm (a, b) xVal

-- A term in the curve function
curveTerm :: Floating a => (a, a) -> a -> a
curveTerm (a, b) x = a * x ** b
