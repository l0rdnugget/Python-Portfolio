print("Hi! Welcome to the Student Grade Calculator")
name = input("Please enter your name: ")
assignment1 = input("Enter the name of Assignment 1: ")
score1 = float(input(f"Enter the score for {assignment1}: "))
assignment2 = input("Enter the name of Assignment 2: ")
score2 = float(input(f"Enter the score for {assignment2}: "))
assignment3 = input("Enter the name of Assignment 3: ")
score3 = float(input(f"Enter the score for {assignment3}: "))
total = score1 + score2 + score3
average = total / 3
print(f"\n-- Grade Report for {name} ---")
print(f"{assignment1}: {score1}")
print(f"{assignment2}: {score2}")
print(f"{assignment3}: {score3}")
print(f"Total Score: {total}")
print(f"Average Score: {average:.2f}")

input("Press Enter to exit :) ...")
