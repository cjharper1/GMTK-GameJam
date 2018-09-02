import math

## A 2D mathematical vector.
## The type of the components depends on what's given to the vector.
## \author  Jacob Pike
## \date    09/01/2018
class Vector2(object):    
    ## Normalizes a vector to be a unit vector of length 1.
    ## @param[in]   vector - The Vector2 to normalize.
    ## @return  A normalized Vector2 of the provided vector.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    @staticmethod
    def Normalize(vector):
        normalized_x = vector.X / vector.Length
        normalized_y = vector.Y / vector.Length
        normalized_vector = Vector2(normalized_x, normalized_y)
        return normalized_vector

    ## Creates a scaled version of a vector.
    ## @param[in]   scale_factor - The amount to scale the vector.
    ## @param[in]   vector - The Vector2 to scale.
    ## @return The scaled Vector2.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    @staticmethod
    def Scale(scale_factor, vector):
        scaled_x = scale_factor * vector.X
        scaled_y = scale_factor * vector.Y
        return Vector2(scaled_x, scaled_y)

    ## Negates a vector.
    ## @param[in]   vector - The Vector2 to negate.
    ## @return The negated Vector2.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    @staticmethod
    def Negate(vector):
        negated_vector = Vector2.Scale(-1, vector)
        return negated_vector

    ## Adds two vectors.
    ## @param[in]   vector1 - One Vector2 to add.
    ## @param[in]   vector2 - The other Vector2 to add.
    ## @return The Vector2 addition of the provided vectors.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    @staticmethod
    def Add(vector1, vector2):
        added_x = vector1.X + vector2.X
        added_y = vector1.Y + vector2.Y
        return Vector2(added_x, added_y)

    ## Subtracts two vectors.
    ## @param[in]   vector1 - The Vector2 to subtract from.
    ## @param[in]   vector2 - The other Vector2 to subtract.
    ## @return The Vector2 subtraction of the provided vectors.
    ## \author  Jacob Pike
    ## \date    09/02/2018
    @staticmethod
    def Subtract(vector1, vector2):
        subtracted_x = vector1.X - vector2.X
        subtracted_y = vector1.Y - vector2.Y
        return Vector2(subtracted_x, subtracted_y)

    ## The length of the vector.
    @property
    def Length(self):
        squared_length = (self.X * self.X) + (self.Y * self.Y)
        length = math.sqrt(squared_length)
        return length

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