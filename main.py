def palindrome_(word):
    return word == word[::-1]


word = input()
print(palindrome_(word))
