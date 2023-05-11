# THIS PROGRAM IS TO FIND THE FACTORS OF A GIVEN NUMBER
num = int(input("Enter the number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
