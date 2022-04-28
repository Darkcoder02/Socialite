#from tkinter import *
import tkinter as tk
from tkinter import ttk;
from PIL import Image, ImageTk

import mysql.connector as mysql

pw ='guitarboard'
connection = mysql.connect(
    host = 'localhost',
    username = 'root',
    password = pw,
    database = 'socialitedb'
)
cursor = connection.cursor()


root = tk.Tk()
root.state("zoomed")
root.title('SocialiteDB')
root['bg']='white'
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

# data structures
users = []
contacts = []
names = ""
groups = []

def show_frame(frame):
    #To show the selected frame
    frame.tkraise()
    distroy_frame(frame)
    
def button_login(name, phone, cursor, users):
    name_text = name.get()
    phone_text = phone.get()
    #bio_text = bio.get()
    query = "select uid from User where phone_number = %s and name = '%s'"%(phone_text,name_text) #Akshit Kumar 1000000000
    cursor.execute(query)
    data = cursor.fetchall()
    users.append(data[0][0])
    show_frame(frame3)

def button_contacts(name, phone, cursor, names):
    global contacts
    name_text = name.get()
    phone_text = phone.get()
    #bio_text = bio.get()
    query1 = "select contact_person_id, saved_by_name from Contacts where user_id = %s"%(users[0])
    cursor.execute(query1)
    data = cursor.fetchall()
    #print(data)
    
    contacts.clear()
    
    for i in data:
        if (i[1] == None):
            query2 = "select phone_number from User where uid = %s"%(i[0])
            cursor.execute(query2)
            data2 = cursor.fetchall()
            #print(data2)
            contacts.append(str(int(data2[0][0])))
        else:
            # contacts.append(i[1])
            contacts.append([i[0], i[1]])
    # print(contacts)
    buttons = []
    for i in range(len(contacts)):
        n = i + 7
        framen = tk.Frame(root, bg="#1B453D")
        framen.grid(row=0, column=0, sticky='nsew')
        buttons.append(tk.Button(frame4, text = contacts[i][1], font=("Helvetica", 16, "bold"), bg="#32CD32", fg="black", height=1, width=15,command=lambda i=i:contact_frames(framen,i,contacts)).place(relx=0.445,rely=(i*0.05)+0.15))
        
        message_label = tk.Label(framen, text = "Message", bg="#235347", fg="black", height=2, width=10)
        message_label.configure(font=("Helvetica", 20, "bold"), anchor=tk.CENTER)
        message_label.place(relx = 0.46, rely = 0.05)
        
        sent_label = tk.Label(framen, text = "Sent", bg="#235347", fg="black", height=1, width=15)
        sent_label.configure(font=("Helvetica", 20, "bold"))
        sent_label.place(relx = 0.3, rely = 0.2)
        
        
        received_label = tk.Label(framen, text = "Recieved", bg="#235347", fg="black", height=1, width=15)
        received_label.configure(font=("Helvetica", 20, "bold"))
        received_label.place(relx = 0.6, rely = 0.2)
        
    framen_button_Back = tk.Button(framen, text="Back", command=lambda:show_frame(frame4), bg="gray", fg="Black", height=1, width=5)
    framen_button_Back.configure(font=("Helvetica", 16, "bold"))
    framen_button_Back.grid(row = 0, column = 0)
        
    show_frame(frame4)

def contact_frames(frame,i,contacts):
    show_frame(frame)
    contact_id = contacts[i][0]
    load_messages_individual(contact_id,frame)

