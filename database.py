from tkinter import *
import sqlite3
import farm_main
import user_signin
import translate

#function to register the users
def users():

    u = Toplevel()
    u.resizable(0, 0)
    def insert():
        a = []
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("SELECT email from user")
        for i in c.fetchall():
            a.append(i[0])
        if (email.get() in a):
            error_label = Label(u, text='Email already registered.', font=('Calibri', 15))
            error_label.place(x=228, y=319)
            conn.commit()
            conn.close()

        else:
            c.execute("INSERT INTO user VALUES (:name, :email, :number, :password, :address)", {
                    'name': name.get(),
                    'email': email.get(),
                    'number': number.get(),
                    'password': password.get(),
                    'address': address.get()
            })
            conn.commit()
            conn.close()
            # clearing the entries
            name.delete(0, END)
            email.delete(0, END)
            number.delete(0, END)
            password.delete(0, END)
            address.delete(0, END)

            # displaying
            result_label = Label(u, text='Registered, Head over to Sign-in!', font=('Calibri', 15))
            result_label.place(x=228, y=319)

    u.geometry('637x455+364+137')
    bg = PhotoImage(file=r"image\buy.png")
    label = Label(u, image=bg)
    label.place(x=-182, y=0)
    title_label = Label(u, text='ENTER YOU DETAILS BELOW', font=('Calibri', 18), bg='#eeede8', fg='black')
    title_label.place(x=337, y=18)
    name_label = Label(u, text="Name", font=('Calibri', 14), bg='#eeede8', fg="black")
    name_label.place(x=319, y=91)
    email_label = Label(u, text="Email", font=('Calibri', 14), bg='#eeede8', fg="black")
    email_label.place(x=319, y=127)
    number_label = Label(u, text="Number", font=('Calibri', 14), bg='#eeede8', fg="black")
    number_label.place(x=319, y=164)
    pw_label = Label(u, text="Password", font=('Calibri', 14), bg='#eeede8', fg="black")
    pw_label.place(x=319, y=218)
    address_label = Label(u, text="Address", font=('Calibri', 14), bg='#eeede8', fg="black")
    address_label.place(x=319, y=245)

    # Entries
    name = Entry(u, width=27)
    name.place(x=410, y=91)
    email = Entry(u, width=27)
    email.place(x=410, y=127)
    number = Entry(u, width=27)
    number.place(x=410, y=164)
    password = Entry(u, width=27, show='*')
    password.place(x=410, y=218)
    address = Entry(u, width=27)
    address.place(x=410, y=245)

    sub = Button(u, text="Register", width=15, command=insert)
    sub.place(x=437, y=273)
    u.mainloop()
    
