import tkinter
from tkinter import ttk,messagebox

myscreen=tkinter.Tk()
myscreen.title("FirstApp")
myscreen.geometry("400x600")
myscreen.configure(bg='gold')

#tkinter.Label(text='Firstname:').pack()
#tkinter.Label(text='Lastname:').pack()

#tkinter.Label(text='Firstname:',bg='gold',font='Candara 15 bold').place(x=0,y=0)
#tkinter.Label(text='Lastname:',bg='gold',font='Candara 15 bold').place(x=0,y=30)

tkinter.Label(text='Firstname:',bg='gold',font='Candara 15 bold',fg='red').grid(row=0,column=0,sticky='W')
tkinter.Label(text='Lastname:',bg='gold',font='Candara 15 bold',fg='red').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=1,text='Male',bg='gold',font='Candara 15 bold',fg='red').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=2,text='Female',bg='gold',font='Candara 15 bold',fg='red').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='Python',bg='gold',font='Candara 15 bold',fg='red').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='JAVA',bg='gold',font='Candara 15 bold',fg='red').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='PHP',bg='gold',font='Candara 15 bold',fg='red').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text='Android',bg='gold',font='Candara 15 bold',fg='red').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Surat','Baroda','Bhavnagar','Jamnagar']
ttk.Combobox(values=city).grid(row=7,column=0)

def btnclick():
    #print("Button Click!")
    #messagebox.showerror("Error","Somthing went wrong...Try again!")
    #messagebox.showinfo("Success","Your data has been saved!")
    messagebox.showwarning("Warning","Your disk is full!")

tkinter.Button(text='Submit',font='Candara 15 bold',fg='red',command=btnclick).place(x=150,y=300)
tkinter.mainloop()
