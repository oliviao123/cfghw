# 2.1
def is_isogram(word):
    # Convert the input string to lowercase to make the comparison case-insensitive
    word = word.lower()

    # Check whether each character in the word appears only once
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            print(f"Found repeated character {word[i]} in {word}")
            return False

    return True
