
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def writeFile(Filename: str, Content: str) -> None:
    file = open(Filename, "w", encoding="UTF-8")
    file.write(Content)
    file.close()


def askRows() -> str:
    print("Collecting plain text rows for ciphering.")
    rows = []

    while True:
        row = input("Insert row(empty stops): ")

        if row == "":
            break

        rows.append(row)

    return "\n".join(rows)


def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    if Character not in Alphabets:
        return Character

    position = Alphabets.index(Character)
    new_position = (position + Shift) % len(Alphabets)

    return Alphabets[new_position]


def rot13(Content: str) -> str:
    ciphered_text = ""

    for character in Content:
        if character in LOWER_ALPHABETS:
            ciphered_text += shiftCharacter(character, LOWER_ALPHABETS)
        elif character in UPPER_ALPHABETS:
            ciphered_text += shiftCharacter(character, UPPER_ALPHABETS)
        else:
            ciphered_text += character

    return ciphered_text


def main() -> None:
    print("Program starting.")
    print()

    plain_text = askRows()
    ciphered_text = rot13(plain_text)

    print()
    print("#### Ciphered text ####")
    print(ciphered_text)
    print()
    print("#### Ciphered text ####")

    filename = input("Insert filename to save: ")

    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        writeFile(filename, ciphered_text)
        print("Ciphered text saved!")

    print("Program ending.")


if __name__ == "__main__":
    main()

