#from tkinter import *
import tkinter as tk
from tkinter import ttk;
from PIL import Image, ImageTk
from datetime import datetime

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
    profile = []
    for i in range(len(contacts)):
        n = i + 7
        framen = tk.Frame(root, bg="#1B453D")
        framen.grid(row=0, column=0, sticky='nsew')
        framey = tk.Frame(root, bg="#1B453D")
        framey.grid(row=0, column=0, sticky='nsew')
        buttons.append(tk.Button(frame4, text = contacts[i][1], font=("Helvetica", 16, "bold"), bg="#32CD32", fg="black", height=1, width=15,command=lambda i=i:contact_frames(framen,i,contacts)).place(relx=0.445,rely=(i*0.05)+0.15))
        profile.append(tk.Button(frame4, text = "View Profile", font=("Helvetica", 16, "bold"), bg="#32CD32", fg="black", height=1, width=10,command=lambda i=i:profile_frame(framey,i,contacts,framen)).place(relx=0.57,rely=(i*0.05)+0.15))
        
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

def load_profile(frame,contact_id,framen):
    query = "SELECT name, phone_number,bio from user where uid = %s"%(contact_id)
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data)
    
    frame_label_Profile = tk.Label(frame, text = "Profile", font=("Helvetica",20, "bold"), bg="#93C572", fg="#123524", height=2, width=15)
    frame_label_Profile.place(relx = 0.43,rely=0.07)

    frame_button_Back = tk.Button(frame, text="Back", command=lambda: show_frame(frame4),font=("Helvetica",17, "bold"), bg="gray", fg="Black", height=1, width=5)
    frame_button_Back.grid(row = 0, column = 0)
    
    frame_label_Profile_name = tk.Label(frame, text = "Name: " + data[0][0], font=("Helvetica", 16, "bold"), bg="#93C572", fg="#123524", height=1, width=30)
    frame_label_Profile_name.place(relx = 0.4,rely = 0.2)

    frame_label_Profile_phone = tk.Label(frame, text = "Phone: " + str(int(data[0][1])), font=("Helvetica", 16, "bold"), bg="#93C572", fg="#123524", height=1, width=30)
    frame_label_Profile_phone.place(relx = 0.4,rely = 0.25)

    frame_label_Profile_bio = tk.Label(frame, text = "Bio: \n" + data[0][2], font=("Helvetica", 16, "bold"), bg="#93C572", fg="#123524", height=2, width=30)
    frame_label_Profile_bio.place(relx = 0.4,rely = 0.31)

def profile_frame(frame,i,contacts,framen):
    show_frame(frame)
    contact_id = contacts[i][0]
    load_profile(frame,contact_id,framen)
    
def contact_frames(frame,i,contacts):
    show_frame(frame)
    contact_id = contacts[i][0]
    load_messages_individual(contact_id,frame)

def load_messages_individual(contact_id,frame):
    text_widget_1 = tk.Text(frame, height=35, width=50)
    text_widget_2 = tk.Text(frame, height=35, width=50)
    message_label = tk.Label(frame, text = "Message", bg="#235347", fg="black", height=2, width=15)
    message_label.configure(font=("Helvetica", 20, "bold"))
    message_label.place(relx = 0.44, rely = 0.05)
    
    MessageIndi = tk.StringVar()
    frame_input_message = tk.Entry(frame, textvariable = MessageIndi, width=70).place(relx = 0.25,rely=0.91)
    
    frame_button_Send = tk.Button(frame, text="Send", command=lambda: create_message_individual(contact_id, MessageIndi, frame),font=("Helvetica", 16, "bold"), bg="gray", fg="Black", height=1, width=5)
    frame_button_Send.place(relx = 0.75,rely=0.909)
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
    data5 = [(" ")]
    if(data3):
        query4 = "SELECT name FROM user Where uid=%s"%(data3[0][2])
        cursor.execute(query4)
        data5 = cursor.fetchall()
    received = ""
    for i in data3:
        #print(i[4])
        received = received + str(i[4]) + "\t" + str(i[3]) +"\t"+str(data5[0][0]) +"\n" + str(i[1]) + "\n"
    #print(sent[:-1])
    received = received[:-1]
    
    # print(received)
    sent = ""
    for i in data2:
        #print(i[4])
        sent = sent + str(i[4]) + "\t" + str(i[3]) + "\n" + str(i[1]) + "\n"
    #print(sent[:-1])
    sent = sent[:-1]

    text_widget_1.place(relx = 0.25,rely=0.3)
    text_widget_1.insert(tk.END, sent)    
    
    text_widget_2.place(relx = 0.55,rely=0.3)
    text_widget_2.insert(tk.END, received)

