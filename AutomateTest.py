import transportionCipher, transpotionHack, random, importlib

def main():
    importlib.reload(transportionCipher)
    importlib.reload(transpotionHack)
    for i in range(20):
        orginal = createString()
    #orginal = "Common Sence is not so Common"
    

        key = random.randint(3,10)
        #Use copy.deepcopy() to create another list with out having the same refrence 
    
    
        enc = transportionCipher.encrypt(key, orginal)
    
        dec = transpotionHack.decipher(key, enc)
        if( dec == orginal):
            print("success")
        else:
            print("orginal", orginal, "encrypted", enc, "decrypted", dec)

def createString():
    length = random.randint(10,30)
    char = "abcdefghijklmnopqrstuvwxyz .!?"
    return char * length
    



if(__name__ == "__main__"):
    main()



