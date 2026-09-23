# Calculator - Python

This is one of my beginner Python projects.

I created this program while learning while loops and conditional statements in Python.
I wanted to practice these concepts in a simple and practical program, so I created a basic calculator.

## What This Program Does

- Takes two numbers from the user.
- Provides four operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Uses a while loop to keep the calculator running.
- Checks for division by zero.
- Checks whether the user entered a valid menu choice.
- Asks the user whether they want to calculate again.

## Python Concepts I Practiced

- input()
- int()
- while loop
- if / elif / else
- Arithmetic operators
- User input validation
- .lower()
- break
- continue
- exit()

## Example Output

Enter Number 1 : 10
Enter Number 2 : 5

1. Addition
2. Subtraction
3. Multiplication
4. Division

Select your choice to perform : 1
Addition is : 15

Want To Calculate Again? (yes / no): yes

Enter Number 1 : 20
Enter Number 2 : 4

1. Addition
2. Subtraction
3. Multiplication
4. Division

Select your choice to perform : 3
Multiplication is : 80

Want To Calculate Again? (yes / no): yes

Enter Number 1 : 20
Enter Number 2 : 5

1. Addition
2. Subtraction
3. Multiplication
4. Division

Select your choice to perform : 4
Division is : 4.0

Want To Calculate Again? (yes / no): no
CALCULATION STOPPED...!

## Error Handling

The program also handles division by zero.

Example:

Enter Number 1 : 10
Enter Number 2 : 0

Select your choice to perform : 4

WRONG , Can't divide by 0

The program also handles an invalid menu choice.

Example:

Select your choice to perform : 7

ERROR ! Wrong choice is entered , Please enter from 1 - 4

The program also checks whether the user enters yes or no when asked to continue.

Example:

Want To Calculate Again? (yes / no): maybe

ERROR: Please enter only yes or no

## About Me

I am a beginner in Python and currently learning programming step by step. 
I am creating small projects to practice the concepts I learn and uploading them to GitHub to track my progress.

This calculator is one of my first Python projects and is part of my journey of learning Python.
