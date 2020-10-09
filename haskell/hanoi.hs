import Data.List
import Data.Maybe
import Debug.Trace

main :: IO ()
main = do
  let (result, log) = hanoi
  putStrLn $ unlines log
  putStrLn $ "\n" ++ show result

hanoi :: ([[Int]], [String])
hanoi = solve ([[1, 2, 3, 4, 5, 6], [], []], ["Initial State"])
        where solve = compose movements
                where compose = foldr (.) id
                      movements = zipWith move [1..6] (replicate 6 2)

move :: Int -> Int -> ([[Int]], [String]) -> ([[Int]], [String])
move n targetStackIndex state
    | n /= minimumCurrentStack =
      let newState = move minimumCurrentStack untouchedStackIndex state
      in move n targetStackIndex newState
    | length targetStack /= 0 && n > minimumTargetStack =
      let newState = move minimumTargetStack untouchedStackIndex state
      in move n targetStackIndex newState
    | otherwise =
      let newTargetStack = n:targetStack
          newCurrentStack = currentStack \\ [n]
          newLog = log ++ [(stackNames !! currentStackIndex) ++ " moved to " ++ (stackNames !! targetStackIndex) ]
          indexes = [currentStackIndex, targetStackIndex, untouchedStackIndex]
          correspondingStacks = [newCurrentStack, newTargetStack, untouchedStack]
          newStacks = map snd $ sort $ zip indexes correspondingStacks
      in (newStacks, newLog)
    where (stacks, log) = state
          currentStackIndex = fromJust . findIndex (n `elem`) $ fst state
          untouchedStackIndex = head $ [0, 1, 2] \\ [currentStackIndex, targetStackIndex]
          targetStack = stacks !! targetStackIndex
          currentStack = stacks !! currentStackIndex
          untouchedStack = stacks !! untouchedStackIndex
          minimumCurrentStack = minimum currentStack
          minimumTargetStack = minimum targetStack

stackNames :: [String]
stackNames = ["A", "B", "C"]
