if __name__ == '__main__':
    
    # Take input for the dimensions of the 3D grid and the sum to exclude
    x = int(input("Enter number"))  # Number of rows (range for i)
    y = int(input("Enter number"))  # Number of columns (range for j)
    z = int(input("Enter number"))  # Number of depth levels (range for k)
    n = int(input("Enter number"))  # The sum to exclude combinations where i + j + k == n
    
    # List comprehension to generate all combinations [i, j, k] where:
    #  - i is from 0 to x
    #  - j is from 0 to y
    #  - k is from 0 to z
    # The combination is included only if the sum of i + j + k is not equal to n
    result = [ [i, j, k] 
               for i in range(x + 1)  # Loop through all possible values for i
               for j in range(y + 1)  # Loop through all possible values for j
               for k in range(z + 1)  # Loop through all possible values for k
               if i + j + k != n ]    # Exclude combinations where i + j + k == n
    
    # Output the result, which is a list of lists where each sublist is [i, j, k]
    print(result)