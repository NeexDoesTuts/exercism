def is_isogram(word):
    word_copy = word.lower()
    word = word.lower()

    for char in word:
        word_copy = word_copy[1:]
        if char in word_copy and char.lower() in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True
