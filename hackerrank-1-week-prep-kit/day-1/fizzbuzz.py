# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        print(fizzBuzzOutput(i))
        

def fizzBuzzOutput(n):
    output = ""
        
    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    
    if len(output) == 0:
        return n
        
    return output
    
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)