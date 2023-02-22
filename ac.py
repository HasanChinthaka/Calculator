from tkinter import*
import math
#------------------------ Put Number/Operator Display --------------------------------------------------------
def click (n):
    global operator
    operator=operator+str(n)
    text_Input.set(operator)

#-------------------------- Calculate Square ------------------------------------------------
def square():
    x=v.get()
    if x=="Binary":
        z=txtDisplay.get()
        z=BinarytoDecimal(z)
        z=math.sqrt(float(z))
        z=str(DecimaltoBinary(z))
        text_Input.set(z+"0")
    elif x=="Octal":
        z=txtDisplay.get()
        z=OctaltoDecimal(z)
        z=math.sqrt(float(z))
        z=str(DecimaltoOctal(z))
        text_Input.set(z+"0")
    elif x=="Hexa_Decimal":
        z=txtDisplay.get()
        z=HexatoDecimal(z)
        z=math.sqrt(float(z))
        z=str(DecimaltoHexa(z))
        text_Input.set(z+"0")
    else:
        text_Input.set(str(math.sqrt(float(txtDisplay.get()))))
#------------------------------ Clear Display ----------------------------------------------------
def clear ():
    global operator
    operator=""
    text_Input.set("")
#--------------------------------------------------------------------------------
#-------------------------- Number System Converting Function (in advance calculator) ------------------------------------------------------
#------------------------------ Decimal number convert Binary number  --------------------------------------------------
def DecimaltoBinary(c):
    c=str(c)
    #c=txtDisplay.get()
    if c=="0":
        u=0
    else:
        t=""
        z=""
        w=0
        for i in c:
            if i==".":
                w=float(c)
        x=type(w)
        if x==float:
            s=str(w)
            s=s.split(".")
            for i in range (0,2):
                if i ==0:
                    b=int(s[i])   
                    g=""
                    while b!=0:
                        a=b%2
                        b=b//2
                        g=str(a)+g
                    g=g
                elif i==1:
                    b="0."+s[1]
                    b=float(b)
                    z=""
                    j=0
                    while j!=20:
                            a=b*2
                            h=str(a)
                            h=h.split(".")
                            z=z+h[0]
                            k="0."+h[1]
                            b=float(k)
                            j=j+1
                    u=g+"."+z
                    u=float(u)
                    u=str(round(u,10))
                    u=u.rstrip("0")
        else:
            b=int(c)
            z=""
            while b!=0:
                a=b%2
                b=b//2
                z=str(a)+z
            u=z
    text_Input.set(u)
    return u;
#---------------------------------- Decimal number convert Octal number -----------------------------------------------------
def DecimaltoOctal(c):
    c=str(c)
    if c=="0":
        u=0
    else:
        t=""
        z=""
        w=0
        #c=txtDisplay.get()
        for i in c:
            if i==".":
                w=float(c)
        x=type(w)
        if x==float:
            s=str(w)
            s=s.split(".")
            for i in range (0,2):
                if i ==0:
                    b=int(s[i])   
                    g=""
                    while b!=0:
                        a=b%8
                        b=b//8
                        g=str(a)+g
                    g=g
                elif i==1:
                    b="0."+s[1]
                    b=float(b)
                    z=""
                    j=0
                    while j!=20:
                            a=b*8
                            h=str(a)
                            h=h.split(".")
                            z=z+h[0]
                            k="0."+h[1]
                            b=float(k)
                            j=j+1
                    u=g+"."+z
                    u=float(u)
                    u=str(round(u,10))
                    u=u.rstrip("0")
        else:
            b=int(c)   
            z=""
            while b!=0:
                a=b%8
                b=b//8
                z=str(a)+z
            u=z
    text_Input.set(u)
    return u;
