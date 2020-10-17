# Modules imported

from Tkinter import *   # For GUI
import tkMessageBox     # For GUI Popup message box
import os               # Starting file
import ttk              # better GUI
import datetime         # to create password

# Variables

details = []   # Used to store user details during login
lblines = 0    # Used to clear the listbox


# Function

'''
    For the login window
    We need to enter username and password
'''
def login():

    def check():

        details.append(un.get()) # getting the username and storing it in the list details
        details.append(pw.get()) # getting the password and storing it in the list details
        now = str(datetime.datetime.today())
        passwd = now[11:13]+now[8:10] # Creating password of the form hhdd
        if passwd != details[1]:
            tkMessageBox.showerror('ERROR','INCORRECT PASSWORD')
            login.destroy()
        else:
            login.destroy()
            EDwindow()

    login = Tk() # Window name
    pw = StringVar() # To retrieve password from password_entry
    un = StringVar() # To retrieve username from username_entry
    login.title('Login')
    login.configure(bg='slategray')
    login.geometry('240x100+530+300')
    username =Label(login,text='Username',bg='slategray',font=('Century',12),padx=10,pady=5).grid(row=0)
    username_entry = ttk.Entry(login,textvariable=un).grid(row=0,column=2)
    password = Label(login,text='Password',bg='slategray',font=('Century',12),pady=5).grid(row=1,column=0)
    password_entry = ttk.Entry(login,textvariable=pw,show='*').grid(row=1,column=2)
    login_button = ttk.Button(login,text='Login',command=check).place(x=90,y=70)
    login.mainloop() # To start the login window



