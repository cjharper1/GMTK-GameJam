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
