# Example Practice:
# Given this list of fruits:
# fruits = ["apple", "banana", "cherry", "date"]

# print(len(fruits))


# Challenge:

# Use a for loop to print each fruit on a new line.
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# for fruit in fruits:
#     print(fruit)
# i just worked with loops

# Given a list of school subjects:
# subjects = ["Math", "Science", "History", "Art"]
# for subject in subjects:
#     if subject == "History":
#         break
#     print(subject)

# for subject in subjects:
#     if subject == "History":
#         continue
#     print(subject)

# for index in range(len(subjects)):
#     print("Subject " + str(index) + ": " + subject[index])
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"


# Given:
# numbers = [5, 10, 15, 20]

# total = 0
# for number in numbers:
#     total += number

# print(total)


# Challenge:
# Use a for loop to add all the numbers and print the total.
total = 0
numbers = (5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)

for total in numbers:
    total = total + numbers

print(total)