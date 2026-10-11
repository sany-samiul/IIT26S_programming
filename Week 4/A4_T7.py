print("Program starting.")
print()
print("Check multiplicative persistence.")

number = int(input("Insert an integer: "))

steps = 0

while number >= 10:
    digits = [int(digit) for digit in str(number)]

    print(" * ".join(str(digit) for digit in digits), end="")

    result = 1
    for digit in digits:
        result *= digit

    print(" = " + str(result))

    number = result
    steps += 1

print("No more steps.")
print()
print("This program took " + str(steps) + " step(s)")
print()
print("Program ending.")