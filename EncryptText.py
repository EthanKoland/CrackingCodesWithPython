import transpotionHack, transportionCipher, os, sys

def main():
    filename = "frankenstein.txt"
    key = 10

    with open(filename, "r") as text:
        s = text.read()

    enc = transportionCipher.encrypt(key, s)
    if(os.path.exists("frankensteinEcrypted.txt")):
        input("THe file will be over written")
        
    with open("frankensteinEcrypted.txt", "w") as output:
        output.write(enc)
    
    dec = transpotionHack.decipher(10, enc)
    
    with open("FrankCheck.txt", "w") as check:
        check.write(dec)
    

    print(enc)

if (__name__ == "__main__"):
    main()