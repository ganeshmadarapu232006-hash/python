def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

result = is_palindrome(121)

if result:
    print("Palindrome")
else:
    print("Not Palindrome")