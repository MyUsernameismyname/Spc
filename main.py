def palindrome_(slovo):
    return slovo == slovo[::-1]


word = input()
print(palindrome_(word))
