
from tkinter import *
from tkinter import ttk;
from PIL import Image, ImageTk

import mysql.connector as mysql

pw = 'guitarboard'
connection = mysql.connect(
    host = 'localhost',
    username = 'root',
    password = pw,
    database = 'socialitedb'
)
cursor = connection.cursor()


root = Tk()
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


def button_login(name, phone, cursor, users):
    name_text = name.get()
    phone_text = phone.get()
    #bio_text = bio.get()
    query = "select uid from User where phone_number = %s"%(phone_text)
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
            contacts.append([i[0], str(int(data2[0][0]))])
        else:
            contacts.append([i[0], i[1]])
    #print(contacts)
    
    result = ""
    for i in range(len(contacts)):
        #print(contacts[i])
        result = result + str(contacts[i][0]) + ": " + contacts[i][1] + "\n"
        
    result = result[:-1]
    #print(result)
    
    frame4_label_Display = Label(frame4, text = result, font="Raleway", bg="white", fg="black", height=10, width=15)
    frame4_label_Display.grid(row = 1, column = 1)
    
    show_frame(frame4)

def load_messages_individual(contact_id):
    phone_text = phone.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    users.append(data1[0][0])
    #users = users[-1]
    #print(users)
    
    contact = contact_id.get()
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
            show_frame(frame7)
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
        received = received + str(i[4]) + "; " + str(i[3]) + "-> " + str(i[1]) + "\n"
    #print(sent[:-1])
    received = received[:-1]
    
    sent = ""
    for i in data2:
        #print(i[4])
        sent = sent + str(i[4]) + "; " + str(i[3]) + "-> " + str(i[1]) + "\n"
    #print(sent[:-1])
    sent = sent[:-1]

    frame7_label_MessageRecieved = Label(frame7, text = received, font="Raleway", bg="white", fg="black", height=10, width=40)
    frame7_label_MessageRecieved.grid(row = 1, column = 1)
    
    frame7_label_MessageSent = Label(frame7, text = sent, font="Raleway", bg="white", fg="#32CD32", height=10, width=40)
    frame7_label_MessageSent.grid(row = 1, column = 3)
    
def create_message_individual(contact_id, MessageIndi):
    phone_text = phone.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    #users.append(data1[0][0])
    #users = users[-1]
    print(users)
    
    contact = contact_id.get()
    #print(contact)
    
    message = MessageIndi.get()
    print(message)
    
    from datetime import date
    today = date.today()
    date = today.strftime("%Y-%m-%d")
    print("date =", date)
    
    from datetime import datetime
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print("Time =", str(time))
    
    query2 = """INSERT INTO message(sender_id, message_body, time, date, visible_to_me)
    VALUES({}, '{}', '{}', curdate(), TRUE);""".format(str(users[0]), str(message), str(time))
    cursor.execute(query2)
    connection.commit()    

    query3 = """SELECT mssg_id from message where sender_id = %s"""%(users[0])   
    cursor.execute(query3)
    data3 = cursor.fetchall()
    print(data3)
    
    mssg_id = data3[-1][0]
    print(mssg_id)
    
    query4 = """INSERT INTO message_recipient(mssg_id, receiver_id)
    VALUES({}, '{}');""".format(mssg_id, contact)
    cursor.execute(query4)
    connection.commit() 
    
    load_messages_individual(contact_id)
    
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
    
    # query2 = "CREATE VIEW user_profile AS SELECT name, phone_number, bio FROM user WHERE uid = %s"%(users[0])
    # cursor.execute(query2)
    
    query3 = "select * from user_profile"
    cursor.execute(query3)
    data3 = cursor.fetchall()
    #print(data3)
    
    query4 = "DROP VIEW user_profile"
    cursor.execute(query4)
    
    frame5_label_Profile_name = Label(frame5, text = "Name: " + data3[0][0], font="Raleway", bg="white", fg="grey", height=2, width=30)
    frame5_label_Profile_name.grid(row = 1, column = 1)

    frame5_label_Profile_phone = Label(frame5, text = "Phone: " + str(int(data3[0][1])), font="Raleway", bg="white", fg="grey", height=2, width=30)
    frame5_label_Profile_phone.grid(row = 2, column = 1)

    frame5_label_Profile_bio = Label(frame5, text = "Bio: \n" + data3[0][2], font="Raleway", bg="white", fg="grey", height=2, width=30)
    frame5_label_Profile_bio.grid(row = 3, column = 1)

    show_frame(frame5)
    
