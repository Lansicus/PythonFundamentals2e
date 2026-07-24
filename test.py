import statistics as stat
from decimal import Decimal
from typing import List, Optional
import random as r



'''Casino Game called Craps'''
points = 0
dice_roll = r.randint(1,6) + r.randint(1,6)

print(f'Roll the dice for a chance to win')
input()
if dice_roll in (7, 11):
    print(f"You rolled {dice_roll}")
    print(f"You win with {dice_roll} points!\n")
elif dice_roll in (2, 3, 12):
    print(f"You lost with a {dice_roll}.\nBetter luck next time!\n")
else:
    print(f"You rolled a {dice_roll}.\nRoll {dice_roll} again to win! ")
    input()
    while True:
        new_roll = r.randint(1,6) + r.randint(1,6)
        if new_roll == 7:
            print(f"You lost with a {dice_roll}.\nBetter luck next time!\n")
            break
        else:
            print(f'You got {new_roll}\n')
            input()
            continue
            


# ------------------------------------------------------------------------------------------------------------

# Hs = 0
# Ts = 0
# for i in range(20):
#     if random.randint(1,2) == 1:
#         Hs += 1
#     else:
#         Ts += 1
# print(f"Heads:{Hs}\nTails:{Ts}")
# ------------------------------------------------------------------------------------------------------------

# random.seed(32)
# for roll in range(10):
#     print(random.randint(1,6), end=' ')
# ------------------------------------------------------------------------------------------------------------

# values = [47, 95, 88, 73, 88, 84, 84]
# values2 = [54, 97, 62, 97, 31, 46, 57]
# values_list = [values, values2]

# def stats_function(*args) -> None:
#     groups = []

#     for arg in args:
#         # Case 1: arg is a list of numbers
#         if all(isinstance(x, (int, float)) for x in arg):
#             groups.append(arg)

#         # Case 2: arg is a list of lists
#         elif all(isinstance(x, list) for x in arg):
#             groups.extend(arg)

#         # Case 3: mixed or invalid input
#         else:
#             raise TypeError("Each argument must be a list of numbers or a list of lists")
#     for idx, x in enumerate(groups, start=1):
#         print(f"Group {idx}:\nmean:{stat.mean(x):.2f}, mode:{stat.mode(x)}, multimode:{stat.multimode(x)}, median:{stat.median(x)}")
# # ---------------

# def temp_average() -> List[List[float]]:
#     """
#     Interactively collect one or more lists of temperatures.
#     Returns a list of lists. If the user never enters any temperatures,
#     returns an empty list.
#     """
#     def collect_one_list() -> List[float]:
#         entries: List[float] = []
#         entry_num = 1
#         print("Enter a number from -212 to 212 (enter blank to finish this list).")
#         while True:
#             s = input(f"Entry #{entry_num}: ").strip()
#             if s == "":
#                 # blank finishes this list
#                 break
#             try:
#                 val = float(s)
#             except ValueError:
#                 print("Invalid input. Enter a number between -212 and 212 (or blank to finish).")
#                 continue

#             if -212 <= val <= 212:
#                 entries.append(val)
#                 entry_num += 1
#             else:
#                 print("Out of range. Enter a number from -212 to 212 (or blank to finish).")
#         return entries

#     all_lists: List[List[float]] = []

#     # First list
#     first = collect_one_list()
#     if first:
#         all_lists.append(first)
#     else:
#         # No entries in first list: ask whether to try again or quit
#         retry = input("No temperatures entered. Try again? (Y/N): ").strip().upper()
#         if retry == "Y":
#             first = collect_one_list()
#             if first:
#                 all_lists.append(first)
#             else:
#                 print("No temperatures entered. Exiting.")
#                 return []  # consistent empty result
#         else:
#             print("Goodbye.")
#             return []

#     # Optionally collect more lists
#     while True:
#         more = input("Any more lists? (Y/N): ").strip().upper()
#         if more == "Y":
#             nxt = collect_one_list()
#             if nxt:
#                 all_lists.append(nxt)
#             else:
#                 print("No temperatures entered for this list; not added.")
#         else:
#             break

#     return all_lists
# ------------------------------------------------------------------------------------------------------------

# tax = .0625
# bill = 37.45
# print(f"{bill + bill * tax:.2f}")
# print(bill + bill * tax)

# bill_total = Decimal('37.45') * Decimal(1.0625)
# print(f"{bill_total:.2f}")
# print(bill_total)
# ------------------------------------------------------------------------------------------------------------

# x = 0
# for _ in range(2, 101, 2):
#     x += _
# print(x)
# ------------------------------------------------------------------------------------------------------------

# for _ in range(99, -1, -11 + 7):
#     print(_, end=" ")
# ------------------------------------------------------------------------------------------------------------

# def prompt_selection() -> None:
#     attempts = 3

#     while attempts > 0:
#         selection = input("Enter: A, B, or C: ").strip().upper()

#         match selection:
#             case 'A':
#                 print("You selected option A.")
#                 return
#             case 'B':
#                 print("You selected option B.")
#                 return
#             case 'C':
#                 print("You selected option C.")
#                 return
#             case _:
#                 attempts -= 1
#                 if attempts > 1:
#                     print(f"Invalid input. You have {attempts} more tries.")
#                 elif attempts == 1:
#                     print("Invalid input. Last chance.")
#                 else:
#                     print("No more attempts. Rerun the program.")
#                     return
# ------------------------------------------------------------------------------------------------------------

# def product_counter() -> None:
#     product = 7
#     while product < 1000:
#         product *= 7
#     print(f"The product is: {product}")
    
# ------------------------------------------------------------------------------------------------------------

# def grade_averager() -> None:
#     tests_submitted = int(input("How many tests have been submitted? "))
#     grades = []
#     for _ in range(tests_submitted):
#         grades.append(int(input("Enter Score: ")))
#     average = sum(grades) / len(grades)
#     print(f"The average score is: {average:.2f}")
# ------------------------------------------------------------------------------------------------------------

# def grade_average() -> None:
#     """Class average program with sentinel-controlled iteration."""
#     number_of_tests = 0
#     print("Enter -1 at any time to exit the function.")
#     while True:
#         number_of_tests = input("How many tests submitted? ").strip()
#         if number_of_tests == "-1":
#             print("Returning...")
#             return
#         elif not number_of_tests.isdigit():
#             print("ANSWER THE QUESTION LABOWSKI")
#         elif 1 <= int(number_of_tests) <= 100:
#             print(f"You have {number_of_tests} tests to average.")
#             number_of_tests = int(number_of_tests)
#             break
#         else:
#             print("Must enter a number from 1 to 100.")

#     grades_list = []
#     for i in range(number_of_tests):
#         while True:
#             grade = input(f"Enter grade {i + 1}: ").strip()
#             if grade == "-1":
#                 print("Returning...")
#                 return
#             if grade.isdigit():
#                 grade = int(grade)
#                 if 1 <= grade <= 100:
#                     grades_list.append(grade)
#                     break
#                 print("Must enter a number from 1 to 100.")
#             else:
#                 print("Must enter a number from 1 to 100.")

#     average_grade = sum(grades_list) / len(grades_list)
#     print(f"The class average is: {int(average_grade)}")
# ------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
#     # prompt_selection()
#     # product_counter()
#     # grade_averager()
#     grade_average()
    # temp_average()
    # stats_function()
    pass
            