#----------------------------------- Decimal number convert Hexa - Decimal number -------------------------------------------------
def DecimaltoHexa(c):
    c=str(c)
    #c=txtDisplay.get()
    if c=="0":
        u=0
    else:
        t=""
        z=""
        x=""
        w=0
        for i in c:
            if i==".":
                s=c.split(".")
                x="y"
        if x=="y":
            for i in range (0,2):
                if i ==0:
                    b=int(s[i])   
                    g=""
                    while b!=0:
                        a=b%16
                        if a>=10:
                            d={"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
                            for i in d.keys():
                                if str(a)==i:
                                     a=d.get(i)
                        b=b//16
                        g=str(a)+g
                    g=g
                elif i==1:
                    b="0."+s[1]
                    b=float(b)
                    z=""
                    j=0
                    while j!=6:
                            a=b*16
                            h=str(a)
                            h=h.split(".")
                            if int(h[0])>9:
                                d={"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
                                for i in d.keys():
                                    if h[0]==i:
                                         a=d.get(i)
                                z=z+a
                            z=z+h[0]
                            k="0."+h[1]
                            b=float(k)
                            j=j+1
                    u=g+"."+z
                    u=u.rstrip("0")
        else:
            b=int(c)   
            z=""
            while b!=0:
                a=b%16
                if a>=10:
                    d={"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
                    for i in d.keys():
                        if str(a)==i:
                            a=d.get(i)
                b=b//16
                z=str(a)+z
            u=z
    text_Input.set(u)
    return u;
#----------------------------------- Binary number number convert Decimal number --------------------------------------------------
def BinarytoDecimal(s):
    #s=txtDisplay.get()
    s=str(s)
    tot=0
    f=""
    for i in s:
        if i==".":
            l=s.split(".")
            f="L"
    if f =="L":
        for o in l:
            for i in o:
                if int(i)>1:
                    text_Input.set("Invaliad Input")
                    return
    if f =="L":
        w=len(l[0])
        e=l[0]
        q=0
        t=0
        for u in range (w,0,-1):
            f=e[u-1]
            t=t+((2**q)*int(f))
            q=q+1
        tot=tot+t
        q=-1
        T=0.0
        for u in l[1]:
            T=T+((2**q)*int(u))
            q=q-1
        tot=tot+T
    else:
        for i in s:
            if int(i)>1:
                text_Input.set("Invaliad Input")
                return
        w=len(s)
        t=0
        q=0
        for i in range (w,0,-1):
            f=s[i-1]
            t=t+((2**q)*int(f))
            q=q+1
        tot=t
    text_Input.set(tot)
    return tot;

#---------------------------------- Binary number number convert Octal number ------------------------------------------------
def BinarytoOctal(s):
    tot=BinarytoDecimal(s)
    t=DecimaltoOctal(tot)
    text_Input.set(t)

#----------------------------------- Binary number number convert Hexa - Decimal number -----------------------------------------------
def BinarytoHexa(s):
    c=str(BinarytoDecimal(s))
    u=DecimaltoHexa(c)
    text_Input.set(u)
#---------------------------------------- Octal number number convert Decimal number -----------------------------------------
def OctaltoDecimal(s):
    #s=txtDisplay.get()
    s=str(s)
    tot=0
    f=""
    for i in s:
        if i==".":
            l=s.split(".")
            f="L"
    if f =="L":
        for o in l:
            for i in o:
                if int(i)>=8:
                    #text_Input.set("Invaliad Input")
                    return
    if f =="L":
        w=len(l[0])
        e=l[0]
        q=0
        t=0
        for u in range (w,0,-1):
            f=e[u-1]
            t=t+((8**q)*int(f))
            q=q+1
        tot=tot+t
        q=-1
        T=0.0
        for u in l[1]:
            T=T+((8**q)*int(u))
            q=q-1
        tot=tot+T
    else:
        for i in s:
            if int(i)>=8:
                #text_Input.set("Invaliad Input")
                return
        w=len(s)
        t=0
        q=0
        for i in range (w,0,-1):
            f=s[i-1]
            t=t+((8**q)*int(f))
            q=q+1
        tot=t
    text_Input.set(tot)
    return tot; 
#------------------------------- Octal number number convert Binary number ------------------------------------------------
def OctaltoBinary(s):
    tot=str(OctaltoDecimal(s))
    u=DecimaltoBinary(tot)
    text_Input.set(u)
#--------------------------------- Octal number number convert Hexa-Decimal number ---------------------------------------------
def OctaltoHexa(s):
    c=str(OctaltoDecimal(s))
    u=DecimaltoHexa(c)
    text_Input.set(u)
#------------------------------------ Hexa - Decimal number number convert Decimal number -----------------------------------------------------
def HexatoDecimal(b):
    #b=txtDisplay.get()
    b=str(b)
    d={"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","A":"10","B":"11","C":"12","D":"13","E":"14","F":"15"}
    q=d.keys()
    tot=0
    x=""
    for i in b:
        if i==".":
            L=b.split(".")
            x="L"
    if x=="L":
        b=L[0]
        b=b[::-1]
        z=0
        p=0
        for t in b:
            for i in q:
                if t==i:
                    w=d.get(i)
                    z=z+((16**p)*int(w))
                    p=p+1
        tot=tot+z
        B=L[1]
        Z=0.0
        P=-1
        for T in B:
            for I in q:
                if T==I:
                    W=d.get(I)
                    Z=Z+((16**P)*float(W))
                    P=P-1
        tot=tot+Z
    else:
        b=b[::-1]
        p=0
        for t in b:
            for i in q:
                if t==i:
                    w=d.get(i)
                    tot=tot+((16**p)*int(w))
                    p=p+1
    text_Input.set(tot)
    return tot;
#---------------------------- Hexa - Decimal number number convert Binary number ------------------------------------------------------
def HexatoBinary(s):
    c=str(HexatoDecimal(s))
    u=DecimaltoBinary(c)
    text_Input.set(u)
#----------------------------- Hexa - Decimal number number convert Octal number ------------------------------------
def HexatoOctal(s):
    c=str(HexatoDecimal(s))
    u=DecimaltoOcta(c)
    text_Input.set(u)
#------------------------------ Number System Opertation Function (in advance calculator) ---------------------------------------------------
#---------------------------------- Addition Decimal number -----------------------------------------
def Decimal_Add():
    p=txtDisplay.get()
    p=p.split("+")
    S=float(p[0])
    for i in range (1,len(p)):
        S=S+float(p[i])
    S=str(S)
    e=S.split(".")
    w=e[1]
    if int(w) >0:
        S=float(S)
    else:
        S=int(e[0])
    text_Input.set(S)     
#---------------------------------- Subtraction Decimal number ---------------------------------------
def Decimal_Sub():
    p=txtDisplay.get()
    p=p.split("-")
    S=float(p[0])
    for i in range (1,len(p)):
        S=S-float(p[i])
    S=str(S)
    e=S.split(".")
    w=e[1]
    if int(w) >0:
        S=float(S)
    else:
        S=int(e[0])
    text_Input.set(S)    
#----------------------------------- Multiply Decimal number --------------------------------------
def Decimal_Mul():
    p=txtDisplay.get()
    p=p.split("*")
    S=float(p[0])
    for i in range (1,len(p)):
        S=S*float(p[i])
    S=str(S)
    e=S.split(".")
    w=e[1]
    if int(w) >0:
        S=float(S)
    else:
        S=int(e[0])
    text_Input.set(S)   
#------------------------------------- Division Decimal number ------------------------------------
def Decimal_Div():
    p=txtDisplay.get()
    p=p.split("/")
    S=float(p[0])
    for i in range (1,len(p)):
        S=S/float(p[i])
    S=str(S)
    e=S.split(".")
    w=e[1]
    if int(w) >0:
        S=float(S)
    else:
        S=int(e[0])
    text_Input.set(S)    
#------------------------------------- Addition Binary number ------------------------------------
def Binary_Add():
    p=txtDisplay.get()
    p=p.split("+") 
    l=[]
    T=0
    for i in p:
        t=BinarytoDecimal(i)
        l.append(t)
    for q in l:
        T=T+q
    u=DecimaltoBinary(T)
    text_Input.set(u)
#-------------------------------------- Subtraction Binary number ------------------------------------
def Binary_Sub():
    p=txtDisplay.get()
    p=p.split("-")
    l=[]
    for i in  p:
        t=BinarytoDecimal(i)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
            T=T-l[q]
    u=DecimaltoBinary(T)
    text_Input.set(u)
#--------------------------------------- Multiply Binary number -----------------------------------
def Binary_Mul():
    p=txtDisplay.get()
    p=p.split("*")
    l=[]
    for g in p:
        t=BainarytoDecimal(g)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
        T=T*l[q]
    u=DecimaltoBinary(T)
    text_Input.set(u)
#---------------------------------------- Division Binary number ----------------------------------
def Binary_Div():
    p=txtDisplay.get()
    p=p.split("/")
    l=[]
    for g in p:
        t=BinarytoDecimal(g)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
        T=T/l[q]
    u=DecimaltoBinary(T)
    text_Input.set(u)
#------------------------------------------- Addition Octal number -------------------------------
def Octal_Add():
    p=txtDisplay.get()
    p=p.split("+") 
    l=[]
    T=0
    for i in p:
        t=OctaltoDecimal(i)
        l.append(t)
    for q in l:
        T=T+q
    u=DecimaltoOctal(T)
    text_Input.set(u)
#---------------------------------------- Subtraction Octal number ----------------------------------
def Octal_Sub():
    p=txtDisplay.get()
    p=p.split("-")
    l=[]
    for g in p:
        t=OctaltoDecimal(g)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
        T=T-l[q]
    u=DecimaltoOctal(T)
    text_Input.set(u)
#------------------------------------------ Multply Octal number --------------------------------
def Octal_Mul():
    p=txtDisplay.get()
    p=p.split("*")
    l=[]
    for g in p:
        t=OctaltoDecimal(g)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
        T=T*l[q]
    u=DecimaltoOctal(T)
    text_Input.set(u)
#---------------------------------------- Division Octal number ----------------------------------
def Octal_Div():
    p=txtDisplay.get()
    p=p.split("/")
    l=[]
    for g in p:
        t=OctaltoDecimal(g)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
        T=T/l[q]
    u=DecimaltoOctal(T)
    text_Input.set(u)
#----------------------------------------- Addition Hexa - Decimal number ---------------------------------
def Hexa_Decimal_Add():
    p=txtDisplay.get()
    p=p.split("+") 
    l=[]
    T=0
    for i in p:
        t=HexatoDecimal(i)
        l.append(t)
    for q in l:
        T=T+q
    u=DecimaltoHexa(T)
    text_Input.set(u)
#------------------------------------------ Subtraction Hexa - Decimal number --------------------------------
def Hexa_Decimal_Sub():
    p=txtDisplay.get()
    p=p.split("-")
    l=[]
    for g in p:
        t=HexatoDecimal(g)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
        T=T-l[q]
    u=DecimaltoHexa(T)
    text_Input.set(u)
#------------------------------------------- Multiply Hexa - Decimal number -------------------------------
def Hexa_Decimal_Mul():
    p=txtDisplay.get()
    p=p.split("*")
    l=[]
    for g in p:
        t=HexatoDecimal(g)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
        T=T*l[q]
    u=DecimaltoHexa(T)
    text_Input.set(u)
#----------------------------------------- Division Hexa - Decimal number ---------------------------------
def Hexa_Decimal_Div():
    p=txtDisplay.get()
    p=p.split("/")
    l=[]
    for g in p:
        t=HexatoDecimal(g)
        l.append(t)
    T=l[0]
    for q in range (1,len(l)):
        T=T/l[q]
    u=DecimaltoHexa(T)
    text_Input.set(u)
#------------------------------- Selection of Decimal operation -------------------------------------------
def Decimal_Selection():
    T=txtDisplay.get()
    for o in T:
        if o=="+":
            Decimal_Add()
        elif o=="-":
            Decimal_Sub()
        elif o=="*":
            Decimal_Mul()
        elif o=="/":
            Decimal_Div()

#--------------------------------- Selection of Binary operation --------------------------------------------------
def Binary_Selection():
    T=txtDisplay.get()
    for o in T:
        if o=="+":
            Binary_Add()
        elif o=="-":
            Binary_Sub()
        elif o=="*":
            Binary_Mul()
        elif o=="/":
            Binary_Div()
#------------------------------------ Selection of Octal operation ------------------------------------
def Octal_Selection():
    T=txtDisplay.get()
    for o in T:
        if o=="+":
            Octal_Add()
        elif o=="-":
            Octal_Sub()
        elif o=="*":
            Octal_Mul()
        elif o=="/":
            Octal_Div()
#--------------------------------------- Selection of Hexa - Decimal operation ---------------------------------
def Hexa_Decimal_Selection():
    T=txtDisplay.get()
    for o in T:
        if o=="+":
            Hexa_Decimal_Add()
        elif o=="-":
            Hexa_Decimal_Sub()
        elif o=="*":
            Hexa_Decimal_Mul()
        elif o=="/":
            Hexa_Decimal_Div()
#------------------------------------ Identify Number System ------------------------------------
def selection():
    x=v.get()
    if x=="Decimal":
         Decimal_Selection()
    elif x=="Binary":
         Binary_Selection()
    elif x=="Octal":
         Octal_Selection()
    elif x=="Hexa_Decimal":
         Hexa_Decimal_Selection()
#------------------------------------ Create Main Window ----------------------------------------------
root=Tk()
root.title("calculator")
root.iconbitmap("Calculator.ico")
root.geometry("338x570")
operator=""
text_Input=StringVar()
w=StringVar()
#-----------------------------------------------------------------------------------

#-------------------------------- Menue Bar Function ----------------------------------------------------
#-------------------------View Menue Function -------------------------------------------
#--------------------------- Standard --------------------------------------------
def Normal():
    D.select()
    root.geometry("338x570")
#---------------------------- Advance ----------------------------------------------------
def Advance():
    root.geometry("705x570")

#------------------------------- Help Menue Function ----------------------------------------------
#---------------------------------- Help --------------------------------------------------------------
def Help():
    top=Toplevel()
    top.title("Help")
    top.iconbitmap("help.ico")
    top.geometry("720x360")
    
#------------------------------- About ----------------------------------------------------
f=PhotoImage(file=r"About.png")
def About():
    top=Toplevel()
    top.title("About Calculator")
    top.iconbitmap("Calculator.ico")
    top.geometry("380x180")
    l=Label(top,image=f).pack()
    top.resizable(0,0)
#----------------------------------------- Create Menue Bar ---------------------------------------------
mb=Menu(root)
#------------------- View Menue ---------------------------------------------------
vm=Menu(mb,tearoff=0)
vm.add_command(label="standard", command=Normal)
vm.add_command(label="Advance", command=Advance)
vm.add_separator()
vm.add_command(label="Exit", command=root.quit)
mb.add_cascade(label="View", menu=vm)
#------------------ Help Menue -----------------------------------------------
hm=Menu(mb,tearoff=0)
hm.add_command(label="Help",command=Help)
hm.add_separator()
hm.add_command(label="About",command=About)
mb.add_cascade(label="Help", menu=hm)
root.config(menu=mb)
#-----------------------------------------------------------------------------------------


#--------------------------------- Define Display --------------------------------------------------
txtDisplay=Entry(root,font=('arial',20,'bold'),bd=14,insertwidth=4,textvariable=text_Input,bg="#fce9dc",relief="groove")
#txtDisplay.insert(0,"0")
txtDisplay.grid(columnspan=4)
#------------------------------------------------------------------------------------------
#----------------------------------- Define Number Pad -----------------------------------------------
clear=Button(root,padx=16,pady=16,bd=8,text="C",font=('arial',18,'bold'),bg="#ff6d6d",activebackgroun="red",command=clear).grid(row=1,column=0)
sq=Button(root,padx=18,pady=14,bd=8,text="√",font=('arial',18,'bold'),bg="light green",activebackgroun="#00ff00",command=square).grid(row=1,column=1)
mul=Button(root,padx=20,pady=16,bd=8,text="*",font=('arial',18,'bold'),bg="light green",activebackgroun="#00ff00",command=lambda:click("*")).grid(row=1,column=2)
div=Button(root,padx=20,pady=16,bd=8,text="/",font=('arial',18,'bold'),bg="light green",activebackgroun="#00ff00",command=lambda:click("/")).grid(row=1,column=3)

bA=Button(root,padx=16,pady=8,bd=8,text="A",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click("A")).grid(row=0,column=4)
bB=Button(root,padx=16,pady=8,bd=8,text="B",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click("B")).grid(row=0,column=5)
bC=Button(root,padx=16,pady=8,bd=8,text="C",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click("C")).grid(row=0,column=6)
#---------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
b7=Button(root,padx=16,pady=16,bd=8,text="7",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(7)).grid(row=2,column=0)
b8=Button(root,padx=16,pady=16,bd=8,text="8",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(8)).grid(row=2,column=1)
b9=Button(root,padx=16,pady=16,bd=8,text="9",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(9)).grid(row=2,column=2)
#-----------------------------------------------------------------------------------
Sub=Button(root,padx=18,pady=16,bd=8,text="-",font=('arial',20,'bold'),bg="light green",activebackgroun="#00ff00",command=lambda:click("-")).grid(row=2,column=3)
#---------------------------------------------------------------------------------------
bD=Button(root,padx=16,pady=16,bd=8,text="D",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click("D")).grid(row=1,column=4)
bE=Button(root,padx=16,pady=16,bd=8,text="E",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click("E")).grid(row=1,column=5)
bF=Button(root,padx=16,pady=16,bd=8,text="F",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click("F")).grid(row=1,column=6)

#-------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
b4=Button(root,padx=16,pady=16,bd=8,text="4",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(4)).grid(row=3,column=0)
b5=Button(root,padx=16,pady=16,bd=8,text="5",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(5)).grid(row=3,column=1)
b6=Button(root,padx=16,pady=16,bd=8,text="6",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(6)).grid(row=3,column=2)
#---------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
Add=Button(root,padx=16,pady=16,bd=8,text="+",font=('arial',20,'bold'),bg="light green",activebackgroun="#00ff00",command=lambda:click("+")).grid(row=3,column=3)
#--------------------------------------------------------------------------------------------------------
t=PhotoImage(file=r"B_Image/1.PNG")
db=Button(root,padx=16,pady=16,bd=8,image=t,bg="light blue",activebackgroun="#00a7f0",command=lambda:DecimaltoBinary(txtDisplay.get())).grid(row=2,column=4)
o=PhotoImage(file=r"B_Image/2.PNG")
do=Button(root,padx=16,pady=16,bd=8,image=o,font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:DecimaltoOctal(txtDisplay.get())).grid(row=2,column=5)
h=PhotoImage(file=r"B_Image/3.PNG")
dh=Button(root,padx=16,pady=16,bd=8,image=h,font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:DecimaltoHexa(txtDisplay.get())).grid(row=2,column=6)

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
b1=Button(root,padx=16,pady=16,bd=8,text="1",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(1)).grid(row=4,column=0)
b2=Button(root,padx=16,pady=16,bd=8,text="2",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(2)).grid(row=4,column=1)
b3=Button(root,padx=16,pady=16,bd=8,text="3",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(3)).grid(row=4,column=2)
#----------------------------------------------------------------------------------------
equal=Button(root,padx=16,pady=65,bd=8,text="=",font=('arial',20,'bold'),bg="light green",activebackgroun="#00ff00",command=selection).grid(row=4,rowspan=2,column=3)
#-------------------------------------------------------------------------------------------------
tt=PhotoImage(file=r"B_Image/4.PNG")
bd=Button(root,padx=16,pady=16,bd=8,image=tt,bg="light blue",activebackgroun="#00a7f0",command=lambda:BinarytoDecimal(txtDisplay.get())).grid(row=3,column=4)
oo=PhotoImage(file=r"B_Image/5.PNG")
bo=Button(root,padx=16,pady=16,bd=8,image=oo,font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:BinarytoDecimal(txtDisplay.get())).grid(row=3,column=5)
hh=PhotoImage(file=r"B_Image/6.PNG")
bh=Button(root,padx=16,pady=16,bd=8,image=hh,font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:BinarytoDecimal(txtDisplay.get())).grid(row=3,column=6)

#---------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
b0=Button(root,padx=60,pady=16,bd=8,text="0",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(0)).grid(row=5,columnspan=2)
dot=Button(root,padx=18,pady=16,bd=8,text=".",font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:click(".")).grid(row=5,column=2)
#--------------------------------------------------------------------------------------------------
ttt=PhotoImage(file=r"B_Image/7.PNG")
od=Button(root,padx=16,pady=16,bd=8,image=ttt,bg="light blue",activebackgroun="#00a7f0",command=lambda:OctaltoDecimal(txtDisplay.get())).grid(row=4,column=4)
ooo=PhotoImage(file=r"B_Image/8.PNG")
ob=Button(root,padx=16,pady=16,bd=8,image=ooo,font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:BinarytoDecimal(txtDisplay.get())).grid(row=4,column=5)
hhh=PhotoImage(file=r"B_Image/9.PNG")
oh=Button(root,padx=16,pady=16,bd=8,image=hhh,font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:BinarytoDecimal(txtDisplay.get())).grid(row=4,column=6)
#--------------------------------------------------------------------------------------------
tttt=PhotoImage(file=r"B_Image/10.PNG")
hd=Button(root,padx=16,pady=16,bd=8,image=tttt,bg="light blue",activebackgroun="#00a7f0",command=lambda:HexatoDecimal(txtDisplay.get())).grid(row=5,column=4)
oooo=PhotoImage(file=r"B_Image/11.PNG")
hb=Button(root,padx=16,pady=16,bd=8,image=oooo,font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:BinarytoDecimal(txtDisplay.get())).grid(row=5,column=5)
hhhh=PhotoImage(file=r"B_Image/12.PNG")
ho=Button(root,padx=16,pady=16,bd=8,image=hhhh,font=('arial',20,'bold'),bg="light blue",activebackgroun="#00a7f0",command=lambda:BinarytoDecimal(txtDisplay.get())).grid(row=5,column=6)
#-------------------------------------------------------------------------------------------------------

#-------------------------------------- Area for Selection Number System -----------------------------------------------------
v=StringVar()

D=Radiobutton(root,text="Decimal        ",variable=v,value="Decimal")
D.select()
D.grid(row=1,column=8)
B=Radiobutton(root,text="Binary          ",variable=v,value="Binary").grid(row=2,column=8)
O=Radiobutton(root,text="Octal           ",variable=v,value="Octal").grid(row=3,column=8)
H=Radiobutton(root,text="Hexa-Decimal",variable=v,value="Hexa_Decimal").grid(row=4,column=8)
#-----------------------------------------------------------------------------------------------
root.resizable(0,0)
root.mainloop()