def load_messages_individual(contact_id,frame):
    text_widget_1 = tk.Text(frame, height=7, width=50)
    text_widget_2 = tk.Text(frame, height=7, width=50)
    message_label = tk.Label(frame, text = "Message", bg="#235347", fg="black", height=2, width=15)
    message_label.configure(font=("Helvetica", 20, "bold"))
    message_label.place(relx = 0.44, rely = 0.05)
    phone_text = phone.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    users.append(data1[0][0])
    #users = users[-1]
    #print(users)
    
    contact = contact_id
    #print(contact)
    query_check = "Select contact_person_id from contacts where user_id = %s"%(users[0])
    cursor.execute(query_check)
    data_check = cursor.fetchall()

    #print("check", data_check)
    for i in data_check:
        #print(i[0])
        #print(contact)
        if str(i[0]) == str(contact):
            #print(i[0])
            #print("True condition")
            show_frame(frame)
            break
    
    # message by user
    query2 = """SELECT M.mssg_id, M.message_body, M.sender_id, M.time, M.date
    FROM message as M, message_recipient as R
    WHERE (M.sender_id = %s)
    AND (R.receiver_id = %s)
    AND (receiver_group_id is null)
    AND (M.mssg_id=R.mssg_id)"""%(users[0], contact)

    cursor.execute(query2)
    data2 = cursor.fetchall()
    #print(data2)
    
    # message by contact
    query3 = """SELECT M.mssg_id, M.message_body, M.sender_id, M.time, M.date
    FROM message as M, message_recipient as R
    WHERE (M.sender_id = %s)
    AND (R.receiver_id = %s)
    AND (receiver_group_id is null)
    AND (M.mssg_id=R.mssg_id)"""%(contact, users[0])

    cursor.execute(query3)
    data3 = cursor.fetchall()
    #print(data3)
    
    received = ""
    for i in data3:
        #print(i[4])
        received = received + str(i[4]) + "\t" + str(i[3]) + "\n" + str(i[1]) + "\n"
    #print(sent[:-1])
    received = received[:-1]
    
    print(received)
    sent = ""
    for i in data2:
        #print(i[4])
        sent = sent + str(i[4]) + "\t" + str(i[3]) + "\n" + str(i[1]) + "\n"
    #print(sent[:-1])
    sent = sent[:-1]

    text_widget_1.place(relx = 0.25,rely=0.3)
    text_widget_1.insert(tk.END, received)    
    
    text_widget_2.place(relx = 0.55,rely=0.3)
    text_widget_2.insert(tk.END, sent)


def button_profile(name, phone, cursor, users):
    name_text = name.get()
    phone_text = phone.get()
    #bio_text = bio.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    users.clear()
    users.append(data1[0][0])
    #print(users)
    
    query2 = "CREATE VIEW user_profile AS SELECT name, phone_number, bio FROM user WHERE uid = %s"%(users[0])
    cursor.execute(query2)
    
    query2 = "select * from user_profile"
    cursor.execute(query2)
    data3 = cursor.fetchall()
    #print(data3)
    
    query4 = "DROP VIEW user_profile"
    cursor.execute(query4)
    
    frame5_label_Profile_name = tk.Label(frame5, text = "Name: " + data3[0][0], font=("Helvetica", 16, "bold"), bg="#93C572", fg="#123524", height=1, width=30)
    frame5_label_Profile_name.place(relx = 0.4,rely = 0.2)

    frame5_label_Profile_phone = tk.Label(frame5, text = "Phone: " + str(int(data3[0][1])), font=("Helvetica", 16, "bold"), bg="#93C572", fg="#123524", height=1, width=30)
    frame5_label_Profile_phone.place(relx = 0.4,rely = 0.25)

    frame5_label_Profile_bio = tk.Label(frame5, text = "Bio: \n" + data3[0][2], font=("Helvetica", 16, "bold"), bg="#93C572", fg="#123524", height=2, width=30)
    frame5_label_Profile_bio.place(relx = 0.4,rely = 0.31)

    show_frame(frame5)
    