def update_query(grp_name,group_id):
    query = "UPDATE grp SET group_name = '%s' WHERE group_id = %s"%(grp_name.get(),group_id)
    cursor.execute(query)
    connection.commit()
    query2 = "REVOKE UPDATE (group_name) ON grp FROM grp_admin"
    cursor.execute(query2)
    connection.commit()
    show_frame(frame3)

def give_name(group_id):
    frame = tk.Frame(root, bg="#1B453D")
    frame.grid(row=0, column=0, sticky='nsew')
    Label_frame = tk.Label(frame, font=("Helvetica", 20, "bold"),text = "Enter Group Name", bg="#235347", fg="black", height=2, width=20).place(relx = 0.42, rely = 0.15)
    grp_name = tk.StringVar()
    frame_input_name = tk.Entry(frame, textvariable = grp_name,).place(relx = 0.499, rely = 0.3, anchor=tk.CENTER)
    frame_button_accept = tk.Button(frame, text="Save", command=lambda:update_query(grp_name,group_id),font = ("Helvetica",20,"bold"), bg="gray", fg="black", height=1, width=5)
    frame_button_accept.place(relx = 0.475,rely=0.35)
    
def give_grants(group_id,users):
    query = "SELECT is_admin FROM user_group_info Where user_id = %s and group_id = %s"%(users[0],group_id)
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data)
    if(data[0][0] == 1):
        query = "GRANT UPDATE(group_name) ON grp to grp_admin"
        cursor.execute(query)
        connection.commit()
        give_name(group_id)

