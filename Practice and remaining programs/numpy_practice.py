def palindrome(x):
    chars = ""
    for i in x:
        if i.isalnum():
            chars += i
    if chars == chars[::-1]:
        print(chars)
        return True
    return False


name = input().lower()
print(palindrome(name))
