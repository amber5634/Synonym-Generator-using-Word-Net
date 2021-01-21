import nltk 
from nltk.corpus import wordnet

class Keyword:
    
    def synonymn_generator(self):
        synonyms = [] 
        antonyms = [] 
        word = input("enter the word : ")
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas(): 
                synonyms.append(l.name()) 
                if l.antonyms(): 
                    antonyms.append(l.antonyms()[0].name())
        print(set(synonyms))
        print(set(antonyms))

p1 = Keyword()

p1.synonymn_generator()