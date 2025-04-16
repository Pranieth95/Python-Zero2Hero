# Program to print the square of all non-negative integers less than a given number n

if __name__ == '__main__':
    n = int(input("Enter a number: "))  # Read an integer from standard input

    for i in range(n):  # Loop through all integers from 0 to n-1
        print(i * i)    # Print the square of each number
