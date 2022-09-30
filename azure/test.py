emojiDict = {
    'a': 5633855357,
    'b': 5716455356,
    'c': 5716355356,
    'd': 5632955357,
    'e': 5634455357,
    'f': 5635155357,
    'g': 5672255358,
    'h': 5633455357,
    'i': 5661355357
}

try:
    for letter in emojiDict.values():
        print(letter)

except OverflowError as e:
    print(letter, chr(letter))