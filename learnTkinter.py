import tkinter as tk

def main():
    t = ["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"]
    labels = []


    def plus(data):
        name = data[0]
        number = data[1]
        cipher = data[2]

        i = cipher.index(name["text"])
        i += 1
        if(i > 25):
            i = 0
        name["text"] = cipher[i]
        
        
    
    def minus(data):
        name = data[0]
        number = data[1]
        cipher = data[2]

        i = cipher.index(name["text"])
        i -= 1
        if(i < 0):
            i = 25
        name["text"] = cipher[i]
    
    def addAll():
        for i in labels:
            plus(i)


    window = tk.Tk()
    

    window.rowconfigure([0,1,2,3], minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)

    for i in range(2):
        locals()['f%dbtnMinus' , (i)] = tk.Button(master=window, text="-" ,command=lambda: minus(labels[i]), height=1)
        locals()['f%dbtnMinus' , (i)].grid(row=0, column=i, sticky="nsew")

        locals()['f%dlbl' , (i)] = tk.Label(master= window, text= t[i][0], height=1, background= "red")
        locals()['f%dlbl' , (i)].grid(row=1, column=i, sticky="nsew")
        labels.append(([locals()['f%dlbl' , (i)], i, t[i]]))

        locals()['f%dplus' , (i)] = tk.Button(master=window, text="+" , command=lambda: plus(labels[i]), height=1)
        locals()['f%dplus' , (i)].grid(row=2, column=i, sticky="nsew")


    Addallbtn = tk.Button(master=window, text="+" , command=addAll, height=1)
    Addallbtn.grid(row=3, column=1, sticky="nsew")

    

    

    

    window.mainloop()

if(__name__ == "__main__"):
    main()