print("Program starting.")
print()

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

valid = True

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    valid = False

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    valid = False

if valid:
    print()
    print("First loop - inspection with break:")

    first = True

    for number in range(start, stop + 1):
        if number == inspection:
            break

        if not first:
            print(" ", end="")
        print(number, end="")
        first = False

    print()
    print("Second loop - inspection with continue:")

    first = True

    for number in range(start, stop + 1):
        if number == inspection:
            continue

        if not first:
            print(" ", end="")
        print(number, end="")
        first = False

    print()

print()
print("Program ending.")