def button_groups(name, phone, cursor, users):
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
        groups.append([i[0], data3[0][0]])
    
    result = ""
    
    for i in range(len(groups)):
        pass
        #print(groups[i])
        result = result + str(groups[i][0]) + ": " + groups[i][1] + "\n"
    #print(result)
    result = result[:-1]
    
    frame6_label_Display = Label(frame6, text = result, font="Raleway", bg="white", fg="black", height=10, width=15)
    frame6_label_Display.grid(row = 1, column = 1)
    
    show_frame(frame6)

def load_messages_group(group_id):
    phone_text = phone.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    users.append(data1[0][0])
    #users = users[-1]
    #print(users)
    
    group = group_id.get()
    #print(contact)
    show_frame(frame8)
    #MESSAGE BY USER
    query2 = """SELECT DISTINCT  M.mssg_id, M.message_body, M.sender_id, M.time, M.date 
                FROM message as M NATURAL JOIN message_recipient as R 
                WHERE (receiver_group_id = %s) AND (M.sender_id = %s)
                AND (M.mssg_id=R.mssg_id);"""%(group,users[0])
    cursor.execute(query2)
    data2 = cursor.fetchall()
    print(data2)
    
    # message by contact
    query3 = """SELECT DISTINCT M.mssg_id, M.message_body, M.sender_id, M.time, M.date 
    FROM message as M NATURAL JOIN message_recipient as R 
    WHERE (receiver_group_id = %s) AND (M.sender_id <> %s)
    AND (M.mssg_id=R.mssg_id);"""%(group, users[0])

    cursor.execute(query3)
    data3 = cursor.fetchall()
    print(data3)
    
    received = ""
    for i in data3:
        print(i[4])
        received = received + str(i[4]) + "; " + str(i[3]) + "-> " + str(i[1]) + "\n"
    #print(sent[:-1])
    received = received[:-1]
    
    sent = ""
    for i in data2:
        #print(i[4])
        sent = sent + str(i[4]) + "; " + str(i[3]) + "-> " + str(i[1]) + "\n"
    #print(sent[:-1])
    sent = sent[:-1]

    frame8_label_MessageRecieved = Label(frame8, text = received, font="Raleway", bg="white", fg="black", height=10, width=40)
    frame8_label_MessageRecieved.grid(row = 1, column = 1)
    
    frame8_label_MessageSent = Label(frame8, text = sent, font="Raleway", bg="white", fg="#32CD32", height=10, width=40)
    frame8_label_MessageSent.grid(row = 1, column = 3)

def create_message_group(group_id, MessageGrp):
    phone_text = phone.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    #users.append(data1[0][0])
    #users = users[-1]
    #print(users)
    
    group = group_id.get()
    #print(contact)
    
    message = MessageGrp.get()
    # print(message)
    
    from datetime import date
    today = date.today()
    date = today.strftime("%Y-%m-%d")
    # print("date =", date)
    
    from datetime import datetime
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    # print("Time =", time)
    
    query2 = """INSERT INTO message(sender_id, message_body, time, date, visible_to_me) VALUES( {},'{}','{}',curdate(), TRUE);""".format(users[0], str(message), str(time))
    cursor.execute(query2)
    connection.commit()    

    query3 = """SELECT mssg_id from message where sender_id = %s"""%(users[0])   
    cursor.execute(query3)
    data3 = cursor.fetchall()
    # print(data3)    
    
    mssg_id = data3[-1][0]
    # print(mssg_id)

    query4 = """INSERT INTO message_recipient(receiver_id, receiver_group_id)
            SELECT distinct user_id, group_id FROM user_group_info
            WHERE group_id = {} and user_id <> {};""".format(group, users[0])
    cursor.execute(query4)
    connection.commit() 
    
    query5 = "UPDATE message_recipient SET mssg_id =%s, status = 'sent' WHERE receiver_group_id = %s and mssg_id is null and status is null;" %(mssg_id,group)
    cursor.execute(query5)
    connection.commit()
    load_messages_group(group_id)
    
    
