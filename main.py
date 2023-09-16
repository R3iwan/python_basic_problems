# Problem 1: Hello World!

print("Hello World!")

# Problem 2: Sum of Two Numbers!

print("Give two numbers: ")
a = int(input())
b = int(input())
c = int()
c = a + b
print("The Value of Two numbers is: ", c)

# Problem 3: Even or Odd

print("Give a number to check whether it's even or odd!")
num = int(input())
if num % 2 == 0:
    print("The Value is Even")
else:
    print("The Value is Odd")

# Problem 4: Calculator

print("Enter Your Numbers:")
num1 = int(input())
num2 = int(input())

print("Choose Operation: \n1)Add \n2)Subtract \n3)Multiply \n4)Divide")
choice = int(input())

match choice:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        print(num1 / num2)
    case _:
        print("Unavailable number.")

import random

 # Problem 5: Factorial

def fact(num1):
    if num1 == 1:
        return 1
    else:
        return num1 * fact(num1-1)

num1 = int(input("Enter Your Number: "))
result = fact(num1)
print(result)

# Problem 6: Guess the number

def guesser():
    return int(input("Enter a number:"))

rand = random.randint(1, 100)

def main():
    num1 = guesser()
    if num1 > rand:
        print("Too High, try again")
        main()
    elif num1 < rand:
        print("Too Low, try again")
        main()
    else:
        print("You are correct!")

if __name__ == "__main__":
    main()

# Problem 7: Palindrome Checker

str1 = input("Enter a String:")
lastChar = len(str1) - 1
strChar = 0
a = str1[strChar]
b = str1[lastChar]

is_palindrome = True

while strChar < lastChar:
    if a != b:
        is_palindrome = False
        break
    strChar = strChar + 1
    lastChar = lastChar - 1
    a = str1[strChar]
    b = str1[lastChar]

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string isn't a palindrome.")


# Problem 8 Fibonacci Sequence

def fib_seq(num1):
    if num1 == 0:
        return 0
    return num1 + fib_seq(num1 - 1)

num1 = int(input("Enter a Number to it's sequence in Fibonacci: "))
result = fib_seq(num1)
print(result)


# Problem 9: Reverse String

str1 = input("Enter a String to Reverse it: ")
result = ""

lastChar = len(str1) - 1

while lastChar >= 0:
    result += str1[lastChar]
    lastChar -= 1

print(result)

# Problem 10: List Input

my_list = []

while True:
    user_input = input("Enter a text: ")
    if user_input.lower() == 'done':
        break
    my_list.append(user_input)

print("Your list: ")
print(my_list)