#function to register the farmers
def farmers():

    f = Toplevel()
    f.geometry('729x546+364+91')
    f.config(bg='#e7c7a9')
    f.resizable(0, 0)
    far = PhotoImage(file=r"image\zz.png")
    label_f = Label(f, image=far)
    label_f.place(x=0, y=-195)
    def insert():
        e = []
        conn = sqlite3.connect('farmer.db')
        c = conn.cursor()
        c.execute("SELECT email from farmer")
        for i in c.fetchall():
            e.append(i[0])
        if (email.get() in e):
            error_label = Label(f, text='Email already registered.', font=('Calibri', 14), bg='#ecfbfc')
            error_label.place(x=364, y=127)
            conn.commit()
            conn.close()

        else:
            c.execute("INSERT INTO farmer VALUES (:name, :email, :number, :password, :location, :pref_lang)", {
                    'name': name.get(),
                    'email': email.get(),
                    'number': number.get(),
                    'password': password.get(),
                    'location': radio.get(),
                    'pref_lang': str(drop.get())
            })
            conn.commit()
            conn.close()
            # clearing the entries
            name.delete(0, END)
            email.delete(0, END)
            number.delete(0, END)
            password.delete(0, END)

            # displaying
            result_label = Label(f, text='Registered, Head over to Sign-in!', font=('Calibri', 15))
            result_label.place(x=228, y=455)

    f.geometry("750x550")
    f.configure(bg='#ffffff')
    #Title Text
    title = Label(f, text="ENTER THE DETAILS BELOW", font=('Calibri', 18), bg='white', fg='black')
    title.place(x=80, y=18)

    #Translate array
    array_trans = ['Name', 'Email', 'Number', 'Password', 'Location', 'Preferred Language']

    #labels
    name_label = Label(f, text=array_trans[0], font=('Calibri', 14), bg='white', fg='black')
    name_label.place(x=91, y=91)
    email_label = Label(f, text=array_trans[1], font=('Calibri', 14), bg='white', fg='black')
    email_label.place(x=91, y=127)
    number_label = Label(f, text=array_trans[2], font=('Calibri', 14), bg='white', fg='black')
    number_label.place(x=91, y=164)
    pw_label = Label(f, text=array_trans[3], font=('Calibri', 14), bg='white', fg='black')
    pw_label.place(x=91, y=190)
    radio_label = Label(f, text=array_trans[4], font=('Calibri', 14), bg='white', fg='black')
    radio_label.place(x=91, y=220)
    drop_label = Label(f, text=array_trans[5], font=('Calibri', 14), bg='white', fg='black')
    drop_label.place(x=27, y=337)

    #Entries
    name = Entry(f, width=27)
    name.place(x=182, y=91)
    email = Entry(f, width=27)
    email.place(x=182, y=127)
    number = Entry(f, width=27)
    number.place(x=182, y=164)
    password = Entry(f, width=27, show='*')
    password.place(x=182, y=190)

    radio = StringVar(f)
    radio.set("Bijapur")
    bijapur = Radiobutton(f, text="Bijapur", variable=radio, value='Bijapur', bg='white', fg='black')
    bijapur.place(x=182, y=220)
    bang_rural = Radiobutton(f, text="Bangalore Rural", variable=radio, value='Bangalore Rural', bg='white', fg='black')
    bang_rural.place(x=182, y=280)
    udupi = Radiobutton(f, text="Udupi", variable=radio, value='Udupi', bg='white', fg='black')
    udupi.place(x=182, y=250)

    drop = StringVar(f)
    OptionList = ["English", "ಕನ್ನಡ", "हिंदी"]
    drop.set(OptionList[0])
    dropdown = OptionMenu(f, drop, *OptionList)
    dropdown.config(width=10, font=('monospace', 10), fg="black")
    dropdown.place(x=182, y=337)

    drop_t = StringVar(f)
    Option = ["English", "ಕನ್ನಡ", "हिंदी"]
    drop_t.set(OptionList[0])
    dropdown_t = OptionMenu(f, drop_t, *Option)
    dropdown_t.config(width=10, font=('monospace', 10), fg="black")
    dropdown_t.place(x=546, y=18)

    def tran():
        if drop_t.get() == 'ಕನ್ನಡ':
            new_array = translate.trans(array_trans, 'en', 'kn')
            name_label.configure(text=new_array[0].text)
            email_label.configure(text=new_array[1].text)
            number_label.configure(text=new_array[2].text)
            pw_label.configure(text=new_array[3].text)
            radio_label.configure(text=new_array[4].text)
            drop_label.configure(text=new_array[5].text)
        elif drop_t.get() == "हिंदी":
            new_array = translate.trans(array_trans, 'en', 'hi')
            name_label.configure(text=new_array[0].text)
            email_label.configure(text=new_array[1].text)
            number_label.configure(text=new_array[2].text)
            pw_label.configure(text=new_array[3].text)
            radio_label.configure(text=new_array[4].text)
            drop_label.configure(text=new_array[5].text)
        else:
            name_label.configure(text=array_trans[0])
            email_label.configure(text=array_trans[1])
            number_label.configure(text=array_trans[2])
            pw_label.configure(text=array_trans[3])
            radio_label.configure(text=array_trans[4])
            drop_label.configure(text=array_trans[5])


    trans_button = Button(f, text='Translate', width=13, command=tran)
    trans_button.place(x=605, y=60)
    sub = Button(f, text="Register", command=insert, width=10)
    sub.place(x=137, y=419)

    f.mainloop()

