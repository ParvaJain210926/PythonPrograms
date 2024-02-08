def change(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)

sentence = input("Enter a sentence: ")
old= input("Enter the word to replace: ")
new = input("Enter the new word: ")
print("Modified sentence:", change(sentence, old, new))
