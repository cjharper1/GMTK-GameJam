## A 2D mathematical vector.
## The type of the components depends on what's given to the vector.
## \author  Jacob Pike
## \date    09/01/2018
class Vector2(object):    
    ## Initializes the vector's components.
    ## @param[in]   x - The x component.
    ## @param[in]   y - The y component.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def __init__(self, x, y):
        ## The x (horizontal) component.
        self.X = x
        ## The y (horizontal) component.
        self.Y = y

    ## Returns the vector as an (x, y) tuple.
    ## \return  The vector as an (x, y) tuple.
    ## \author  Jacob Pike
    ## \date    09/01/2018
    def AsXYTuple(self):
        return (self.X, self.Y)

    ## Compares the vector to another vector.
    ## \return  True if the two vectors have the same components, or false otherwise.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def __eq__(self, other):
        if isinstance(other, Vector2):
            return (self.X == other.X) and (self.Y == other.Y)
        return False

    ## Returns a hash value for the vector. Must be overridden
    ## because __eq__ is overridden.
    ## \return  The hash of the vector.
    ## \author  Tom Rogan
    ## \date    09/01/2018
    def __hash__(self):
        return self.X ^ self.Y