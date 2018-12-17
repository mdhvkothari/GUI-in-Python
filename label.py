from tkinter import * 
g = Tk()
g.title('Calculator')
g.geometry('500x500+0+0')

mylabe = Label(text='first label',fg='blue',bg='yellow').place(x=100,y=200)
mylabe2= Label(text='second label' ,fg='red').place(x=100,y=300)

mylabe3 = Label(text='third with grid').grid(row=0,column=0)

mylabe4= Label(text='fourth gird').grid(row=1,column=0,stick='e')












g.mainloop()
