def reverse(sentence):
    # All in One line
    return ' '.join(word[::-1] for word in sentence.split(" "))


sentence = input("Votre phrase :")
print(reverse(sentence))
