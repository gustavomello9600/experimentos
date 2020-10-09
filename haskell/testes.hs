main :: IO ()
main = print $ numLongChains

numLongChains :: Int
numLongChains = length $ filter isLong $ map chain [1..100]
  where
    isLong xs = length xs > 15

chain :: Int -> [Int]
chain 1 = [1]
chain n
    | odd n = n:chain (3*n + 1)
    | even n = n:chain (n `div` 2)
