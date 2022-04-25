Drop table User;
Drop table Grp;
Drop table User_group_info;
Drop table Message;
Drop table Contacts;
Drop table Message_recipient;

DROP VIEW user_profile;

CREATE TABLE User (
uid INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(16) NOT NULL,
phone_number FLOAT NOT NULL UNIQUE,
bio VARCHAR(11) NOT NULL
);
INSERT INTO user(uid,name,phone_number,bio) VALUES (1001,'Akshit Kumar',1000000000,'i am akshit');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1002,'Abhay Jindal',2000000000,'im abhay');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1003,'Charu Kaur',3000000000,'im charu');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1004,'Divya Sharma',4000000000,'im divya');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1005,'Esha Kapoor',5000000000,'im esha');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1006,'Ayush Raje Chak',6000000000,'im ayush');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1007,'Aryan Verma',7000000000,'im aryan');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1008,'Muskan Gupta',8000000000,'im muskan');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1009,'Himansh Yadav',9000000000,'im himansh');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1010,'Sanya Samrath',1010000000,'im sanya');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1011,'Aditya Peer',1100000000,'im aditya');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1012,'Shrugal Tayal',1200000000,'im shrugal');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1013,'Gauri Srinivasan',1300000000,'im gauri');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1014,'Shreya Bhatia',1400000000,'im shreya');
INSERT INTO user(uid,name,phone_number,bio) VALUES (1015,'Jay Malhotra',1500000000,'im jay');

CREATE TABLE GRP (
group_id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
group_name VARCHAR(16) NOT NULL,
date DATE NOT NULL,
creator_id INT NOT NULL UNIQUE
);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (10,'Ada','2020-10-01',1001);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (11,'dbms','2020-10-02',1002);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (12,'bio','2020-10-03',1003);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (13,'football','2020-10-04',1004);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (14,'iiitd peeps','2020-10-05',1005);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (15,'hostellers','2020-10-06',1007);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (16,'badminton','2020-10-07',1006);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (17,'clubs','2020-10-08',1011);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (18,'study grp','2021-09-29',1013);
INSERT INTO grp(group_id,group_name,date,creator_id) VALUES (19,'cse','2021-09-30',1014);

CREATE TABLE User_group_info (
user_id INT NOT NULL,
group_id INT NOT NULL,
is_admin BOOLEAN NOT NULL
);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1001,10,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1004,10,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1010,10,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1013,10,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1015,10,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1002,11,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1006,11,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1010,11,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1012,11,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1014,11,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1002,12,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1003,12,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1006,12,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1008,12,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1011,12,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1001,13,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1004,13,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1008,13,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1009,13,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1013,13,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1003,14,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1005,14,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1007,14,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1011,14,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1015,14,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1002,15,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1007,15,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1009,15,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1011,15,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1014,15,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1001,16,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1004,16,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1006,16,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1010,16,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1012,16,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1001,17,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1003,17,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1007,17,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1011,17,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1012,17,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1004,18,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1006,18,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1009,18,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1013,18,TRUE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1015,18,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1001,19,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1003,19,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1005,19,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1008,19,FALSE);
INSERT INTO user_group_info(user_id,group_id,is_admin) VALUES (1014,19,TRUE);

CREATE TABLE Message (
mssg_id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
sender_id INT NOT NULL,
message_body VARCHAR(100) NOT NULL,
time VARCHAR(11) NOT NULL,
date DATE NOT NULL,
visible_to_me BOOLEAN DEFAULT TRUE
);
INSERT INTO message(mssg_id,sender_id,message_body,time,date,visible_to_me) VALUES (101,1004,'hi','10:11:12','2021-09-29',TRUE);
INSERT INTO message(mssg_id,sender_id,message_body,time,date,visible_to_me) VALUES (102,1002,'hello','5:46:40','2021-09-30',TRUE);
INSERT INTO message(mssg_id,sender_id,message_body,time,date,visible_to_me) VALUES (103,1001,'hey','11:19:05','2021-10-01',TRUE);
INSERT INTO message(mssg_id,sender_id,message_body,time,date,visible_to_me) VALUES (104,1011,'hi there','7:16:47','2021-10-02',TRUE);
INSERT INTO message(mssg_id,sender_id,message_body,time,date,visible_to_me) VALUES (105,1001,'hiya','6:54:07','2021-10-03',TRUE);
INSERT INTO message(mssg_id,sender_id,message_body,time,date,visible_to_me) VALUES (106,1005,'hellooo','4:05:55','2021-10-04',TRUE);
INSERT INTO message(mssg_id,sender_id,message_body,time,date,visible_to_me) VALUES (107,1006,'heyyy','16:14:30','2021-10-05',TRUE);

