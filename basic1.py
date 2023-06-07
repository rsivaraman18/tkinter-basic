# Basic template for every Tkinter's
from tkinter import *
window = Tk()


# We can Set Geometric Size of window
window.title("Tkinter Basic Window")
window.minsize(width=100,height=200)
window.maxsize(width=600,height=600)



# create Label box
lab1 = Label(window,text='Siva learning',bg='blue',font='arial')

#lab1.grid(row=0,column=45)
lab1.place(x=45,y=10)


# insert Photo Image
img1 = PhotoImage(file='D:/visual studio Projects/Tkinter1/book1.gif')
lab2 = Label(window,image = img1)
lab2.place(x=60,y=150)





# Create Entery wizard
en1 = Entry(window,bg='orange',bd=5,width=10,font=('calibri',50))
en1.place(x=50,y=50)


# Create Buttons
b1 = Button(window,text='Enter this button',bg='yellow',fg='green',bd=15)
b1.pack()



window = mainloop() # infinite loop .place at the bottom of code


