def palindromecheck(a):
    rev= a[::-1]
    if a==rev:
        print("palindrome")
    else:
        print("not palindrome")
        
palindromecheck("madam")
palindromecheck("cat")