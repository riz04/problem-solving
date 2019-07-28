def is_palindrome(string):
    for i in string:
        for j in string[::-1]:
            if i==j:
                return True
            return False

print(is_palindrome("woweee"))
