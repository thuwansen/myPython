from tkinter import *
root=Tk()
root.title('计算器-万森')
root.geometry('360x430')

calTitle=Label(root,text='计算器',font=('隶书',20))
calTitle.pack()

strScreen=StringVar()
myScreen=Entry(root,textvariable=strScreen,width=20,font=('隶书',25))
myScreen.pack()

def input1():
    temp=strScreen.get()
    temp=temp+'1'
    strScreen.set(temp)
button_1=Button(root,text='1',font=('隶书',25),height=1,width=3,command=input1)
button_1.place(x=30,y=100)


def input2():
    temp=strScreen.get()
    temp=temp+'2'
    strScreen.set(temp)
button_1=Button(root,text='2',font=('隶书',25),height=1,width=3,command=input2)
button_1.place(x=110,y=100)

def input3():
    temp=strScreen.get()
    temp=temp+'3'
    strScreen.set(temp)
button_1=Button(root,text='3',font=('隶书',25),height=1,width=3,command=input3)
button_1.place(x=190,y=100)


def input4():
    temp=strScreen.get()
    temp=temp+'4'
    strScreen.set(temp)
button_1=Button(root,text='4',font=('隶书',25),height=1,width=3,command=input4)
button_1.place(x=30,y=180)

def input5():
    temp=strScreen.get()
    temp=temp+'5'
    strScreen.set(temp)
button_1=Button(root,text='5',font=('隶书',25),height=1,width=3,command=input5)
button_1.place(x=110,y=180)

def input6():
    temp=strScreen.get()
    temp=temp+'6'
    strScreen.set(temp)
button_1=Button(root,text='6',font=('隶书',25),height=1,width=3,command=input6)
button_1.place(x=190,y=180)

def input7():
    temp=strScreen.get()
    temp=temp+'7'
    strScreen.set(temp)
button_1=Button(root,text='7',font=('隶书',25),height=1,width=3,command=input7)
button_1.place(x=30,y=260)

def input8():
    temp=strScreen.get()
    temp=temp+'8'
    strScreen.set(temp)
button_1=Button(root,text='8',font=('隶书',25),height=1,width=3,command=input8)
button_1.place(x=110,y=260)

def input9():
    temp=strScreen.get()
    temp=temp+'9'
    strScreen.set(temp)
button_1=Button(root,text='9',font=('隶书',25),height=1,width=3,command=input9)
button_1.place(x=190,y=260)

def input_plus():
    temp=strScreen.get()
    temp=temp+'+'
    strScreen.set(temp)
button_1=Button(root,text='+',bg='gray',font=('隶书',25),height=1,width=3,command=input_plus)
button_1.place(x=270,y=100)

def input_minus():
    temp=strScreen.get()
    temp=temp+'-'
    strScreen.set(temp)
button_1=Button(root,text='-',bg='gray',font=('隶书',25),height=1,width=3,command=input_minus)
button_1.place(x=270,y=180)

def input_mul():
    temp=strScreen.get()
    temp=temp+'*'
    strScreen.set(temp)
button_1=Button(root,text='*',bg='gray',font=('隶书',25),height=1,width=3,command=input_mul)
button_1.place(x=270,y=260)

def input_div():
    temp=strScreen.get()
    temp=temp+'/'
    strScreen.set(temp)
button_1=Button(root,text='/',bg='gray',font=('隶书',25),height=1,width=3,command=input_div)
button_1.place(x=30,y=340)

def input_dot():
    temp=strScreen.get()
    temp=temp+'.'
    strScreen.set(temp)
button_1=Button(root,text='.',bg='gray',font=('隶书',25),height=1,width=3,command=input_dot)
button_1.place(x=110,y=340)

def input_0():
    temp=strScreen.get()
    temp=temp+'0'
    strScreen.set(temp)
button_1=Button(root,text='0',font=('隶书',25),height=1,width=3,command=input_0)
button_1.place(x=190,y=340)



def input_cal():
    a=strScreen.get()
    num=len(a)
    myIndex=[]
    i=0
    while i<num:
        if (a[i]=='*')|(a[i]=='/')|(a[i]=='+')|(a[i]=='-'):
            myIndex.append(i)
        i=i+1
    print(myIndex)

    myNum=[]
    j=0
    temp1=a[0:myIndex[0]]
    temp2=a[myIndex[0]+1:len(a)]
    temp1=float(temp1)
    temp2=float(temp2)
    if a[myIndex[0]]=='*':
        temp3=temp1*temp2
    elif a[myIndex[0]]=='/':
        temp3=temp1/temp2
    elif a[myIndex[0]]=='+':
        temp3=temp1+temp2
    elif a[myIndex[0]]=='-':
        temp3=temp1-temp2
        temp3=round(temp3,2)
    strScreen.set(temp3)
    
button_1=Button(root,text='=',bg='green',font=('隶书',25),height=1,width=3,command=input_cal)
button_1.place(x=270,y=340)

root.mainloop()
