# Program to demonstrate exponentiation in Python using ** and pow()

if __name__ == '__main__':
    a = int(input("Enter value for a: ")) 
    b = int(input("Enter value for b (power of a): ")) 
    c = int(input("Enter value for c: ")) 
    d = int(input("Enter value for d (power of c): ")) 
    
    # Using exponentiation operator (**)
    print(a ** b + c ** d)
    
    # Using built-in pow() function
    print(pow(a, b) + pow(c, d))
