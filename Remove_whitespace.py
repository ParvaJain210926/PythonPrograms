def rem(sentence):
    return sentence.replace(" ", "")

sentence = input("Enter a sentence: ")
print("Sentence without whitespace:", rem(sentence))
