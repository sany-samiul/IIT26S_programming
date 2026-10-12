print("Program starting.")
print()

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print()
print("Starting while-loop:")

number = start

while number <= stop:
    if number == stop:
        print(number)
    else:
        print(number, end=" ")
    number += 1

print()
print("Program ending.")