def encrypt(message, key):
    ind = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?."
    out = ""
    for char in message:
        i = ind.find(char)
        i *= key
        i %= len(ind)
        out += ind[i]
    return out

if (__name__ == "__main__"):
    print(encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?.", 17))