def load_messages_group(group_id,frame):
    phone_text = phone.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    users.append(data1[0][0])
    #users = users[-1]
    #print(users)
    members_label = tk.Label(frame, text = "Members", bg="#235347", fg="black", height=1, width=10)
    members_label.configure(font=("Helvetica", 20, "bold"))
    members_label.place(relx = 0.04, rely = 0.2)
    
    query0 = "SELECT COUNT(%s), group_id FROM user_group_info GROUP BY group_id ORDER BY COUNT(user_id) DESC;"%(users[0])
    cursor.execute(query0)
    data0 = cursor.fetchall()
    
    number_members_label = tk.Label(frame, font=("Helvetica", 15, "bold"),text = str(data0[0][0])+" Participants", bg="#235347", fg="black", height=1, width=18).place(relx = 0.03, rely = 0.76)
    
    members_window = tk.Text(frame, height=25, width=30)
    members_window.place(relx = 0.01, rely = 0.3)
    
    
    text_widget_1 = tk.Text(frame, height=35, width=50)
    text_widget_2 = tk.Text(frame, height=35, width=50)
    
    Message_group = tk.StringVar()
    MessageGrp = tk.Entry(frame, textvariable = Message_group, width=70).place(relx = 0.25,rely=0.91)
    
    frame_button_Send = tk.Button(frame, text="Send", command=lambda: create_message_group(group_id, Message_group.get(),frame),font = ("Helvetica",20,"bold"), bg="gray", fg="black", height=1, width=5)
    frame_button_Send.place(relx = 0.75,rely=0.909)
    
    frame_button_change_name = tk.Button(frame, text="Change Group Name", command=lambda: give_grants(group_id,users),font = ("Helvetica",15,"bold"), bg="gray", fg="black", height=1, width=15)
    frame_button_change_name.place(relx = 0.85,rely=0.5)
    
    group = group_id
    #print(contact)
    # show_frame(frame)
    #MESSAGE BY USER
    query2 = """SELECT DISTINCT M.sender_id, M.message_body, M.sender_id, M.time, M.date 
                FROM message as M NATURAL JOIN message_recipient as R 
                WHERE (receiver_group_id = %s) AND (M.sender_id = %s)
                AND (M.mssg_id=R.mssg_id);"""%(group,users[0])
    cursor.execute(query2)
    data2 = cursor.fetchall()
    # print(data2)
    
    # message by contact
    query3 = """SELECT DISTINCT M.message_body, M.sender_id, M.time, M.date 
    FROM message as M NATURAL JOIN message_recipient as R 
    WHERE (receiver_group_id = %s) AND (M.sender_id <> %s)
    AND (M.mssg_id=R.mssg_id);"""%(group, users[0])
    cursor.execute(query3)
    data3 = cursor.fetchall()
    
    # print(data3)
    data5 = [(" ")]
    if(data3):
        query4 = "SELECT name FROM user Where uid=%s"%(data3[0][1])
        cursor.execute(query4)
        data5 = cursor.fetchall()
    
    # print(data3)
    
    received = ""
    for i in data3:
        received = received + str(i[2]) + "\t"+ str(i[3])+"\t"+ str(data5[0][0]) +"\n" + str(i[0]) + "\n" + "\n"
    # print(received[:-1])
    received = received[:-1]
    
    sent = ""
    for i in data2:
        #print(i[4])
        sent = sent + str(i[4]) + "\t" + str(i[3]) + "\n" + str(i[1]) + "\n" + "\n"
    # print(sent[:-1])
    sent = sent[:-1]

    query = "SELECT U.uid, U.name,U.bio FROM user_group_info as UG NATURAL JOIN user as U WHERE group_id = %s AND (U.uid = UG.user_id)"%(group_id)
    cursor.execute(query)
    data4 = cursor.fetchall()
    # print(data4)
    members_name = ""
    for i in data4:
        members_name = members_name + "~"+str(i[1])+ "\n" + " " + str(i[2]) + "\n" + "\n"
    members_window.insert(tk.END, members_name)
    # frame8_label_MessageRecieved = tk.Label(frame, text = received, font="Raleway", bg="white", fg="black", height=10, width=40)
    # frame8_label_MessageRecieved.grid(row = 1, column = 1)
    text_widget_1.place(relx = 0.25,rely=0.3)
    text_widget_1.insert(tk.END, sent)    
    
    text_widget_2.place(relx = 0.55,rely=0.3)
    text_widget_2.insert(tk.END, received)
    # frame8_label_MessageSent = tk.Label(frame8, text = sent, font="Raleway", bg="white", fg="#32CD32", height=10, width=40)
    # frame8_label_MessageSent.grid(row = 1, column = 3)