CREATE TABLE Contacts (
id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
user_id INT NOT NULL,
contact_person_id INT NOT NULL,
saved_by_name VARCHAR(20),
is_blocked BOOLEAN DEFAULT FALSE,
is_saved BOOLEAN DEFAULT FALSE,
CHECK (user_id <> contact_person_id)
);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (301,1001,1009,'Potts',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (302,1001,1005,'Ratliff',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (303,1001,1011,'Clayton',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (304,1001,1012,'Gould',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (305,1014,1003,'Morse',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (306,1014,1002,'Ferguson',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (307,1014,1008,'Schwartz',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (308,1002,1014,'Cameron',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (309,1002,1013,'Fitzgerald',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (310,1002,1001,'Kane',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (311,1002,1012,'Hamptn',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (312,1003,1010,'Hyde',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (313,1003,1001,'Brown',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (314,1003,1004,'Bender',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (315,1003,1015,'Olsn',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (316,1003,1005,'Brewer',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (317,1005,1004,'Ortega',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (318,1005,1014,'Gallagher',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (319,1005,1001,'Franco',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (320,1006,1003,'Flowers',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (321,1006,1014,'Richard',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (322,1006,1015,'Walter',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (323,1006,1005,'Tate',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (324,1006,1002,'Jarvis',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (325,1006,1007,'Good',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (326,1007,1015,'Santiago',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (327,1007,1011,'Cash',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (328,1007,1008,'Foreman',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (329,1007,1010,'Mors',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (330,1008,1004,'Stevens',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (331,1008,1013,'Edwards',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (332,1009,1012,'Horne',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (333,1009,1008,'Cline',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (334,1009,1011,'Talley',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (335,1009,1005,'Owens',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (336,1009,1001,'Murray',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (337,1010,1002,'Taylor',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (338,1010,1005,'Cox',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (339,1011,1006,'Gill',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (340,1011,1004,'Barlow',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (341,1011,1007,'Olson',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (342,1012,1003,'Lynn',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (343,1012,1002,'Sharp',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (344,1012,1010,'Shields',TRUE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (345,1013,1006,'Hickman',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (346,1013,1001,'Barrett',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (347,1014,1006,'Conrad',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (348,1015,1003,'Hampton',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (349,1015,1014,'Tran',FALSE,TRUE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (350,1015,1008,'Warner',FALSE,FALSE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (351,1010,1001,NULL,FALSE,FALSE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (352,1010,1007,NULL,FALSE,FALSE);
INSERT INTO Contacts(id,user_id,contact_person_id,saved_by_name,is_blocked,is_saved) VALUES (353,1008,1006,NULL,FALSE,FALSE);

CREATE TABLE Message_recipient (
id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
mssg_id INT,    
receiver_id INT NOT NULL,
receiver_group_id INT,
is_read BOOLEAN DEFAULT FALSE,
status VARCHAR(10),
CHECK( (is_read, status) <> (true, 'not sent') ) 
);
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status) VALUES (101,1001,10,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (101,1010,10,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (101,1013,10,FALSE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (101,1015,10,FALSE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (102,1007,15,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (102,1009,15,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (102,1011,15,FALSE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (102,1014,15,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (103,1003,17,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (103,1007,17,FALSE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (103,1011,17,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (103,1012,17,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (104,1001,17,FALSE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (104,1003,17,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (104,1007,17,FALSE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (104,1012,17,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (105,1005,NULL,TRUE,'sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (106,1009,NULL,FALSE,'not sent');
INSERT INTO message_recipient(mssg_id,receiver_id,receiver_group_id,is_read,status)  VALUES (107,1003,NULL,FALSE,'sent');

# Query1
CREATE VIEW user_profile AS
SELECT name, phone_number, bio
FROM user
WHERE uid=1001;

# Query2
SELECT phone_number, bio, name
FROM user
WHERE uid = 1005 and ( SELECT count(contact_person_id)
FROM contacts
WHERE user_id = 1001 and contact_person_id = 1005);

# Query3
Select contact_person_id, saved_by_name
From contacts
Where user_id=1014 and is_saved = TRUE;

# Query4
Select U.name ,U.uid
From user as U, contacts as C
Where C.user_id = 1014 and U.uid = C.contact_person_id and is_blocked = TRUE;

# Query5
SELECT M.mssg_id, M.message_body, M.sender_id, M.time, M.date
FROM message as M, message_recipient as R
WHERE (M.sender_id = 1001 or M.sender_id = 1005)
AND (R.receiver_id = 1005 or R.receiver_id = 1001)
AND (receiver_group_id is null)
AND (M.mssg_id=R.mssg_id);

# Query6
SELECT group_name, date, creator_id
FROM grp as G, user_group_info as I
Where I.user_id = 1001 and I.group_id = G.group_id;

# Query7
SELECT G.group_id, G.group_name
FROM grp AS G
WHERE G.group_id in (SELECT UG1.group_id
FROM user_group_info as UG1, user_group_info as UG2
WHERE UG1.user_id =1006 and UG2.user_id = 1004
and UG1.group_id = UG2.group_id);

# Query8
SELECT COUNT(user_id), group_id
FROM user_group_info
GROUP BY group_id
ORDER BY COUNT(user_id) DESC;

# Query9
SET SQL_SAFE_UPDATES = 0;
UPDATE user_group_info
SET is_admin = TRUE
WHERE user_id=1004;

# Query10
SET SQL_SAFE_UPDATES = 0;
SELECT * FROM grp;
UPDATE grp
SET group_name ='csd'
WHERE group_id=19;

# Query11
INSERT INTO message(sender_id, message_body, time, date, visible_to_me)
VALUES( 1001,
'20th is my bday',
'09:09:09',
'2022-03-01', 
TRUE);

# Query12
INSERT INTO message_recipient(receiver_id, receiver_group_id)
SELECT distinct user_id, group_id FROM user_group_info
WHERE group_id = 20 and user_id <> 1001;

# Query13
UPDATE message_recipient
SET mssg_id =108
WHERE receiver_group_id = 20 and mssg_id is null and status is null;

select * from contacts;