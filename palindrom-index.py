# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    if isPalindrome(s):
        return -1
    
    sReversed = s[::-1]
    for i in range(len(s)):
        if s[i] != sReversed[i]:
            testString = s[:i] + "" + s[i + 1:]
            if isPalindrome(testString):
                return i
            return len(s) - i - 1
        

def isPalindrome(s):
    return s == s[::-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()