def show_frame(frame):
    #To show the selected frame
    frame.tkraise()

#frames
frame1 = Frame(root, bg="white")
frame2 = Frame(root, bg="white")
frame3 = Frame(root, bg="white")
frame4 = Frame(root, bg="white")
frame5 = Frame(root, bg="white")
frame6 = Frame(root, bg="white")
frame7 = Frame(root, bg="white")
frame8 = Frame(root, bg="white")

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8):
    frame.grid(row=0, column=0, sticky='nsew')

show_frame(frame1)

# Frame1: Landing page
logo1 = Image.open('Applogo.png')
logo1 = ImageTk.PhotoImage(logo1)
frame1_logo = Label(frame1, image=logo1)
frame1_logo.place(relx = 0.5, rely = 0.3, anchor = CENTER)
# frame1_logo.grid(row = 1, column = 1,sticky='wnse')

frame1_button_register = Button(frame1, text="Ready To Chat!", command=lambda:show_frame(frame2), bg="#32CD32", fg="white", height=2, width=20)
frame1_button_register.configure(font=("Helvetica", 18, "bold"))
frame1_button_register.place(relx = 0.5, rely = 0.8, anchor=CENTER)
# frame1_button_register.grid(row = 2, column = 1)

# Frame2: Login page
frame2_label_register = Label(frame2, text = "Login", font="Raleway", bg="#FF0000", fg="white", height=2, width=15)
frame2_label_register.grid(row = 0, column = 1)

logo2 = Image.open('Applogo.png')
logo2 = ImageTk.PhotoImage(logo2)
frame2_logo = Label(frame2, image=logo2)
frame2_logo.grid(row = 0, column = 1)

name = StringVar()
frame2_label_name = Label(frame2, text="Name:", font="Raleway", bg="white", fg="black", height=1, width=10).grid(row = 1, column = 0)
frame2_input_name = Entry(frame2, textvariable = name).grid(row = 1, column = 1)

phone = StringVar()
frame2_label_phone = Label(frame2, text="Phone:", font="Raleway", bg="white", fg="black", height=1, width=10).grid(row = 2, column = 0)
frame2_input_phone = Entry(frame2, textvariable = phone).grid(row = 2, column = 1)

frame2_button_after_login = Button(frame2, text="Login", command=lambda:button_login(name, phone, cursor, users),
                              font="Raleway", bg="#32CD32", fg="white", height=1, width=15)
frame2_button_after_login.grid(row = 4, column = 1)

# Frame3: Menu page
frame3_label_Menu = Label(frame3, text = "Menu", font="Raleway", bg="white", fg="black", height=2, width=15)
frame3_label_Menu.grid(row = 0, column = 1)

logo3 = Image.open('Applogo.png')
logo3 = ImageTk.PhotoImage(logo3)
frame3_logo = Label(frame3, image=logo3)
frame3_logo.grid(row = 0, column = 1)

frame3_button_Contacts = Button(frame3, text="Contacts", command=lambda: button_contacts(name, phone, cursor, names),
                              font="Raleway", bg="#32CD32", fg="white", height=1, width=15)
frame3_button_Contacts.grid(row = 1, column = 1)

frame3_button_Groups = Button(frame3, text="Groups", command=lambda: button_groups(name, phone, cursor, users),
                              font="Raleway", bg="#32CD32", fg="white", height=1, width=15)
frame3_button_Groups.grid(row = 2, column = 1)

frame3_button_Profile = Button(frame3, text="Profile", command=lambda: button_profile(name, phone, cursor, users),
                              font="Raleway", bg="#32CD32", fg="white", height=1, width=15)
frame3_button_Profile.grid(row = 3, column = 1)

# Frame4: Contacts page
frame4_label_Contacts = Label(frame4, text = "Contacts", font="Raleway", bg="white", fg="black", height=2, width=15)
frame4_label_Contacts.grid(row = 0, column = 1)

