
SEPARATOR = ";"


def readValues(filename: str) -> str:
    values: str = ""

    file = open(filename, "r")

    for line in file:
        if values != "":
            values += SEPARATOR

        values += line.strip()

    file.close()

    return values


def analyseNumbers(values: str) -> str:
    numbers = values.split(SEPARATOR)

    count: int = 0
    total: int = 0
    greatest: int = 0

    for number in numbers:
        value: int = int(number)

        count += 1
        total += value

        if value > greatest:
            greatest = value

    average: float = total / count

    results: str = str(count) + SEPARATOR
    results += str(total) + SEPARATOR
    results += str(greatest) + SEPARATOR
    results += "{:.2f}".format(average)

    return results


def displayResults(filename: str, results: str) -> None:
    print("#### Number analysis - START ####")
    print('File "' + filename + '" results:')
    print("Count;Sum;Greatest;Average")
    print(results)
    print()
    print("#### Number analysis - END ####")


def main() -> None:
    print("Program starting.")

    filename: str = input("Insert filename: ")

    values: str = readValues(filename)
    results: str = analyseNumbers(values)

    displayResults(filename, results)

    print("Program ending.")


main()
