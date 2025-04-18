def is_leap(year):
    leap = False  # Assume it's not a leap year initially
    
    # Check if the year is divisible by 4 and (not divisible by 100 or divisible by 400)
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        leap = True  # Set to True if it's a leap year
    
    return leap  # Return the result

year = int(input())  # Get the year from user input
print(is_leap(year))  # Print whether it's a leap year or not
