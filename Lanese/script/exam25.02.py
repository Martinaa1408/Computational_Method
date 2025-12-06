#Write a python program that accepts two command-line parameters: a filename and an option (MIN/MAX/BOTH). The specified file contain space separated
#integers.
#This program should process each line of the file and:
#If the option is MIN or BOTH, calculate the local minima and write them to the min.txt file.
#If the option is MAX or BOTH, calculate the local minima and write them to the max.txt file.
#A local minim is a number that is strictly less than both the preceding and following numbers. If a number is at the begining or end of the line,
#it is considereded a local minimum if it is less than the adjacent number (if present). A local maximum is defined symmetrically, with the condition of
#being strictly greater.

#Example:
#Input file:
# 1 2 1 1 5 3
# 4 2 6 1 4 5 9 1

#Output file min.txt:
#1 3
#2 1 1
#Output file max.txt:
#2 5
#4 6 9
from sys import argv

def main(input_file, output_min, output_max, option):

    for raw_line in input_file:
        raw_line = raw_line.strip()

        if raw_line == "":
            if option == "MIN" or option == "BOTH":
                output_min.write("\n")
            if option == "MAX" or option == "BOTH":
                output_max.write("\n")
            continue

        parts = raw_line.split()
        nums = []

        for p in parts:
            nums.append(int(p))

        min_list = []
        max_list = []

        # -------- FIRST ELEMENT --------
        if nums[0] < nums[1]:
            min_list.append(nums[0])
        elif nums[0] > nums[1]:
            max_list.append(nums[0])

        # -------- CENTRAL ELEMENTS --------
        for pos in range(1, len(nums) - 1):
            if nums[pos] < nums[pos - 1] and nums[pos] < nums[pos + 1]:
                min_list.append(nums[pos])
            elif nums[pos] > nums[pos - 1] and nums[pos] > nums[pos + 1]:
                max_list.append(nums[pos])

        # -------- LAST ELEMENT --------
        if nums[-1] < nums[-2]:
            min_list.append(nums[-1])
        elif nums[-1] > nums[-2]:
            max_list.append(nums[-1])

        # Convert numbers to string
        min_line = ""
        max_line = ""

        for x in min_list:
            min_line += str(x) + " "

        for x in max_list:
            max_line += str(x) + " "

        min_line = min_line.strip()
        max_line = max_line.strip()

        # -------- OPTION HANDLING --------
        if option == "MIN":
            output_min.write(min_line + "\n")

        elif option == "MAX":
            output_max.write(max_line + "\n")

        else:   # BOTH
            output_min.write(min_line + "\n")
            output_max.write(max_line + "\n")


def file():
    """Gestisce apertura file e errori."""
    try:
        option = input("Enter MIN, MAX, BOTH: ").strip().upper()

        input_file = open(argv[1], "r")
        output_min = open("min.txt", "w")
        output_max = open("max.txt", "w")

        main(input_file, output_min, output_max, option)

        input_file.close()
        output_min.close()
        output_max.close()

    except FileNotFoundError:
        print("File not found.")
    except IndexError:
        print("Usage: python script.py <input_file>")

file()