def EDwindow():
    '''  The main Encryption-Decryption interface  '''

    # In the following functions the ones ending with 2 work on the DECRYPTION side
    # When '2' is not mentioned it works on the ENCRYPTION side

    def openfile():
        path = 'C:\\ED\\Newfiles\\'+var.get()+'.txt'
        f = file(path,'w+').close()
        show([])
        os.startfile(path)
        insert(path)

    def openfile2():
        path = 'C:\\ED\\Newfiles2\\'+var3.get()+'.txt'
        f = file(path,'w+').close()
        show([])
        os.startfile(path)
        insert2(path)

    def insert(path): # Inserts file to folder having files that are unencrypted
        f = open('C:\\ED\\existing1.txt','a+')
        existing = f.readlines()
        if (path+'\n') not in existing: # Inserts only if unique to avoid repetition
            f.write(path+'\n')

    def insert2(path): # Inserts file to folder having files that are encrypted
        f = open('C:\\ED\\existing2.txt','a+')
        existing = f.readlines()
        if (path+'\n') not in existing: # Inserts only if unique to avoid repetition
            f.write(path+'\n')

    def searchexisting(): # For user convenience, it provides a list of the files that are unencrypted
        os.startfile('C:\\ED\\existing1.txt')

    def searchexisting2(): # For user convenience, it provides a list of the files that are encrypted
        os.startfile('C:\\ED\\existing2.txt')

    def openexisting(): # For editing of files
        try:
            path = var2.get()
            os.startfile(path)
        except:
            tkMessageBox.showerror('ERROR','FILE NOT FOUND')

    def openexisting2(): # For editing of files
        try:
            path = var4.get()
            os.startfile(path)
        except:
            tkMessageBox.showerror('ERROR','FILE NOT FOUND')

    def NFE(): # New File Encryption
        path = 'C:\\ED\\Newfiles\\'+var.get()+'.txt'
        f = open(path)
        l = f.readlines()
        newpath = 'C:\\ED\\EncryptedFiles\\'+var.get()+'_e.txt'
        l = encrypt(l,newpath)
        insert2(newpath) # updates the record keeping of files that are of encrypted format
        show(l)

    def NFD(): # New File Decryption
        path = 'C:\\ED\\Newfiles2\\'+var3.get()+'.txt'
        f = open(path)
        l = f.readlines()
        newpath = 'C:\\ED\\DecryptedFiles\\'+var3.get()+'_d.txt'
        l = decrypt(l,newpath)
        insert(newpath) # updates the record keeping of files that are of unencrypted format
        show(l)

    def EXFE(): # EXisting File Encryption
        try:
            path = var2.get()
            newpath = ''
            # Based on the different path name types
            # we need to create final path name of encrypted file accordingly
            if 'Newfiles' in path: # for file path like: C:\ED\Newfiles\...
                # resultant path like: C:\ED\EncryptedFiles\..._d.txt
                newpath = (path[:6]+'EncryptedFiles'+path[14:]).rstrip('._edtx')+'_e.txt'
            elif 'DecryptedFiles' in path: # for file path like: C:\ED\EncryptedFiles\...
                # resultant path like: C:\ED\DecryptedFiles\..._d.txt
                newpath = (path[:6]+'EncryptedFiles'+path[20:]).rstrip('._edtx')+'_e.txt'
            else:
                tkMessageBox.showerror('ERROR','FILE NOT IDENTIFIED')
            f = open(path)
            l = f.readlines()
            l = encrypt(l,newpath)
            insert2(newpath) # updates the record keeping of files that are of encrypted format
            show(l)
        except:
            tkMessageBox.showerror('ERROR','FILE NOT FOUND')

    def EXFD(): # EXisting File Decryption
        try:
            path = var4.get()
            newpath = ''
            # Based on the different path name types
            # we need to create final path name of decrypted file accordingly
            if 'Newfiles2' in path: # for file path like: C:\ED\Newfiles2\...
                # resultant path like: C:\ED\DecryptedFiles\..._d.txt
                newpath = (path[:6]+'DecryptedFiles'+path[15:]).rstrip('._edtx')+'_d.txt'
            elif 'EncryptedFiles' in path: # for file path like: C:\ED\EncryptedFiles\...
            # resultant path like: C:\ED\DecryptedFiles\..._d.txt
                newpath = (path[:6]+'DecryptedFiles'+path[20:]).rstrip('._edtx')+'_d.txt'
            else:
                tkMessageBox.showerror('ERROR','FILE NOT IDENTIFIED')
            f = open(path)
            l = f.readlines()
            l = decrypt(l,newpath)
            insert(newpath) # updates the record keeping of files that are of unencrypted format
            show(l)
        except:
            tkMessageBox.showerror('ERROR','FILE NOT FOUND')

    def encrypt(l,path):
        ''' Algorithm for encryption, returns encrypted file as list of lines '''
        l1 = list(l)
        newlist = []
        f = open(path,'w')
        for i in l1:
            s = ''
            for j in i:
                s += chr(ord(j)+10) # changes every character
            newlist.append(s)
            f.write(s+'\n')
        return newlist

    def decrypt(l,path):
        ''' Algorithm for decryption, returns decrypted file as list of lines '''
        l1 = list(l)
        newlist = []
        f = open(path,'w')
        for i in l1:
            s = ''
            for j in i:
                s += chr(ord(j)-10) # changes every character
            newlist.append(s[:-1])
            f.write(s+'\n')
        return newlist

    def show(l):
        ''' Displays the contents of the list of lines received in the list ox accordingly '''
        global lblines # Helps in storing the number of lines in the previous listbox globally
        lb1.delete(0,lblines-1) # To clear the listbox
        lblines = len(l)
        for i in range(lblines):
            lb1.insert(i,l[i]) # Adding new lines to the listbox
        lb1.place(x=18,y=0)
        scrollbar.config(command=lb1.yview)

    def HELP():
        ''' Displays the Help file '''
        path = "C:\\ED\\help.txt"
        f = open(path)
        l = f.readlines()
        show(l)

    ed = Tk() # Window name

    #Variables used in entrybox widget to extract text
    var=StringVar()
    var2=StringVar()
    var3=StringVar()
    var4=StringVar()

    #BASIC FRAME
    scrollbar = ttk.Scrollbar(ed)
    scrollbar.pack(side=LEFT,fill=Y)
    lb1 = Listbox(ed,height=46,width=100,bg='light steel blue',selectmode=EXTENDED,yscrollcommand=scrollbar.set)
    logo = Label(ed,text='KCAS',font=('Magneto',50),bg='slate gray',fg='firebrick').place(x=890,y=10)
    usn = Label(ed,text=('USERNAME:'+details[0]),font=('Consolas',14),bg='slate gray',fg='dark orange').place(x=630,y=710)
    enheading = Label(ed,text='ENCRYPTION',bg='slate gray',font=('Century Gothic',30),fg='SlateBlue4').place(x=630,y=120)

    #CREATE NEW FILE
    l1 = Label(ed,text='Enter new file name: ',font=('',18),bg='slate gray').place(x=630,y=200)
    e1 = ttk.Entry(ed,textvariable=var,font=('',18)).place(x=865,y=200)
    helpl1 = Label(ed,text='Don\'t forget to save the file :)',bg='slate gray',fg='white').place(x=920,y=233)
    b1 = ttk.Button(ed,text='Open',command=openfile).place(x=1145,y=205)
    b2 = ttk.Button(ed,text='Encrypt',command=NFE).place(x=1237,y=205)

    #OPEN EXISTING FILE
    l2 = Label(ed,text='Open an existing file: ',font=('',18),bg='slate gray').place(x=630,y=265)
    e2 = ttk.Entry(ed,textvariable=var2,font=('',18)).place(x=865,y=265)
    b3 = ttk.Button(ed,text='Edit',command=openexisting).place(x=1145,y=265)
    b4 = ttk.Button(ed,text='...',command=searchexisting).place(x=1237,y=265)

    #ENCRYPT BUTTON FOR EXISTING FILE
    encb = Button(ed,text='ENCRYPT FILE',bg='green',fg='black',width=92,command=EXFE).place(x=650,y=310)

    # Separator label between Encryption and Decryption sections
    seplabel = Label(ed,text=('_'*140),bg='slate gray').place(x=625,y=370)
    decheading = Label(ed,text='DECRYPTION',bg='slate gray',font=('Century Gothic',30),fg='SlateBlue4').place(x=630,y=420)

    #CREATE NEW ENCRYPTED FILE
    l3 = Label(ed,text='Enter new file name: ',font=('',18),bg='slate gray').place(x=630,y=500)
    e3 = ttk.Entry(ed,textvariable=var3,font=('',18)).place(x=865,y=500)
    helpl1 = Label(ed,text='Don\'t forget to save the file :)',bg='slate gray',fg='white').place(x=920,y=533)
    b5 = ttk.Button(ed,text='Open',command=openfile2).place(x=1145,y=505)
    b6 = ttk.Button(ed,text='Decrypt',command=NFD).place(x=1237,y=505)

    #OPEN EXISTING ENCRYPTED FILE
    l4 = Label(ed,text='Open an existing file: ',font=('',18),bg='slate gray').place(x=630,y=565)
    e4 = ttk.Entry(ed,textvariable=var4,font=('',18)).place(x=865,y=565)
    b7 = ttk.Button(ed,text='Edit',command=openexisting2).place(x=1145,y=565)
    b8 = ttk.Button(ed,text='...',command=searchexisting2).place(x=1237,y=565)

    #DECRYPT BUTTON FOR EXISTING FILE
    decb = Button(ed,text='DECRYPT FILE',bg='green',fg='black',width=92,command=EXFD).place(x=650,y=610)

    helpbutton = Button(ed,text='?',font=('Colonna MT',20),bg='yellow',command=HELP).place(x=1315,y=680)

    ed.state('zoomed') # To open window in full screen mode
    ed.configure(bg='slate gray')
    ed.title('ENCRYPTION-DECRYPTION WINDOW')
    ed.mainloop()

# Start the program
login()
