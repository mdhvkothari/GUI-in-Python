from tkinter import *

g = Tk()
k = Tk()


def fun1():
	txt1 = txt.get()
	Label(text=txt1,font=10).pack();

# for string input
txt = StringVar()

g.title('Calculator')
k.title('Second')
g.geometry('500x500+0+0')
k.geometry('500x500+600+0')


mylabesecod  = Label(k,text='second window').pack()
mylabe = Label(text='first label',fg='blue',bg='yellow').place(x=100,y=200)
mylabe2= Label(text='second label' ,fg='red').place(x=100,y=300)


mylabe3 = Label(text='third with grid').pack()

mylabe4= Label(text='fourth gird').place(x=50,y=50)


mytext = Entry(textvariable=txt).pack()
btn1 = Button(text='Submit',fg='green',bg='pink',command=fun1).place(x=70,y=100);











g.mainloop()
k.mainloop()
