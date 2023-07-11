## Concept Questions

**2.1**

 `def is_isogram(word)`

    word = word.lower()
    letter_count = {}

    for letter in word:
        if letter.isalpha():
            if letter in letter_count:
                return False
            letter_count[letter] = 1

    return True
print(is_isogram("isogram"))  # True

print(is_isogram("uncopyrightable"))  # True

print(is_isogram("ambidextrously"))  # False (letter 'o' is repeated)