def signin():
    sign_window = Toplevel()
    sign_window.title("SIGN IN")
    sign_window.geometry("410x364+455+182")
    sign_window.configure(bg='#ecfbfc')
    sign_window.resizable(0, 0)
    def farm_window():
        em = email.get()
        e = []
        n = []
        l = []
        num = []
        pref_l = []
        conn = sqlite3.connect('farmer.db')
        c = conn.cursor()
        c.execute("SELECT email, name, location, number, pref_lang FROM farmer")
        for i in c.fetchall():
            e.append(i[0])
            n.append(i[1])
            l.append(i[2])
            num.append(i[3])
            pref_l.append(i[4])
        conn.commit()
        conn.close()
        sign_window.destroy()
        for x in range(0, len(e)):
            if(em==e[x]):
                name = n[x]
                location = l[x]
                number = num[x]
                pref_lan = pref_l[x]
        farm_main.f(name, location, em, number, pref_lan)


    def farm_window_check():
        e = []
        p = []
        em = email.get()
        pw = password.get()
        conn = sqlite3.connect('farmer.db')
        c = conn.cursor()
        c.execute("SELECT email,password FROM farmer")
        for i in c.fetchall():
            e.append(i[0])
            p.append(i[1])
        conn.commit()
        conn.close()
        for i in range(0, len(e)):
            if em == e[i]:
                if pw == p[i]:
                    farm_window()
                    break

                else:
                    error_msg = Label(sign_window, text="Invalid Password", font=('monospace', 14), bg="#FCF3CF", fg="black")
                    error_msg.place(x=137, y=340)
            else:
                error_m = Label(sign_window, text="Email not registered.", font=('monospace', 12), bg="#FCF3CF", fg="black")
                error_m.place(x=137, y=340)

    # function to open the main page
    def buyer_window():
        em = email.get()
        e = []
        n = []
        a = []
        num = []
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("SELECT email, name, address, number FROM user")
        for i in c.fetchall():
            e.append(i[0])
            n.append(i[1])
            a.append(i[2])
            num.append(i[3])
        conn.commit()
        conn.close()
        sign_window.destroy()
        for x in range(0, len(e)):
            if (em == e[x]):
                name = n[x]
                location = a[x]
                number = num[x]
        user_signin.page1(name, location, em, number)

    # functions checks the email and password before opening main page
    def buyer_window_check():
        em = []
        pw = []
        ema = email.get()
        pwd = password.get()
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("SELECT email,password FROM user")
        for i in c.fetchall():
            em.append(i[0])
            pw.append(i[1])
        conn.commit()
        conn.close()
        for i in range(0, len(em)):
            if ema == em[i]:
                if pwd == pw[i]:
                    buyer_window()
                    break
                else:
                    error_msg = Label(sign_window, text="Invalid Password", font=('monospace', 14), bg="#FCF3CF", fg="black")
                    error_msg.place(x=137, y=340)
            else:
                error_m = Label(sign_window, text="Email not registered.", font=('monospace', 12), bg="#FCF3CF", fg="black")
                error_m.place(x=137, y=340)

    # Background image for sign-in
    canvas=Canvas(sign_window)
    farm = PhotoImage(file=r"image\smalls.png")
    farm = farm.subsample(1, 1)
    canvas.create_image(270, 50, image=farm)

    # labels
    email_label = canvas.create_text(55, 59, text="Email", font=('monospace', 14), fill="white")
    pw_label = canvas.create_text(59, 127, text="Password", font=('monospace', 14), fill="white")

    # Entries
    email = Entry(sign_window, width=18, font=('monospace', 13))
    email.place(x=137, y=46)
    password = Entry(sign_window, show="*", width=18, font=('monospace', 13))
    password.place(x=137, y=118)

    # Submit button
    Submit_button = Button(sign_window, text="Submit as farmer", font=('monospace', 12) , width=15, height=0, bg="white", command=farm_window_check)
    Submit_button.place(x=137, y=209)
    Sub_button = Button(sign_window, text="Submit as buyer", font=('monospace', 12), width=15, height=0, bg="white", command=buyer_window_check)
    Sub_button.place(x=137, y=264)
    canvas.pack(expand=TRUE, fill="both")
    sign_window.mainloop()