frame4_button_Back = Button(frame4, text="Back", command=lambda: show_frame(frame3),
                              font="Raleway", bg="grey", fg="white", height=1, width=5)
frame4_button_Back.grid(row = 0, column = 0)

contact_id = StringVar()
frame4_label_contact_id = Label(frame4, text="Contact ID:", font="Raleway", bg="white", fg="black", height=1, width=10).grid(row = 2, column = 0)
frame4_input_contact_id = Entry(frame4, textvariable = contact_id).grid(row = 2, column = 1)

frame4_button_Select = Button(frame4, text="Select", command=lambda: load_messages_individual(contact_id),
                              font="Raleway", bg="#32CD32", fg="white", height=1, width=5)
frame4_button_Select.grid(row = 3, column = 1)

# Frame5: Profile page
frame5_label_Profile = Label(frame5, text = "Profile", font="Raleway", bg="white", fg="black", height=2, width=15)
frame5_label_Profile.grid(row = 0, column = 1)

frame5_button_Back = Button(frame5, text="Back", command=lambda: show_frame(frame3),
                              font="Raleway", bg="grey", fg="white", height=1, width=5)
frame5_button_Back.grid(row = 0, column = 0)

# Frame6: Groups page
frame6_label_Groups = Label(frame6, text = "Groups", font="Raleway", bg="white", fg="black", height=2, width=15)
frame6_label_Groups.grid(row = 0, column = 1)

frame6_button_Back = Button(frame6, text="Back", command=lambda: show_frame(frame3),
                              font="Raleway", bg="grey", fg="white", height=1, width=5)
frame6_button_Back.grid(row = 0, column = 0)

group_id = StringVar()
frame6_label_group_id = Label(frame6, text="Group ID:", font="Raleway", bg="white", fg="black", height=1, width=10).grid(row = 2, column = 0)
frame6_label_group_id = Entry(frame6, textvariable = group_id).grid(row = 2, column = 1)

frame6_button_Select = Button(frame6, text="Select", command=lambda: load_messages_group(group_id),
                              font="Raleway", bg="#32CD32", fg="white", height=1, width=5)
frame6_button_Select.grid(row = 3, column = 1)

# Frame7: Message_Individual page
frame7_label_Message = Label(frame7, text = "Message Contact", font="Raleway", bg="white", fg="black", height=2, width=15)
frame7_label_Message.grid(row = 0, column = 2)

frame7_button_Back = Button(frame7, text="Back", command=lambda: show_frame(frame3),
                              font="Raleway", bg="grey", fg="white", height=1, width=5)
frame7_button_Back.grid(row = 0, column = 0)

frame7_button_Send = Button(frame7, text="Send", command=lambda: create_message_individual(contact_id, MessageIndi),
                              font="Raleway", bg="#32CD32", fg="white", height=1, width=5)
frame7_button_Send.grid(row = 2, column = 3)

MessageIndi = StringVar()
frame7_label_message = Label(frame7, text="Message:", font="Raleway", bg="white", fg="black", height=1, width=10).grid(row = 2, column = 0)
frame7_input_message = Entry(frame7, textvariable = MessageIndi, width=100).grid(row = 2, column = 1)

# Frame8: Message_Group page
frame8_label_Message = Label(frame8, text = "Message Group", font="Raleway", bg="white", fg="black", height=2, width=15)
frame8_label_Message.grid(row = 0, column = 2)

frame8_button_Back = Button(frame8, text="Back", command=lambda: show_frame(frame3),
                              font="Raleway", bg="grey", fg="white", height=1, width=5)
frame8_button_Back.grid(row = 0, column = 0)

frame8_button_Send = Button(frame8, text="Send", command=lambda: create_message_group(group_id, MessageGrp),
                              font="Raleway", bg="#32CD32", fg="white", height=1, width=5)
frame8_button_Send.grid(row = 2, column = 3)

MessageGrp = StringVar()
frame8_label_message = Label(frame8, text="Message:", font="Raleway", bg="white", fg="black", height=1, width=10).grid(row = 2, column = 0)
frame8_input_message = Entry(frame8, textvariable = MessageGrp, width=100).grid(row = 2, column = 1)


root.mainloop()
