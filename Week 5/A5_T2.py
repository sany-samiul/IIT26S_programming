def frameWord(PWord):
    frame = "*" * (len(PWord) + 4)

    print(frame)
    print("* " + PWord + " *")
    print(frame)
    print()
    return None


def main():
    print("Program starting.")
    word = input("Insert word: ")
    print()
    frameWord(word)
    print("Program ending.")
    return None


main()