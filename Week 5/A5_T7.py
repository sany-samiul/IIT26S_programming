
DELIMITER = ","


def collectWords():
    words = ""

    while True:
        word = input("Insert word(empty stops): ")

        if word == "":
            break

        if words == "":
            words = word
        else:
            words += DELIMITER + word

    return words


def analyseWords(words):
    if words == "":
        wordList = []
    else:
        wordList = words.split(DELIMITER)

    amountOfWords = len(wordList)

    characters = 0

    for word in wordList:
        characters += len(word)

    if amountOfWords > 0:
        avg = characters / amountOfWords
    else:
        avg = 0

    print("- {} Words".format(amountOfWords))
    print("- {} Characters".format(characters))
    print("- {:.2f} Average word length".format(avg))


def main():
    print("Program starting.")

    words = collectWords()
    analyseWords(words)

    print("Program ending.")


main()

