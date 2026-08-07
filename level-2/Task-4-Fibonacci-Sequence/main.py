# Fibonacci Sequence Program
terms = int(input("Enter the number of terms: "))
first = 0
second = 1
print("Fibonacci Sequence:")
if terms <= 0:
    print("Please enter a positive number.")

elif terms == 1:
    print(first)

else:
    print(first)
    print(second)

    for i in range(2, terms):
        next_number = first + second
        print(next_number)
        first = second
        second = next_number