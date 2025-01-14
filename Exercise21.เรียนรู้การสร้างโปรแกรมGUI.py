from tkinter import *
import  math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    ResultBMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if float(ResultBMI) < 18.5 :
        print("ผอมเกินไป"),
        labelResultBMI.configure(text="ผอมเกินไป")
    elif float(ResultBMI) <= 22.9 :
        print("น้ำหนักปกติ เหมาะสม"),
        labelResultBMI.configure(text="น้ำหนักปกติ เหมาะสม")
    elif float(ResultBMI) <= 24.9 :
        print("น้ำหนักเกิน"),
        labelResultBMI.configure(text="น้ำหนักเกิน")
    elif float(ResultBMI) <= 29.9 :
        print("อ้วน"),
        labelResultBMI.configure(text="อ้วน")
    elif float(ResultBMI) > 30.0 :
        print("อ้วนมาก"),
        labelResultBMI.configure(text="อ้วนมาก")


MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง(cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก(Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
CalculateButton = (Button(MainWindow,text="คำนวณ"))
CalculateButton.bind('<Button-1>',leftClickButton)
CalculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelBMI = Label(MainWindow,text="BMI :")
labelBMI.grid(row=3,column=0)
labelResultBMI = Label(MainWindow,text="ผลลัพธ์")
labelResultBMI.grid(row=3,column=1)
MainWindow.mainloop()
