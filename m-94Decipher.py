import os, tkinter as tk


def main():

    

    window = tk.Tk()
    

    window.rowconfigure([0,1], minsize = 100, weight=1)
    window.columnconfigure([0,1,2], minsize=25, weight=1)

    exitText = tk.Label(master=window, text="hello", background="blue")
    exitText.grid(row=0, column=0, columnspan=3, sticky="nsew")

    infoText = tk.Label(master=window, text = "Enter a encrypted Text")
    infoText.grid(column=0, row=1, sticky="nsew")

    encryptEntry = tk.Entry(master=window)
    encryptEntry.grid(row=1, column=1,  sticky="nsew")

    encryptButton = tk.Button(master=window, text="encrypt Message", command = lambda: decrypt(encryptEntry.get(), exitText) )
    encryptButton.grid(row=1, column=2, sticky="NSEW")
        
        

def decrypt(sdfghjn, exitText):
    
    encryptedText = sdfghjn

    print(encryptedText)

    if(len(encryptedText) > 25):
        return
        
    wheels = []
    with open("m-94wheels.txt", "r") as txt:
        for line in txt:
            wheels.append(line[0:len(line) -1])

    

    wheels = adjustStarting(wheels, encryptedText)
    

    possible = []
    for i in range(len(wheels[0])):
        temp = ""
        for  t in range(len(wheels)):
            temp += wheels[t][i]
        possible.append(temp)

   

    dict = []
    with open("dictionary.txt", "r") as txt:
        dict = txt.read().split()

    ratio = {}
    for p in possible:
        
        ratio[p] = isEnglish(p, dict)

    exitString = []

    for r in ratio:
        exitString.append(str(r) + " : " + str(ratio[r]) + "\n")

    

    exitText["text"] = exitString

    

        

    
def isEnglish(s, dict):
    c = 0
    for i in range(len(s)):
        for t in range(i, len(s)):
            if s[i : t+1].upper() in dict:
                c += 1
                

    return(c)


def adjustStarting(t, m):
    for i in range(len(m)):
        char = m[i]
        
        ind = t[i].find(char)
        t[i] = t[i][ind : len(t[i])] + t[i][0 : ind]
    return t
        


    
    
    



if(__name__ == "__main__"):
    main()