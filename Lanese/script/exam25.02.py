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
def main(input_file, outputmin_file, outputmax_file, option):
  '''the function main take teh file and option as arguments, and analyze each case in order to collect the list max and min'''
  for line in input_file:
    line=line.split()
    max_list=[]
    min_list=[]
    #first element
    if int(line[0])>int(line[1]):
      max_list.append(line[0])
    elif int(line[0])<int(line[1]):
      min_list.append(line[0])
    #central elements
    for pos in range(1,len(line)-1)):
      if int(line[pos])>int(line[pos-1]) and int(line[pos])>int(line[pos+1]):
        max_list.append(line[pos])
      elif int(line[pos])<int(line[pos-1]) and int(line[pos])<int(line[pos+1]):
        min_list.append(line[pos])
    #last element
    if int(line[-1])>int(line[-2]):
      max_list.append(line[-1])
    elif int(line[-1])<int(line[-2]):
      min_list.append(line[-1])

    max_list=''.join(max_list)
    min_list=''.join(min_list)

    #option case
    if option=='MIN':
      outputmin_file.write(str(min_list)+'\n')
    elif option=='MAX':
      outputmax_file.write(str(max_list)+'\n')
    else option=='BOTH':
      outputmin_file.write(str(min_list)+'\n')
      outputmax_file.write(str(max_list)+'\n')
    
def file():
''' this function analyze the errors and explain the file'''
try:
  option=input('Enter MAX,MIN,BOTH:')
  input_file=open(argv[1],'r')
  output_min=open(argv[2],'w')
  output_max=open(argv[3],'w')
  main(input_file,output_min,output_max,option)
except FileNotFoundError:
  print('File not found')
except IndexError:
  print('Not enough arguments')
  
file()
    
### in the console you write python3 exam25.02.py input_file_name outputmin_file_name outputmax_file_name
### insert an option: MIN/MAX/BOTH
### the result print on the file

      