def button_groups(name, phone, cursor, users):
    pass
    name_text = name.get()
    phone_text = phone.get()
    #bio_text = bio.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    users.clear()
    users.append(data1[0][0])
    #print(users)
    
    query2 = "select group_id from user_group_info where user_id = %s"%(users[0])
    cursor.execute(query2)
    data2 = cursor.fetchall()
    #print(data2)
    
    groups.clear()
    for i in data2:
        #print(i[0])
        query3 = "SELECT group_name FROM grp Where group_id = %s"%(i[0])
        cursor.execute(query3)
        data3 = cursor.fetchall()
        #print(data3)
        groups.append(data3[0][0])
    
    for i in range(len(groups)):
        pass
        x = i + 7
        framex = tk.Frame(root, bg="#1B453D")
        framex.grid(row=0, column=0, sticky='nsew')
        frame6_button_Namesi = tk.Button(frame6, text = groups[i], bg="gray", fg="black", height=1, width=15,command=lambda:show_frame(framex))
        frame6_button_Namesi.configure(font=("Helvetica", 16, "bold"))
        frame6_button_Namesi.grid(row = i+1, column = 1)
        frame6_button_Namesi.place(relx=0.445,rely=(i*0.05)+0.15)
        
        message_label = tk.Label(framex, text = "Message", bg="#235347", fg="black", height=2, width=15)
        message_label.configure(font=("Helvetica", 20, "bold"))
        message_label.place(relx = 0.44, rely = 0.05)
        
        framen_button_Back = tk.Button(framex, text="Back", command=lambda:show_frame(frame6),font=("Helvetica", 16, "bold"), bg="grey", fg="black", height=1, width=5)
        framen_button_Back.grid(row = 0, column = 0)
    
    show_frame(frame6)
 
def distroy_frame(frame):
    exit_button = tk.Button(frame, text="Exit", font = ("Helvetica",20,"bold"), command=root.destroy)
    exit_button.place(relx=0.949,rely=0)

#frames
frame1 = tk.Frame(root, bg="#1B453D")
frame2 = tk.Frame(root, bg="#1B453D")
frame3 = tk.Frame(root, bg="#1B453D")
frame4 = tk.Frame(root, bg="#1B453D")
frame5 = tk.Frame(root, bg="#1B453D")
frame6 = tk.Frame(root, bg="#1B453D")
# frame6 = Frame(root, bg="#1B453D")

for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
    frame.grid(row=0, column=0, sticky='nsew')

show_frame(frame1)

# Frame1: Landing page
logo1 = Image.open('Applogo.png')
logo1 = ImageTk.PhotoImage(logo1)
frame1_logo = tk.Label(frame1, image=logo1)
frame1_logo.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)

frame1_button_register = tk.Button(frame1, text="Ready To Chat!", command=lambda:show_frame(frame2), bg="#32CD32", fg="black", height=2, width=20)
frame1_button_register.configure(font=("Helvetica", 18, "bold"))
frame1_button_register.place(relx = 0.5, rely = 0.8, anchor=tk.CENTER)


# Frame2: Login page
frame2_label_register = tk.Label(frame2, text = "Login", bg="#A9A9A9", fg="white", height=2, width=15)
frame2_label_register.configure(font=("Helvetica", 15, "bold"))
frame2_label_register.place(relx = 0.5, rely = 0.4, anchor=tk.CENTER)

frame2_logo = tk.Label(frame2, image=logo1)
frame2_logo.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)

name = tk.StringVar()
frame2_label_name = tk.Label(frame2, text="Name:", bg="#235347", fg="white", height=1, width=10)
frame2_label_name.place(relx = 0.35, rely = 0.7, anchor=tk.CENTER)
frame2_label_name.configure(font=("Helvetica", 16, "bold"))
frame2_input_name = tk.Entry(frame2, textvariable = name).place(relx = 0.46, rely = 0.7, anchor=tk.CENTER)

