def askDimension(PPrompt: str) -> float:
    value = float(input("Insert {}: ".format(PPrompt)))
    return value


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    area = PWidth * PHeight
    return area


def main():
    print("Program starting.")

    width = askDimension("width")
    height = askDimension("height")

    area = calcRectangleArea(width, height)

    print()
    print("Area is {}²".format(area))
    print("Program ending.")
    return None


main()