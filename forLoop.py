# Program to demonstrate basic for loops in Python

if __name__ == '__main__':
    n = int(input("Enter a number: "))  # Read an integer from standard input

    for i in range(n):  # Loop through all integers from 0 to n-1
        print(i * i)    # Print the square of each number


    
    for i in range (1, n + 1): # Loop through all integers from 1 to n
        print(i, end="") #Print in a single line instead of a new line for each result using end=""
        