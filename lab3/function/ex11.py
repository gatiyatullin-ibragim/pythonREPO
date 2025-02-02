def is_polindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    return False

slovo = str(input("введите строку: "))
print(is_polindrome(slovo))
