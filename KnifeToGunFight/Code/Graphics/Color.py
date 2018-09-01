import enum

## An RGB (red, green, blue) color value.
## Designed as an enumeration to list predefined colors.
class Color(enum.Enum):
    Black = (0, 0, 0)
    Blue = (0, 0, 255)
    FullGreen = (0, 255, 0)
    Gray = (128, 128, 128)
    Magenta = (255, 0, 255)
    Red = (255, 0, 0)
