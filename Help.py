from tkinter import *

root=Tk()
root.title("Help")
root.geometry("720x360")
#root.resizable(0,0)
#-----------------Create Frame--------------------------
F=Frame(root)
F.pack()

F_Left=Frame(root,width=200,height=360).pack(side=LEFT)
F_Right=Frame(root,width=520,height=360,bg="green").pack(side=RIGHT)
#---------------------------------------------------------------------
L=Label(F_Left,text="Standed",ancho=E).pack()
root.mainloop()
