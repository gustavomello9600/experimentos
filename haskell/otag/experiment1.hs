import qualified Data.Matrix as Mat
import Data.List (sort)


-- Output channel for visualizing the manipulation of objects
main = print
     . reverse
     . sort
     . testEach
     $ designSamples
     where
         testEach = map test
         designSamples = zipWith ($) [flipFirst, flipFirstTwo, flipFirstThree] envinronmentSample


-- Type aliases
type Gene = Mat.Matrix Bool
type State = Int -- Mock State
type Population = [Design]


{- Des
Category of engineering structures designs which morfisms are operators that take its
source as a input and outputs its target. -}


class Testable a where
    getFitness :: a -> Maybe Float


-- Objects in the Des category
data Design = Design {
                  gene :: Gene,
                  fitness :: Maybe Float
              } deriving Show

instance Testable Design where
    getFitness = fitness


-- A morfism in the Des category is simply any operator where:
-- operator :: Design -> Design


-- Structure of Tested Designs as an endofunctor Des -> Des
newtype Tested a = Tested a deriving Show

instance Functor Tested where
    fmap o (Tested d) = Tested (o d)

instance (Testable a) => Eq (Tested a) where
    (Tested d1) == (Tested d2) = (getFitness d1) == (getFitness d2)

instance (Testable a) => Ord (Tested a) where
    compare (Tested d1) (Tested d2) = compare (getFitness d1) (getFitness d2)

-- Natural Transformation that produces Tested Designs
test :: Design -> Tested Design
test (Design g a) = Tested . Design g . Just $ fea g


---------------------------------------
-- # Utilities for testing the model --
---------------------------------------

-- Mock implementation of finite element analysis
fea :: Gene -> Float
fea = foldr1 (+) . fmap (fromIntegral . fromEnum)

genericGeneticOperator :: Design -> Design
genericGeneticOperator (Design gene a) = Design (flipBit (1, 1) gene) a

flipFirst      (Design gene a) = Design (flipBit (1, 1) $ gene) a
flipFirstTwo   (Design gene a) = Design (flipBit (1, 2) . flipBit (1, 1) $ gene) a
flipFirstThree (Design gene a) = Design (flipBit (1, 3) . flipBit (1, 2) . flipBit (1, 1) $ gene) a
 
flipBit :: (Int, Int) -> Gene -> Gene 
flipBit (i, j) gene = Mat.setElem (not elem) (i, j) gene
    where
        elem = Mat.getElem i j gene

designSample = Design (Mat.fromList 3 3 $ repeat False) Nothing
designSamples = repeat designSample
envinronmentSample = take 3 designSamples
