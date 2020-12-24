import transpotionHack, transportionCipher, isEnglish, sys,importlib

def main():
    importlib.reload(transpotionHack)
    message = "Cntooc nmesm ooi nsC  oSnmeom"
    print(transpotionHack.decipher(9, message))
    for i in range(2, len(message)):
        temp = transpotionHack.decipher(i, message)
        print("Using the key %d the message became %s" % (i, temp))
        if(isEnglish.isEnglish(temp)):

            cont = input("if this is not a valid message type y")  
            if(cont == "y"):
                sys.exit()
    


if ( __name__ == "__main__") :
    main() 