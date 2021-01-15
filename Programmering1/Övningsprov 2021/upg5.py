print("Skriv en mening som du vill räkna orden av.")
sentence = input("Mening: ")

sentence_words = sentence.split(" ")
#print(sentence_words) #Debug
sentence_words = list(filter(None, sentence_words)) #Detta låter oss ta bort extra mellanslag
#print(sentence_words) #Debug

print("Antal ord: ", len(sentence_words))
