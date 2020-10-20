main = do print $ Line (Design [1, 2, 3]) (Best (Design [1, 0, 0]))

data Design = Design [Int] deriving Show
data Pop = Best Design | Line Design Pop deriving Show
