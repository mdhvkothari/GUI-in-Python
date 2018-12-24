from tkinter import * 
g = Tk()

def func1():
	txt1 = txt.get()
	Label(text=txt1,font=10).pack()


g.title('Calculator')
g.geometry('500x500+0+0')
#for input to string
txt = StringVar()

mylabe = Label(text='first label',fg='blue',bg='yellow').place(x=100,y=200)
mylabe2= Label(text='second label' ,fg='red').place(x=100,y=300)

mylabe3 = Label(text='third with grid').pack()

mylabe4= Label(text='fourth gird').place(x=50,y=50)

btn1 = Button(text='Submit',fg='green',bg='pink',command=func1).place(x=70,y=100);

myText = Entry(textvariable=txt).pack()










g.mainloop()
