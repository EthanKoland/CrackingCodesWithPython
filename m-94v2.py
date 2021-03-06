import random, os, sys, tkinter as tk
from typing import Text



def main():
    if( not os.path.exists("m-94wheels.txt")):
        print("please install m-94wheels.txt")
        sys.exit()

    t = ""

    with open('m-94wheels.txt', "r") as m:
        t = m.read()
    
    t = t.split()

    plainText = ""

    

    

    #Start Gui
    labels = []
    positions = [0] * 25
    MinusButtons = []
    PlusButtons = []


    def plus(data):
        name = data[0]
        number = data[1]
        cipher = data[2]

        positions[number] = (1+positions[number])%26

        name["text"] = cipher[positions[number]]
        updateText()
        
        
    
    def minus(data):
        
        name = data[0]
        number = data[1]
        cipher = data[2]
        
        positions[number] = (-1+positions[number])

        if(positions[number] < 0):
            positions[number] = 25

        name["text"] = cipher[positions[number]]
        
        updateText()
    
    def addAll():
        for i in labels:
            plus(i)

    def minusAll():
        for i in labels:
            minus(i)

    def encrypt(pt):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        f = ""
        for i in range(len(pt)):
            if(pt[i]  in alpha):
                f += pt[i]
        
        pt = f
        if(len(pt) > 25):
            encryptEntry.delete(0, tk.END)
            encryptEntry.insert(0,"Text is longer than 25 chars")
            return
        for i in range(len(pt)):
            data = labels[i]
            name = data[0]
            number = data[1]
            cipher = data[2]
            t =cipher.find(pt[i])
            positions[i] = t
            name["text"] = cipher[positions[number]]

        updateText()

    


        
        
        

    def updateText():
        out = ""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(positions)):
            ind = t[i]
            pos = positions[i]
            out += ind[pos]
            
            
        encryptEntry.delete(0, tk.END)
        encryptEntry.insert(0,out)
                

    def decrypt(s):
        window1 = tk.Tk()
    

        window1.rowconfigure([0,1], minsize = 100, weight=1)
        window1.columnconfigure([0,1,2], minsize=25, weight=1)

        exitText = tk.Label(master=window1, text="hello", background="blue")
        exitText.grid(row=0, column=0, columnspan=3, sticky="nsew")

        infoText = tk.Label(master=window1, text = "Enter a encrypted Text")
        infoText.grid(column=0, row=1, sticky="nsew")

        encryptEntry = tk.Entry(master=window1)
        encryptEntry.grid(row=1, column=1,  sticky="nsew")

        encryptButton = tk.Button(master=window1, text="encrypt Message", command = lambda: decrypt(encryptEntry.get(), exitText) )
        encryptButton.grid(row=1, column=2, sticky="NSEW")
        
        encryptedText = s

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
            
            



    

    




    


    window = tk.Tk()
    

    window.rowconfigure([0,1,2,3], minsize=25, weight=1)
    window.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25, 26], minsize=25, weight=1)

    Addallbtn = tk.Button(master=window, text="add all" , command=addAll, height=1,)
    Addallbtn.grid(row=2, column=26, sticky="nsew")

    Minusallbtn = tk.Button(master=window, text="Minus all" , command=minusAll, height=1,)
    Minusallbtn.grid(row=1, column=26, sticky="nsew")


    plainText = tk.Label(master=window, text="Plain text")
    plainText.grid(row=3, column=0, columnspan=3, sticky="nsew")

    plainEntry = tk.Entry(master=window)
    plainEntry.grid(row=3, column=3, columnspan=7, sticky="nsew")

    encryptButton = tk.Button(master=window, text="encrypt Message", command=lambda: encrypt(plainEntry.get()))
    encryptButton.grid(row=3, column=26, sticky="NSEW")

    decryptButton = tk.Button(master=window, text="Decrypt Message", command=lambda: decrypt(encryptEntry.get()))
    decryptButton.grid(row=0, column=26, sticky="NSEW")


    encryptText = tk.Label(master=window, text="Encrypted Text")
    encryptText.grid(row=3, column=10, columnspan=5, sticky="nsew")

    encryptEntry = tk.Entry(master=window)
    encryptEntry.grid(row=3, column=15, columnspan=7, sticky="nsew")



    

        
    i = 0

    Plus0 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[0]), height=1)
    Plus0.grid(row=0, column=i, sticky="nsew")
        

    Label0 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label0.grid(row=1, column=i, sticky="nsew")
    labels.append((Label0, i, t[i]))

    Minus0 = tk.Button(master=window, text="+" , command=lambda: plus(labels[0]), height=1)
    Minus0.grid(row=2, column=i, sticky="nsew")
        
    i += 1

    Plus1 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[1]), height=1)
    Plus1.grid(row=0, column=1, sticky="nsew")
        

    Label1 = tk.Label(master= window, text= t[1][0], height=1, background= "red")
    Label1.grid(row=1, column=i, sticky="nsew")
    labels.append((Label1, 1, t[1]))

    Minus1 = tk.Button(master=window, text="+" , command=lambda: plus(labels[1]), height=1)
    Minus1.grid(row=2, column=1, sticky="nsew")

    i += 1

    Plus2 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[2]), height=1)
    Plus2.grid(row=0, column=i, sticky="nsew")
        

    Label2 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label2.grid(row=1, column=i, sticky="nsew")
    labels.append((Label2, i, t[i]))

    Minus2 = tk.Button(master=window, text="+" , command=lambda: plus(labels[2]), height=1)
    Minus2.grid(row=2, column=i, sticky="nsew")

    i += 1

    Plus3 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[3]), height=1)
    Plus3.grid(row=0, column=i, sticky="nsew")
        

    Label3 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label3.grid(row=1, column=i, sticky="nsew")
    labels.append((Label3, i, t[i]))

    Minus3 = tk.Button(master=window, text="+" , command=lambda: plus(labels[3]), height=1)
    Minus3.grid(row=2, column=i, sticky="nsew")

    i +=1

    Plus4 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[4]), height=1)
    Plus4.grid(row=0, column=i, sticky="nsew")
        

    Label4 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label4.grid(row=1, column=i, sticky="nsew")
    labels.append((Label4, i, t[i]))

    Minus4 = tk.Button(master=window, text="+" , command=lambda: plus(labels[4]), height=1)
    Minus4.grid(row=2, column=i, sticky="nsew")

    i +=1

    Plus5 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[5]), height=1)
    Plus5.grid(row=0, column=i, sticky="nsew")
        

    Label5 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label5.grid(row=1, column=i, sticky="nsew")
    labels.append((Label5, i, t[i]))

    Minus5 = tk.Button(master=window, text="+" , command=lambda: plus(labels[5]), height=1)
    Minus5.grid(row=2, column=i, sticky="nsew")

    i +=1

    Plus6 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[6]), height=1)
    Plus6.grid(row=0, column=i, sticky="nsew")
        

    Label6 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label6.grid(row=1, column=i, sticky="nsew")
    labels.append((Label6, i, t[i]))

    Minus6 = tk.Button(master=window, text="+" , command=lambda: plus(labels[6]), height=1)
    Minus6.grid(row=2, column=i, sticky="nsew")

    i +=1

    Plus7 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[7]), height=1)
    Plus7.grid(row=0, column=i, sticky="nsew")
        

    Label7 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label7.grid(row=1, column=i, sticky="nsew")
    labels.append((Label7, i, t[i]))

    Minus7 = tk.Button(master=window, text="+" , command=lambda: plus(labels[7]), height=1)
    Minus7.grid(row=2, column=i, sticky="nsew")

    i +=1

    Plus8 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[8]), height=1)
    Plus8.grid(row=0, column=i, sticky="nsew")
        

    Label8 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label8.grid(row=1, column=i, sticky="nsew")
    labels.append((Label8, i, t[i]))

    Minus8 = tk.Button(master=window, text="+" , command=lambda: plus(labels[8]), height=1)
    Minus8.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss9 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[9]), height=1)
    Pluss9.grid(row=0, column=i, sticky="nsew")
        

    Label9 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label9.grid(row=1, column=i, sticky="nsew")
    labels.append((Label9, i, t[i]))

    Minus9 = tk.Button(master=window, text="+" , command=lambda: plus(labels[9]), height=1)
    Minus9.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss10 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[10]), height=1)
    Pluss10.grid(row=0, column=i, sticky="nsew")
        

    Label10 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label10.grid(row=1, column=i, sticky="nsew")
    labels.append((Label10, i, t[i]))

    Minus10 = tk.Button(master=window, text="+" , command=lambda: plus(labels[10]), height=1)
    Minus10.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss11 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[11]), height=1)
    Pluss11.grid(row=0, column=i, sticky="nsew")
        

    Label11 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label11.grid(row=1, column=i, sticky="nsew")
    labels.append((Label11, i, t[i]))

    Minus11 = tk.Button(master=window, text="+" , command=lambda: plus(labels[11]), height=1)
    Minus11.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss12 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[12]), height=1)
    Pluss12.grid(row=0, column=i, sticky="nsew")
        

    Label12 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label12.grid(row=1, column=i, sticky="nsew")
    labels.append((Label12, i, t[i]))

    Minus12 = tk.Button(master=window, text="+" , command=lambda: plus(labels[12]), height=1)
    Minus12.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss13 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[13]), height=1)
    Pluss13.grid(row=0, column=i, sticky="nsew")
        

    Label13 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label13.grid(row=1, column=i, sticky="nsew")
    labels.append((Label13, i, t[i]))

    Minus13 = tk.Button(master=window, text="+" , command=lambda: plus(labels[13]), height=1)
    Minus13.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss14 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[14]), height=1)
    Pluss14.grid(row=0, column=i, sticky="nsew")
        

    Label14 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label14.grid(row=1, column=i, sticky="nsew")
    labels.append((Label14, i, t[i]))

    Minus14 = tk.Button(master=window, text="+" , command=lambda: plus(labels[14]), height=1)
    Minus14.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss15 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[15]), height=1)
    Pluss15.grid(row=0, column=i, sticky="nsew")
        

    Label15 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label15.grid(row=1, column=i, sticky="nsew")
    labels.append((Label15, i, t[i]))

    Minus15 = tk.Button(master=window, text="+" , command=lambda: plus(labels[15]), height=1)
    Minus15.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss16 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[16]), height=1)
    Pluss16.grid(row=0, column=i, sticky="nsew")
        

    Label16 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label16.grid(row=1, column=i, sticky="nsew")
    labels.append((Label16, i, t[i]))

    Minus16 = tk.Button(master=window, text="+" , command=lambda: plus(labels[16]), height=1)
    Minus16.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss17 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[17]), height=1)
    Pluss17.grid(row=0, column=i, sticky="nsew")
        

    Label17 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label17.grid(row=1, column=i, sticky="nsew")
    labels.append((Label17, i, t[i]))

    Minus17 = tk.Button(master=window, text="+" , command=lambda: plus(labels[17]), height=1)
    Minus17.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss18 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[18]), height=1)
    Pluss18.grid(row=0, column=i, sticky="nsew")
        

    Label18 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label18.grid(row=1, column=i, sticky="nsew")
    labels.append((Label18, i, t[i]))

    Minus18 = tk.Button(master=window, text="+" , command=lambda: plus(labels[18]), height=1)
    Minus18.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss19 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[19]), height=1)
    Pluss19.grid(row=0, column=i, sticky="nsew")
        

    Label19 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label19.grid(row=1, column=i, sticky="nsew")
    labels.append((Label19, i, t[i]))

    Minus19 = tk.Button(master=window, text="+" , command=lambda: plus(labels[19]), height=1)
    Minus19.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss20 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[20]), height=1)
    Pluss20.grid(row=0, column=i, sticky="nsew")
        

    Label20 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label20.grid(row=1, column=i, sticky="nsew")
    labels.append((Label20, i, t[i]))

    Minus20 = tk.Button(master=window, text="+" , command=lambda: plus(labels[20]), height=1)
    Minus20.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss21 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[21]), height=1)
    Pluss21.grid(row=0, column=i, sticky="nsew")
        

    Label21 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label21.grid(row=1, column=i, sticky="nsew")
    labels.append((Label21, i, t[i]))

    Minus21 = tk.Button(master=window, text="+" , command=lambda: plus(labels[21]), height=1)
    Minus21.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss22 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[22]), height=1)
    Pluss22.grid(row=0, column=i, sticky="nsew")
        

    Label22 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label22.grid(row=1, column=i, sticky="nsew")
    labels.append((Label22, i, t[i]))

    Minus22 = tk.Button(master=window, text="+" , command=lambda: plus(labels[22]), height=1)
    Minus22.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss23 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[23]), height=1)
    Pluss23.grid(row=0, column=i, sticky="nsew")
        

    Label23 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label23.grid(row=1, column=i, sticky="nsew")
    labels.append((Label23, i, t[i]))

    Minus23 = tk.Button(master=window, text="+" , command=lambda: plus(labels[23]), height=1)
    Minus23.grid(row=2, column=i, sticky="nsew")

    i +=1

    Pluss24 = tk.Button(master=window, text="-" ,command=lambda: minus(labels[24]), height=1)
    Pluss24.grid(row=0, column=i, sticky="nsew")
        

    Label24 = tk.Label(master= window, text= t[i][0], height=1, background= "red")
    Label24.grid(row=1, column=i, sticky="nsew")
    labels.append((Label24, i, t[i]))

    Minus24 = tk.Button(master=window, text="+" , command=lambda: plus(labels[24]), height=1)
    Minus24.grid(row=2, column=i, sticky="nsew")

    


    


    

    

    
    
    window.mainloop()
    
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

if (__name__ == "__main__"):
    main()