def create_message_group(group_id,message,frame):
    phone_text = phone.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    #users.append(data1[0][0])
    #users = users[-1]
    #print(users)
    
    group = group_id
    #print(contact)
    # print(message)
    
    today = datetime.today()
    date = today.strftime("%Y-%m-%d")
    # print("date =", date)
    
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
            WHERE group_id = %s and user_id <> %s;"""%(group, users[0])
    cursor.execute(query4)
    connection.commit() 
    
    query5 = "UPDATE message_recipient SET mssg_id =%s, status = 'sent' WHERE receiver_group_id = %s and mssg_id is null and status is null;" %(mssg_id,group)
    cursor.execute(query5)
    connection.commit()
    load_messages_group(group_id,frame)
    

def create_message_individual(contact_id, MessageIndi, frame):
    phone_text = phone.get()
    query1 = "select uid from User where phone_number = %s"%(phone_text)
    cursor.execute(query1)
    data1 = cursor.fetchall()
    #users.append(data1[0][0])
    #users = users[-1]
    # print(users)
    
    contact = contact_id
    #print(contact)
    
    message = MessageIndi.get()
    today = datetime.today()
    date = today.strftime("%Y-%m-%d")
    
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    # print("Time =", str(time))
    
    query2 = """INSERT INTO message(sender_id, message_body, time, date, visible_to_me)
    VALUES({}, '{}', '{}', curdate(), TRUE);""".format(str(users[0]), str(message), str(time))
    cursor.execute(query2)
    connection.commit()    

    # query5 ="""CREATE INDEX message_c ON message (sender_id);"""
    # cursor.execute(query5)
    # indexList = cursor.fetchall()
    # print(indexList)
    
    
    query3 = """SELECT mssg_id from message where sender_id = %s"""%(users[0])   
    cursor.execute(query3)
    data3 = cursor.fetchall()
    # print(data3)
    
    # query6 ="""ALTER TABLE message DROP INDEX message_c;"""
    # cursor.execute(query6)
    # connection.commit()
    
    mssg_id = data3[-1][0]
    print(mssg_id)
    
    query4 = """INSERT INTO message_recipient(mssg_id, receiver_id,status)
    VALUES({}, '{}','sent');""".format(mssg_id, contact)
    cursor.execute(query4)
    connection.commit() 
    
    load_messages_individual(contact_id, frame)

def change_query(users,name,phone,bio):
    user_id = users[0] 
    uname = name.get()
    uphone = phone.get()
    ubio = bio.get()
    query1 = "UPDATE user SET name = '%s',bio = '%s' WHERE uid=%s"%(uname,ubio,user_id)
    cursor.execute(query1)
    connection.commit()
    
    button_profile(name, phone, cursor, users)
    
def change_profile(frame,users):
    user_id = users[0]
    show_frame(frame)
    
    name_label = tk.Label(frame,font=("Helvetica", 20, "bold"), text = "Edit Profile", bg="#235347", fg="black", height=1, width=10).place(relx = 0.446, rely = 0.06)
    name_label = tk.Label(frame,font=("Helvetica", 20, "bold"), text = "Name", bg="#235347", fg="black", height=1, width=10).place(relx = 0.3, rely = 0.13)
    
    name = tk.StringVar()
    frame9_input_name = tk.Entry(frame, textvariable = name).place(relx = 0.5, rely = 0.15, anchor=tk.CENTER)
    phone_label = tk.Label(frame,font=("Helvetica", 20, "bold"), text = "Bio", bg="#235347", fg="black", height=1, width=10).place(relx = 0.3, rely = 0.18)
    
    bio = tk.StringVar()
    frame9_input_bio = tk.Entry(frame, textvariable = bio).place(relx = 0.5, rely = 0.2, anchor=tk.CENTER)
    change_button = tk.Button(frame,text = "Save", font=("Helvetica", 20, "bold"), command=lambda:change_query(users,name,phone,bio),bg="gray", fg="black", height=2, width=10).place(relx = 0.445,rely=0.3)
    
    frame_button_Back = tk.Button(frame, text="Back", command=lambda: show_frame(frame5),font=("Helvetica",16, "bold"), bg="gray", fg="Black", height=1, width=5)
    frame_button_Back.grid(row = 0, column = 0)


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

    frame9 = tk.Frame(root, bg="#1B453D")
    frame9.grid(row=0, column=0, sticky='nsew')
    frame5_change_button = tk.Button(frame5,text = "Change Profile", font=("Helvetica", 18, "bold"), command=lambda: change_profile(frame9,users),bg="gray", fg="black", height=1, width=10).place(relx = 0.445,rely=0.4)
    
    show_frame(frame5)

#
def group_frames(frame,i,groups):
    show_frame(frame)
    # print(groups)
    group_id = groups[i][0]
    load_messages_group(group_id,frame)
    
        
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
        query3 = "SELECT group_id , group_name FROM grp Where group_id = %s"%(i[0])
        cursor.execute(query3)
        data3 = cursor.fetchall()
        # print(data3)
        groups.append(data3[0])
    
    grp_button = []
    for i in range(len(groups)):
        pass
        x = i + 7
        framex = tk.Frame(root, bg="#1B453D")
        framex.grid(row=0, column=0, sticky='nsew')
        
        grp_button.append(tk.Button(frame6, text = groups[i][1], font=("Helvetica", 16, "bold"),bg="gray", fg="black", height=1, width=15,command=lambda i=i :group_frames(framex,i,groups)).place(relx=0.445,rely=(i*0.05)+0.15))
        
        message_label = tk.Label(framex, text = "Message", bg="#235347", fg="black", height=2, width=15)
        message_label.configure(font=("Helvetica", 20, "bold"))
        message_label.place(relx = 0.44, rely = 0.05)
        
        sent_label = tk.Label(framex, text = "Sent", bg="#235347", fg="black", height=1, width=15)
        sent_label.configure(font=("Helvetica", 20, "bold"))
        sent_label.place(relx = 0.3, rely = 0.2)
        
        
        received_label = tk.Label(framex, text = "Recieved", bg="#235347", fg="black", height=1, width=15)
        received_label.configure(font=("Helvetica", 20, "bold"))
        received_label.place(relx = 0.6, rely = 0.2)
        
        
        framen_button_Back = tk.Button(framex, text="Back", command=lambda:show_frame(frame6),font=("Helvetica", 16, "bold"), bg="grey", fg="black", height=1, width=5)
        framen_button_Back.grid(row = 0, column = 0)
    
    show_frame(frame6)
 
def show_blocked(phone,frame):
    show_frame(frame)
    phone_text = phone.get()
    #bio_text = bio.get()
    query = "select uid from User where phone_number = %s"%(phone_text) #Akshit Kumar 1000000000
    cursor.execute(query)
    data = cursor.fetchall()
    users.append(data[0][0])
    
    query2="Select U.name ,U.uid ,U.phone_number From user as U, contacts as C Where C.user_id = %s and U.uid = C.contact_person_id and is_blocked = TRUE;"%(users[0])
    cursor.execute(query2)
    data2 = cursor.fetchall()    
    
    label_blocked = tk.Label(frame, text = "Blocked Contacts", bg="#235347", fg="Black", height=2, width=15)
    label_blocked.configure(font=("Helvetica", 15, "bold"))
    label_blocked.place(relx = 0.5, rely = 0.05, anchor=tk.CENTER)
    
    if(data2):
        result = ""
        for i in data2:
            result = result +"~"+str(i[0])+"\n"+" "+str(i[2])+"\n"+"\n"
            
        label_name = tk.Label(frame, text = result, bg="#235347", fg="Black", height=20, width=15)
        label_name.configure(font=("Helvetica", 15, "bold"))
        label_name.place(relx = 0.46, rely = 0.2)
    
    else:
        label_name = tk.Label(frame, text = "No Blocked Contacts Found", bg="#235347", fg="Black", height=2, width=25)
        label_name.configure(font=("Helvetica", 15, "bold"))
        label_name.place(relx = 0.42, rely = 0.2)
        
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
frame7 = tk.Frame(root, bg="#1B453D")
# frame6 = Frame(root, bg="#1B453D")

for frame in (frame1, frame2, frame3, frame4, frame5, frame6,frame7):
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

frame3_button_Back = tk.Button(frame3, text="Back", command=lambda: show_frame(frame2),font=("Helvetica",16, "bold"), bg="gray", fg="Black", height=1, width=5)
frame3_button_Back.grid(row = 0, column = 0)

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

frame6_button_Back = tk.Button(frame6, text="Back", command=lambda: show_frame(frame3),font=("Helvetica",16, "bold"), bg="grey", fg="Black", height=1, width=5)
frame6_button_Back.grid(row = 0, column = 0)

exit_button = tk.Button(root, text="Exit", font = ("Helvetica",20,"bold"), command=root.destroy)
exit_button.place(relx=0.949,rely=0)

# Frame 7: Show Blocked Contacts
frame7_button_profile = tk.Button(frame3, text="Blocked Contacts", command=lambda: show_blocked(phone,frame7), bg="#235347", fg="black", height=1, width=15)
frame7_button_profile.place(relx = 0.44,rely = 0.9)
frame7_button_profile.configure(font=("Helvetica",20, "bold"))

frame7_button_Back = tk.Button(frame7, text="Back", command=lambda: show_frame(frame3),font=("Helvetica",16, "bold"), bg="grey", fg="Black", height=1, width=5)
frame7_button_Back.grid(row = 0, column = 0)

root.mainloop()