phone = tk.StringVar()
frame2_label_phone = tk.Label(frame2, text="Phone:", bg="#235347", fg="white", height=1, width=10)
frame2_label_phone.configure(font=("Helvetica", 16, "bold"))
frame2_label_phone.place(relx = 0.35, rely = 0.77, anchor=tk.CENTER)
frame2_input_phone = tk.Entry(frame2, textvariable = phone).place(relx = 0.46, rely = 0.77, anchor=tk.CENTER)

frame2_button_after_login = tk.Button(frame2, text="Login", command=lambda:button_login(name, phone, cursor, users),bg="#235347", fg="Black", height=1, width=15)
frame2_button_after_login.configure(font=("Helvetica", 16, "bold"))
frame2_button_after_login.place(relx = 0.5, rely = 0.85, anchor=tk.CENTER)

# Frame3: Menu page
frame3_label_Menu = tk.Label(frame3, text = "Menu", bg="#1B453D", fg="white", height=2, width=15)
frame3_label_Menu.configure(font=("Helvetica",25, "bold"))
frame3_label_Menu.place(relx = 0.5, rely = 0.03, anchor=tk.CENTER)

frame3_logo = tk.Label(frame3, image=logo1)
frame3_logo.place(relx = 0.5, rely = 0.39,anchor=tk.CENTER)

frame3_button_Contacts = tk.Button(frame3, text="Contacts", command=lambda: button_contacts(name, phone, cursor, names), bg="#32CD32", fg="black", height=1, width=15)
frame3_button_Contacts.place(relx = 0.44,rely = 0.8)
frame3_button_Contacts.configure(font=("Helvetica",20, "bold"))
                            
frame3_button_profile = tk.Button(frame3, text="Profile", command=lambda: button_profile(name, phone, cursor, users), bg="#32CD32", fg="black", height=1, width=15)
frame3_button_profile.place(relx = 0.24,rely = 0.8)
frame3_button_profile.configure(font=("Helvetica",20, "bold"))

frame3_button_Groups = tk.Button(frame3, text="Groups", command=lambda: button_groups(name, phone, cursor, users), bg="#32CD32", fg="Black", height=1, width=15)
frame3_button_Groups.place(relx = 0.64,rely = 0.8)
frame3_button_Groups.configure(font=("Helvetica",20, "bold"))


# Frame4: Contacts page 
frame4_label_Contacts = tk.Label(frame4, text = "Contacts",font=("Helvetica",20, "bold"), bg="#235347", fg="black", height=2, width=15)
frame4_label_Contacts.place(relx = 0.44,rely = 0.05)

frame4_button_Back = tk.Button(frame4, text="Back", command=lambda: show_frame(frame3),font=("Helvetica",16, "bold"), bg="gray", fg="Black", height=1, width=5)
frame4_button_Back.grid(row = 0, column = 0)

# Frame5: Profile page
frame5_label_Profile = tk.Label(frame5, text = "Profile", font=("Helvetica",20, "bold"), bg="#93C572", fg="#123524", height=2, width=15)
frame5_label_Profile.place(relx = 0.43,rely=0.07)

frame5_button_Back = tk.Button(frame5, text="Back", command=lambda: show_frame(frame3),font=("Helvetica",17, "bold"), bg="gray", fg="Black", height=1, width=5)
frame5_button_Back.grid(row = 0, column = 0)

# Frame6: Groups page
frame6_label_Groups = tk.Label(frame6, text = "Groups", bg="#235347", fg="black", height=2, width=15)
frame6_label_Groups.place(relx = 0.44,rely = 0.05)
frame6_label_Groups.config(font = ("Helvetica",20,"bold"))

frame6_button_Back = tk.Button(frame6, text="Back", command=lambda: show_frame(frame3),font=("Helvetica",17, "bold"), bg="grey", fg="Black", height=1, width=5)
frame6_button_Back.grid(row = 0, column = 0)

exit_button = tk.Button(root, text="Exit", font = ("Helvetica",20,"bold"), command=root.destroy)
exit_button.place(relx=0.949,rely=0)

root.mainloop()