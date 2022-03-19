


sentence = input(" write a sentence:")
word = input(" write a word:")

def reverse(sentence,word):
    sentence=sentence.lower()
    word=word.lower()

    X=0
    Y=0
    if isinstance(word,str):
        if word in sentence:
            while X<len(word):
                if word[X]==sentence[Y]:
                    return sentence.replace(word,word[::-1])
                    X=X+1
                    Y=Y+1
                else:
                    Y=Y+1
        else:
            return "no match word found"
    else:
        return "invalid input" 
            
    
print(reverse(sentence,word))
    
    
    
   