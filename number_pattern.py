'''
Print the number pattern 

1
12
123
1234
12345

'''

def patternNumber(n):
    # Outer loop for the number of lines
    for i in range(1, n+1):
        # Inner loop to print numbers in each line
        for j in range(1, i+1):
            print(j, end="")  # Print the current number on the same line
        print()  # Print a newline after each line

if __name__ == "__main__":
    n = int(input("Enter the number of lines: "))
    patternNumber(n)
