
import CeaserCipher, MultiplcationCipher, cryptoMath, sys
ind = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?."

def encrypt(message, a,b):
    o = ""
    for char in message:
        if(char in ind):
            o += ind[ind.find(char) * a + b % len(ind)]
        o += char



def allclear(a,b,message,mode):
    if(a == 1 and mode == 'e'):
        print('find a stronger A')
        sys.exit

    if(a == 0 and mode == 'e'):
        print('find a stronger A')
        sys.exit

    



if ( __name__ == "__main__"):
    pass