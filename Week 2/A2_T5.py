print("Program starting.")
print()

Word = input("Insert a closed compound word: ")

Length = len(Word)
First_character = Word[0]
Reversed_word = Word[::-1]
Last_character = Word[-1]

print(f"The word you inserted is '{Word}' and in reverse it is '{Reversed_word}'.")
print(f"The inserted word length is {Length}")
print(f"Last character is '{Last_character}'")
print()

print("Take substring from the inserted word by inserting...")
Starting_point = int(input("1) Starting point: "))
Ending_point = int(input("2) Ending point: "))
Step_size = int(input("3) Step size: "))
print()

Substring = Word[Starting_point:Ending_point:Step_size]

print(f"\nThe word '{Word}' sliced to the defined substring is '{Substring}'.")
print("Program ending.")