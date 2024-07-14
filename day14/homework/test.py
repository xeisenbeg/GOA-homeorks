#1
# for i in range(1, 21):
#     print(i)


#2
# for i in range(11):
#     print(i)

#3

# for i in range(100):
#     if i % 2 == 0:
#         print(i, "even")
#     else:
#         print(i,"odd")


# #4
# # num = int(input('enter a number: '))
# # sum = 0
# # for i in range(5):
#     sum += i
# #     print(sum)


#5

# for i in range(50):
#     if i % 5 == 0:
#         print(i)





#6

# i = 0
# while i < 20:
#     if i % 2 == 0:
#         print(i)

#     i += 1



# 2)Check if a given string entered by the user is a palindrome.

str = input("Enter your word: ").lower()

print(str == str[::-1])


# 4)Write a program that calculates and prints the square of numbers from 1 to 10 using a while loop.

i = 0
sum = 0

while i < 10:
    sum += i ** 2
    i += 1

print(sum)



# 2)Write a program that uses a while loop to print numbers from 10 down to 1.

i = 10

while i > 0:
    print(i)
    i -= 1


# 5)Write a program that prints numbers from 10 to 1 in reverse order using a for loop.

for i in range(10, 1, -1):
    print(i)



# 4)Print numbers divisible by both 3 and 5 from 1 to 100 inclusive.

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 3)Write a program that calculates and prints the sum of squares of numbers from 1 to 5 using a for loop.

sum = 0

for i in range(1, 5):
    sum += i ** 2

print(sum)



# 2)Print the squares of numbers from 1 to 15.

for i in range(1, 15):
    print(i ** 2)



# 4) Write a while loop that processes a list of numbers, doubling each number, and prints the new list.

i = 0
list1 = [1, 5, 20, 12, 17]
result = []

while i < len(list1):
    result.append(list1[i] * 2)
    i += 1

print(result)



# 3) Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.

guess = 0

while guess != 7:
    guess = int(input("Enter your guess: "))




# 2) calculate the sum of numbers from 1 to 10.

i = 0
sum = 0

while i < 10:
    sum += i
    i += 1

print(sum)




# 1) Print even numbers up to 20.

i = 0

while i < 20:
    if i % 2 == 0:
        print(i)
    i += 1
# 5) Write an algorithm that prints multiples of 5 (numbers divisible by 5) from 1 to 50 inclusive

for i in range(1, 50):
    if i % 5 == 0:
        print(i)


# 4) Enter a number to the user and then using a for loop output the sum of all the numbers up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).

num = int(input("Enter your number: "))
sum = 0

for i in range(num):
    sum += i

print(sum)



# 3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive.

for i in range(100):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")


 