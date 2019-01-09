from tkinter import *

g = Tk()


def fun1():
	txt1 = txt.get()
	Label(text=txt1,font=10).pack();

# for string input
txt = StringVar()

g.title('Calculator')
g.geometry('500x500+0+0')

mylabe = Label(text='first label',fg='blue',bg='yellow').place(x=100,y=200)
mylabe2= Label(text='second label' ,fg='red').place(x=100,y=300)


mylabe3 = Label(text='third with grid').pack()

mylabe4= Label(text='fourth gird').place(x=50,y=50)


mytext = Entry(textvariable=txt).pack()
btn1 = Button(text='Submit',fg='green',bg='pink',command=fun1).place(x=70,y=100);

# for adding menu label

menulist = Menu()
menulistitem = Menu()

menulistitem.add_command(label='Save')
menulistitem.add_command(label='Save as')
menulistitem.add_command(label='New File')
menulistitem.add_command(label='File window')

menulist.add_cascade(label='File',menu=menulistitem)
menulist.add_cascade(label='Edit')
menulist.add_cascade(label='View')
menulist.add_cascade(label='Save')
menulist.add_cascade(label='Print')



g.config(menu=menulist)







g.mainloop()
