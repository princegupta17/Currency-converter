#startng with importing  for library for using tkinter  

from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()#defineing root  to start the GUI

#setting the geometry screen
root.geometry("1300x700")                                                                                                                                                                                                     


#Adding lable heading 
z=Label(root,text="Currency Converter", bg="black", fg="yellow",padx=644, pady=10, font=("comicsansns",20), borderwidth=10, relief=RIDGE,bd=5)
z.grid()#packing the heading


def help():
    
    
    '''this function is defined to help the user to know how to use the app'''
    
    value=tmsg.askquestion("we will help you","click 'yes' for help")
    if value=="yes":#this function happen if user click on yes button then code willl explain how to use the GUI
        msg="The app works in following steps \n 1. select the currency from Dropbox you want to convert. \n 2. select the currency from Drop box in  which you want the input amount \n 3. then enter the amount you need to convert \n 4. click on the 'convert' button \n"
    else:
        msg="Give us your feedback !!!"#if user dont need help We will ask for rating to our GUI
    tmsg.showinfo("Help", msg)

def rate():
    '''this function is defined which help the user to give rating to our GUI'''
    value=tmsg.askquestion("was your experience Good?","You used this GUI...Was your experience Good?")
    if value=="yes":
        with open("rate.txt", "a") as f:
            f.write(value)
    else:
        with open("rate.txt", "a") as f:
            f.write(value)
     
# creating label for ffrom currency ,to currency ,amount,result
youhave=Label(root,text="From Currency:", font="APRAJITA 18 bold")
youwant=Label(root,text="To Currency:", font="APRAJITA 18 bold")
amount=Label(root,text="Enter Amount:", font="APRAJITA 18 bold")
result=Label(root,text="Amount in:", font="APRAJITA 18 bold")
    
#placing the label at appropiate place    
youhave.place(x=450, y=80)
youwant.place(x=450,y=120)
amount.place(x=450,y=160)
result.place(x=450,y=250)

#defing the list from where user can select the currecies
currency=['countrycurrency',
'ARS',
'AUD',
'BHD',
'BWP',
'BRL',
'BGN',
'CAD',
'CLP',
'CNY',
'COP',
'CZK',
'DKK',
'EUR',
'HKD',
'HUF',
'ISK',
'IDR',
'IRR',
'ILS',
'INR',
'JPY',
'KZT',
'KWD',
'LYD', 
'MYR', 
'MUR', 
'MXN', 
'NPR', 
'NZD', 
'NOK',
'OMR', 
'PKR', 
'PHP', 
'PLN',
'QAR', 
'RON', 
'RUB', 
'SAR', 
'SGD', 
'ZAR', 
'LKR', 
'TWD', 
'THB', 
'TTD',
'TRY',
'USD', 
'VEF']

# creating the type of inputs GUI will take in the entry boxes
youhavevalue=StringVar()
youhavevalue.set(currency[0])
youwantvalue=StringVar()
youwantvalue.set(currency[0])
amountvalue=DoubleVar()
resultvalue=IntVar()

# creating the optionmenu, entry boxes
youhaveentry=OptionMenu(root, youhavevalue, *currency)
youhaveentry.config(width=50,bd=4)
youwantentry=OptionMenu(root, youwantvalue, *currency)
youwantentry.config(width=50,bd=4)
amountentry=Entry(root,textvariable= amountvalue,bd=5,width=50)
resultentry=Entry(root,textvariable=resultvalue,bd=5,width=50)
 
 # placing the optionmenu and entry box   
youhaveentry.place(x=780,y=80)
youwantentry.place(x=780,y=120)
amountentry.place(x=780,y=160)
resultentry.place(x=780,y=260)





def convert():
    '''this function will open a file compare.txt where the data is stored for a particular date and then it will convert the amount '''

    F1=open('compare.txt','r')
    f=F1.readlines()
    rupee_exchange_rate={}
    for i in f:
        m=i.split()
        rupee_exchange_rate[m[0]]=float(m[1])
        
        
        
    from_currency=(youhavevalue.get())
    t=rupee_exchange_rate[from_currency]
    to_currency=(youwantvalue.get())
    u=(1/rupee_exchange_rate[to_currency])
    
    
    
    e=float(t) * float(amountvalue.get()) * float(u)#multiplying the amount to req. number taken from file
    e=round(e,4)
    e = '{:,}'.format(e)
    resultentry.insert(0,f'{e}')
    
    status.set("Converting currency...")
    sbar.update()
    import time
    time.sleep(0.2)
    status.set("Ready")
    
       

def clear():
    '''this function is defined to tell the instruction to the clear button and running the sbar'''
    amountentry.delete(0,END)
    resultentry.delete(0,END)
    
    status.set("Clearing...")
    sbar.update()
    import time
    time.sleep(0.2)
    status.set("Ready")

# creating the buttons for convert and cleara
Button(text="convert", font="APRAJITA 18 bold", bg="grey", command=convert,width=10,bd=4).place(x=665,y=200)
Button(text="clear", font="APRAJITA 18 bold", bg="grey", command=clear,width=10,bd=5).place(x=665,y=300)

# creating the menu bars for help and rate

#for help   
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="help",command=help)
mainmenu.add_cascade(label="Help",menu=m1)

#for rate
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Rate us",command=rate)
mainmenu.add_cascade(label="Rate us",menu=m2)
root.config(menu=mainmenu)


# creating sbar and placing it  
status=StringVar()
status.set("Ready")
sbar=Label(root,textvariable=status,relief=SUNKEN,anchor='w', padx=750)
sbar.place(x=0,y=700)


#giving title to our GUI
root.title("GE103 PROJECT")
#using.mainloop to pack aal over GUI
root.mainloop()