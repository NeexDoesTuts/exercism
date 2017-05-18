def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet_s = "abcdefghijklmnopqrstuvwxyz"
    alphabet_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for char in sentence:
        if char in alphabet_s and char in alphabet_l:
            alphabet_l.remove(char)

    if len(alphabet_l) == 0:
        return True
    return False
