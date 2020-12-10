
import os
    
def isEnglish(s):
    if(not os.path.exists("dictionary.txt")):
        print("please install a Dicotary that is named dicitionary.txt")
    else:
        with open("dictionary.txt", "r") as dicText:
            dic = dicText.read().split()

        s = s.split()
        
        if(len(s) == 0):
            return False
        
        c = [0]
        print(s)

        for i in range(len(s)):
            s[i] = lettersOnly(s[i], c)
        

        count = 0

        for word in s:
            if(word.upper() in dic):
                count += 1
            else:
                print(word)
        return (count/float(len(s)) > .20 and c[0]/float(len(s)) > .85)

def lettersOnly(s, c):
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    arr = ""
    for char in s:
        if(char.upper() in l):
            arr += char
            c[0] += 1
    return(arr)

if (__name__ == "__main__"):
    isEnglish("Is this sentence English?")
    