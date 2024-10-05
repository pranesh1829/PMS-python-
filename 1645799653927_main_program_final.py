# Establishing connection with MySQL
import mysql.connector as mycon
cnxn = mycon.connect(host = "localhost", user = "root", password = "pranesh@123", charset = "utf8")
cur = cnxn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS OPMS;")
cur.execute("USE OPMS;")


# Tables creation in Mysql Databases
cur.execute("CREATE TABLE IF NOT EXISTS USER1 (U_ID CHAR(7) PRIMARY KEY,U_NAME VARCHAR(30) NOT NULL,U_AGE INT,U_ADDRESS VARCHAR(50),CITY VARCHAR(15),U_MOBILE BIGINT(10),U_PWD VARCHAR(20));")
cur.execute("CREATE TABLE IF NOT EXISTS MEDICINE1 (M_ID CHAR(7) PRIMARY KEY,M_NAME VARCHAR(30) NOT NULL,M_PRICE FLOAT(7,2),M_AVAILABILITY INT(3));")
cur.execute("CREATE TABLE IF NOT EXISTS ORDER1 (U_ID CHAR(7) NOT NULL,M_ID CHAR(7) NOT NULL,QUANTITY INT(5),DELIVERY_STATUS CHAR(10),PAYMENT_STATUS CHAR(10),TOTAL_BILL FLOAT(8,2));")


# Creating foreign key constraints in table 'ORDER'
cur.execute("ALTER TABLE ORDER1 ADD FOREIGN KEY(U_ID) REFERENCES USER1(U_ID);")
cur.execute("ALTER TABLE ORDER1 ADD FOREIGN KEY(M_ID) REFERENCES MEDICINE1(M_ID);")
cnxn.commit()


# MAIN PROGRAM
print("#"*100)
print("#  "*33 + "#")
print("#"*100)
print()
print("-------------------------------------ONLINE PHARMACY--------------------------------------")
print()
print("#"*100)
print("#  "*33 + "#")
print("#"*100)
print()
quit1 = "n"
while quit1.lower() == "n":
    print("""###SELECT USER TYPE\n\t\t1.ADMINISTRATOR\n\t\t2.USER\n\t\t3.EXIT""")
    choice1 = int(input("ENTER CHOICE:"))
    # ADMIN SITE
    if choice1 == 1:
        input_password = input("###ENTER ADMINISTRATOR PASSWORD:")
        if input_password != "123abc":
            print("###PASSWORD IS INCORRECT###\n###TRY AGAIN")
        else:
            print()
            print("###ACCESS GRANTED###")
            print("WELCOME BACK!!!")
            print()
            admin_more = "y"
            while admin_more.lower() == "y":
                print("""### SELECT ANY FUNCTIONALITY###\n\t\t1.ACCESS USER DETAILS\n\t\t2.ACCESS MEDICINE DETAILS\n\t\t3.ACCESS ORDER DETAILS""")
                choice2 = int(input("###ENTER CHOICE:"))

                #ADMIN SITE: USER SECTION......
                if choice2 == 1:
                    print()
                    print("###WELCOME TO USER SECTION###")
                    print()
                    print("""###SELECT SPECIFIC TASK###\n\t\t1.VIEW USER DETAILS\n\t\t2.ADD A NEW USER\n\t\t3.EDIT DETAILS OF EXISTING USER\n\t\t4.DELETE AN EXISTING USER""")
                    choice3 = int(input("###ENTER CHOICE:"))
                    print()
                    if choice3 == 1:
                        view_more = "y"
                        while view_more.lower() == "y":
                            print("""###SELECT ANY CATEGORY TO SEARCH BY###\n\t\t0.SHOW ALL EXISTING USERS\n\t\t1.SEARCH BY USER_ID\n\t\t2.SEARCH BY USER_NAME\n\t\t3.SEARCH BY AGE_CATEGORY\n\t\t4.SEARCH BY CITY""")
                            print()
                            choice4 = int(input("###ENTER CHOICE:"))
                            print()
                            cur.execute("SELECT * FROM USER1;")
                            result = cur.fetchall()
                            count1 = cur.rowcount
                            if choice4 == 0:
                                if count1 == 0:
                                    print("###SORRY!!! NO USER DETAILS IN TABLE")
                                else:
                                    print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME", "AGE","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                    for row in result:
                                        USER_ID, USER_NAME, AGE, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                        print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME, AGE,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))

                            elif choice4 == 1:
                                input_id1 = input("###ENTER USER_ID TO SEARCH:")
                                if count1 == 0:
                                    print("###SORRY!!! NO USER DETAILS IN TABLE")
                                else:
                                    count2 = 0
                                    for row in result:
                                        if row[0] == input_id1:
                                            count2 += 1
                                    if count2 == 0:
                                        print("###USER_ID NOT FOUND")
                                    else:
                                        print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME","AGE","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                        for row in result:
                                            if row[0] == input_id1:
                                                USER_ID, USER_NAME, AGE, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                                print(
                                                    "{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME,AGE,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))

                            elif choice4 == 2:
                                input_name1 = input("###ENTER USER_NAME TO SEARCH:")
                                if count1 == 0:
                                    print("###SORRY!!! NO USER DETAILS IN TABLE")
                                else:
                                    count3 = 0
                                    for row in result:
                                        if row[1] == input_name1:
                                            count3 += 1
                                    if count3 == 0:
                                        print("###USER_NAME NOT FOUND")
                                    else:
                                        print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME","AGE","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                        for row in result:
                                            if row[1] == input_name1:
                                                USER_ID, USER_NAME, AGE, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                                print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME,AGE,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))

                            elif choice4 == 3:
                                input_age1 = int(input("###ENTER MINIMUM USER_AGE TO SEARCH:"))
                                input_age2 = int(input("###ENTER MAXIMUM USER_AGE TO SEARCH:"))
                                if count1 == 0:
                                    print("###SORRY!!! NO USER DETAILS IN TABLE")
                                else:
                                    count2 = 0
                                    for row in result:
                                        if row[2] >= input_age1 and row[2] <= input_age2:
                                            count2 += 1
                                    if count2 == 0:
                                        print("###USER_ID NOT FOUND")
                                    else:
                                        print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME","AGE_GROUP","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                        for row in result:
                                            if row[2] >= input_age1 and row[2] <= input_age2:
                                                USER_ID, USER_NAME, AGE_GROUP, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                                print(
                                                    "{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME,AGE_GROUP,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))

                            elif choice4 == 4:
                                input_city1 = input("###ENTER CITY TO SEARCH:")
                                if count1 == 0:
                                    print("###SORRY!!! NO USER DETAILS IN TABLE")
                                else:
                                    count3 = 0
                                    for row in result:
                                        if row[4] == input_city1:
                                            count3 += 1
                                    if count3 == 0:
                                        print("###USERS IN GIVEN CITY NOT FOUND")
                                    else:
                                        print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME","AGE","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                        for row in result:
                                            if row[4] == input_city1:
                                                USER_ID, USER_NAME, AGE, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                                print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME,AGE,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))
                                            else:
                                                continue
                            else:
                                print("###INVALID CHOICE!!!")
                            view_more = input("DO YOU WANT TO VIEW MORE USER DETAILS?(Y/N)")

                    elif choice3 == 2:
                        add_more = "y"
                        while add_more.lower() == "y":
                            add_id1 = input("###ENTER USER_ID:")
                            add_name1 = input("###ENTER USER_NAME:")
                            add_age1 = int(input("###ENTER USER_AGE:"))
                            add_address1 = input("###ENTER USER_ADDRESS:")
                            add_city1 = input("###ENTER USER_CITY:")
                            add_mobile1 = int(input("###ENTER MOBILE NUMBER:"))
                            add_password1 = input("ENTER PASSWORD:")
                            cur.execute("INSERT INTO USER1(U_ID,U_NAME,U_AGE,U_ADDRESS,CITY,U_MOBILE,U_PWD) VALUES('{}','{}',{},'{}','{}',{},'{}')".format(add_id1, add_name1, add_age1,add_address1, add_city1,add_mobile1, add_password1))
                            cnxn.commit()
                            print()
                            print("###USER DETAILS ADDED TO USER TABLE###")
                            add_more = input("DO YOU WANT TO ADD MORE USERS?(Y/N)")

                    elif choice3 == 3:
                        cur.execute("SELECT * FROM USER1;")
                        result = cur.fetchall()
                        count3 = cur.rowcount
                        edit_more = "y"
                        while edit_more.lower() == "y":
                            print("""###YOU CAN EDIT USER DETAIL ON BASIS OF USER_ID""")
                            choice5 = 1
                            if choice5 == 1:
                                input_id2 = input("ENTER USER_ID TO EDIT:")
                                count4 = 0
                                for row in result:
                                    if row[0] == input_id2:
                                        count4 += 1
                                if count4 == 0:
                                    print("###USER_ID NOT FOUND")
                                else:
                                    edit_sameuser = "y"
                                    if edit_sameuser == "y":
                                        print("###THE CURRENT USER DETAILS ARE:")
                                        print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME","AGE","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                        for row in result:
                                            if row[0] == input_id2:
                                                USER_ID, USER_NAME, AGE, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                                print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME,AGE,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))
                                        print("""###SELECT THE DETAIL TO BE UPDATED:\n\t\t1.NAME\n\t\t2.AGE\n\t\t3.ADDRESS\n\t\t4.CITY\n\t\t5.MOBILE\n\t\t6.PASSWORD""")
                                        edit_sameuser1 = "y"
                                        while edit_sameuser == "y":
                                            choice6 = int(input("###ENTER CHOICE:"))
                                            if choice6 == 1:
                                                input_name2 = input("###ENTER NEW NAME:")
                                                cur.execute("UPDATE USER1 SET U_NAME = '{}' WHERE U_ID = '{}';".format(input_name2,input_id2))
                                                cnxn.commit()
                                                print("###USER DETAIL UPDATED SUCCESSFULLY!!!")
                                            elif choice6 == 2:
                                                input_age2 = int(input("###ENTER NEW AGE:"))
                                                cur.execute("UPDATE USER1 SET U_AGE = {} WHERE U_ID = '{}';".format(input_age2, input_id2))
                                                cnxn.commit()
                                                print("###USER DETAIL UPDATED SUCCESSFULLY!!!")
                                            elif choice6 == 3:
                                                input_address2 = input("###ENTER NEW ADDRESS:")
                                                cur.execute("UPDATE USER1 SET U_ADDRESS = '{}' WHERE U_ID = '{}';".format(input_address2,input_id2))
                                                cnxn.commit()
                                                print("###USER DETAIL UPDATED SUCCESSFULLY!!!")
                                            elif choice6 == 4:
                                                input_city2 = input("###ENTER NEW CITY:")
                                                cur.execute("UPDATE USER1 SET CITY = '{}' WHERE U_ID = '{}';".format(input_city2,input_id2))
                                                cnxn.commit()
                                                print("###USER DETAIL UPDATED SUCCESSFULLY!!!")
                                            elif choice6 == 5:
                                                input_mobile2 = input("###ENTER NEW MOBILE NUMBER:")
                                                cur.execute("UPDATE USER1 SET U_MOBILE = {} WHERE U_ID = '{}';".format(input_mobile2,input_id2))
                                                cnxn.commit()
                                                print("###USER DETAIL UPDATED SUCCESSFULLY!!!")
                                            elif choice6 == 6:
                                                input_password2 = input("###ENTER NEW PASSWORD:")
                                                cur.execute("UPDATE USER1 SET U_PWD = '{}' WHERE U_ID = '{}';".format(input_password2,input_id2))
                                                cnxn.commit()
                                                print("###USER DETAIL UPDATED SUCCESSFULLY!!!")
                                            else:
                                                print("###INVALID CHOICE!!!")
                                            edit_sameuser = input("DO YOU WANT TO EDIT MORE OF THE SAME USER?(Y/N)")
                                edit_more = input("###DO YOU WANT TO EDIT MORE USERS?(Y/N)")

                    elif choice3 == 4:
                        cur.execute("SELECT * FROM USER1;")
                        result = cur.fetchall()
                        count6 = cur.rowcount
                        delete_more = "y"
                        while delete_more.lower() == "y":
                            print("""###USER CAN BE DELETED ON BASIS OF\n\t\t1.USER_ID\n\t\t2.USER_NAME\n\t\t3.MOBILE NUMBER""")
                            choice7 = int(input("###ENTER CHOICE:"))
                            if choice7 == 1:
                                input_id3 = input("###ENTER USER_ID TO DELETE:")
                                count7 = 0
                                for row in result:
                                    if row[0] == input_id3:
                                        count7 += 1
                                if count7 == 0:
                                    print("###USER_ID NOT FOUND")
                                else:
                                    print("THE DETAILS OF GIVEN USER_ID ARE:")
                                    print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME","AGE","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                    for row in result:
                                        if row[0] == input_id3:
                                            USER_ID, USER_NAME, AGE, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                            print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME,AGE,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))
                                    delete_sure1 = input("###ARE YOU SURE YOU WANT TO DELETE THIS USER?(Y/N)")
                                    cur.execute("DELETE FROM USER1 WHERE U_ID = '{}'".format(input_id3))
                                    cnxn.commit()
                                    print("###USER DELETED SUCCESSFULLY")
                            elif choice7 == 2:
                                input_name4 = input("###ENTER USER_NAME TO DELETE:")
                                count8 = 0
                                for row in result:
                                    if row[1] == input_name4:
                                        count8 += 1
                                if count8 == 0:
                                    print("###USER_NAME NOT FOUND")
                                else:
                                    print("THE DETAILS OF GIVEN USER_NAME ARE:")
                                    print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME", "AGE","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                    for row in result:
                                        if row[1] == input_name4:
                                            USER_ID, USER_NAME, AGE, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                            print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME,AGE,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))
                                    delete_sure1 = input("###ARE YOU SURE YOU WANT TO DELETE THIS USER?(Y/N)")
                                    cur.execute("DELETE FROM USER1 WHERE U_NAME = '{}';".format(input_name4))
                                    cnxn.commit()
                                    print("###USER DELETED SUCCESSFULLY")
                            elif choice7 == 3:
                                input_mobile4 = int(input("###ENTER USER_MOBILE TO DELETE:"))
                                count8 = 0
                                for row in result:
                                    if row[5] == input_mobile4:
                                        count8 += 1
                                if count8 == 0:
                                    print("###USER_MOBILE NOT FOUND")
                                else:
                                    print("THE DETAILS OF GIVEN USER_MOBILE ARE:")
                                    print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID","USER_NAME","AGE","USER_ADDRESS","USER_CITY","MOBILE_NO","PASSWORD"))
                                    for row in result:
                                        if row[5] == input_mobile4:
                                            USER_ID, USER_NAME, AGE, USER_ADDRESS, USER_CITY, MOBILE_NO, PASSWORD = row
                                            print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(USER_ID,USER_NAME,AGE,USER_ADDRESS,USER_CITY,MOBILE_NO,PASSWORD))
                                    delete_sure1 = input("###ARE YOU SURE YOU WANT TO DELETE THIS USER?(Y/N)")
                                    cur.execute("DELETE FROM USER1 WHERE U_MOBILE = {};".format(input_mobile4))
                                    cnxn.commit()
                                    print("###USER DELETED SUCCESSFULLY")
                            delete_more = input("DO YOU WANT TO DELETE MORE USERS?(Y/N)")

                #ADMIN SITE: MEDICINE SECTION......
                elif choice2 == 2:
                    print("###WELCOME TO MEDICINE SECTION")
                    med_more1 = "y"
                    while med_more1.lower() == "y":
                        print("""SELECT ANY FUNCTIONALITY:\n\t\t1.SEARCH FOR A MEDICINE\n\t\t2.ADD A NEW MEDICINE\n\t\t3.EDIT DETAILS OF EXISTING MEDICINE\n\t\t4.DELETE AN EXISTING MEDICINE""")
                        choicem1 = int(input("###ENTER CHOICE:"))
                        if choicem1 == 1:
                            search_more2 = "y"
                            while search_more2.lower() == "y":
                                print("""SELECT OPTION TO VIEW MEDICINES:\n\t\t0.SHOW ALL EXISTING MEDICINES\n\t\t1.SEARCH BY MEDICINE_ID\n\t\t2.SEARCH BY MEDICINE_NAME""")
                                cur.execute("SELECT * FROM MEDICINE1;")
                                result = cur.fetchall()
                                countm1 = cur.rowcount
                                choicem2 = int(input("###ENTER CHOICE:"))
                                if choicem2 == 0:
                                    if countm1 == 0:
                                        print("###SORRY!!!NO MEDICINE DETAILS IN TABLE")
                                    else:
                                        print("{:<10} {:<30} {:<10} {:<10}".format("MED_ID", "MED_NAME", "MED_PRICE","AVAILABILTY"))
                                        for row in result:
                                            MED_ID, MED_NAME, MED_PRICE, AVAILABILTY = row
                                            print("{:<10} {:<30} {:<10} {:<10}".format(MED_ID, MED_NAME, MED_PRICE,AVAILABILTY))
                                elif choicem2 == 1:
                                    if countm1 == 0:
                                        print("###SORRY!!!NO MEDICINE DETAILS IN TABLE")
                                    countm2 = 0
                                    input_mid1 = input("###ENTER MEDICINE_ID TO SEARCH:")
                                    for row in result:
                                        if row[0] == input_mid1:
                                            countm2 += 1
                                    if countm2 == 0:
                                        print("###SORRY!!!NO MEDICINE DETAILS FOR GIVEN MEDICINE_ID EXIST IN TABLE")
                                    else:
                                        print("{:<10} {:<30} {:<10} {:<10}".format("MED_ID", "MED_NAME", "MED_PRICE","AVAILABILTY"))
                                        for row in result:
                                            if row[0] == input_mid1:
                                                MED_ID, MED_NAME, MED_PRICE, AVAILABILTY = row
                                                print("{:<10} {:<30} {:<10} {:<10}".format(MED_ID, MED_NAME, MED_PRICE,AVAILABILTY))
                                elif choicem2 == 2:
                                    if countm1 == 0:
                                        print("###SORRY!!!NO MEDICINE DETAILS IN TABLE")
                                    countm3 = 0
                                    input_name1 = input("###ENTER MEDICINE_NAME TO SEARCH:")
                                    for row in result:
                                        if row[1] == input_name1:
                                            countm3 += 1
                                    if countm3 == 0:
                                        print("###SORRY!!!NO MEDICINE DETAILS FOR GIVEN MEDICINE_NAME EXIST IN TABLE")
                                    else:
                                        print("{:<10} {:<30} {:<10} {:<10}".format("MED_ID", "MED_NAME", "MED_PRICE","AVAILABILTY"))
                                        for row in result:
                                            if row[1] == input_name1:
                                                MED_ID, MED_NAME, MED_PRICE, AVAILABILTY = row
                                                print("{:<10} {:<30} {:<10} {:<10}".format(MED_ID, MED_NAME, MED_PRICE,AVAILABILTY))
                                else:
                                    print("###INVALID CHOICE!!!")
                                search_more2 = input("###DO YOU WANT TO SEARCH MORE?(Y/N)")
                        elif choicem1 == 2:
                            add_more2 = "y"
                            while add_more2.lower() == "y":
                                add_id2 = input("###ENTER MEDICINE_ID:")
                                add_name2 = input("###ENTER MEDICINE_NAME:")
                                add_price2 = float(input("###ENTER PRICE:"))
                                add_availability = int(input("###ENTER AVAILABILITY:"))
                                cur.execute("INSERT INTO MEDICINE1 VALUES('{}','{}',{},{});".format(add_id2, add_name2, add_price2,add_availability))
                                cnxn.commit()
                                print("###MEDICINE ADDED SUCCESSFULLY!!!")
                                add_more2 = input("###DO YOU WANT TO ADD MORE MEDICINE?(Y/N)")
                        elif choicem1 == 3:
                            update_more2 = "y"
                            cur.execute("SELECT * FROM MEDICINE1;")
                            result = cur.fetchall()
                            countm1 = cur.rowcount
                            while update_more2.lower() == "y":
                                print("""###YOU CAN EDIT MEDICINE DETAIL ON BASIS OF MEDICINE_ID""")
                                choicem3 = 1
                                if choicem3 == 1:
                                    input_mid2 = input("###ENTER MEDICINE_ID TO UPDATE:")
                                    if countm1 == 0:
                                        print("###SORRY!!!NO MEDICINE DETAILS IN TABLE")
                                    countm4 = 0
                                    for row in result:
                                        if row[0] == input_mid2:
                                            countm4 += 1
                                    if countm4 == 0:
                                        print("###MEDICINE_ID NOT FOUND IN TABLE")
                                    else:
                                        print("###CURRENT DETAILS OF GIVEN MEDICINE_ID IS:")
                                        print("{:<10} {:<30} {:<10} {:<10}".format("MED_ID", "MED_NAME", "MED_PRICE","AVAILABILTY"))
                                        for row in result:
                                            if row[0] == input_mid2:
                                                MED_ID, MED_NAME, MED_PRICE, AVAILABILTY = row
                                                print("{:<10} {:<30} {:<10} {:<10}".format(MED_ID, MED_NAME, MED_PRICE,AVAILABILTY))
                                        print("""###SELECT THE OPTION TO BE UPDATED\n\t\t1.NAME\n\t\t2.PRICE\n\t\t3.AVAILABILITY""")
                                        editsamemed = "y"
                                        while editsamemed.lower() == "y":
                                            choicem4 = int(input("###ENTER CHOICE:"))
                                            if choicem4 == 1:
                                                update_name2 = input("###ENTER NEW NAME:")
                                                cur.execute("UPDATE MEDICINE1 SET M_NAME = '{}' WHERE M_ID = '{}';".format(update_name2,input_mid2))
                                                cnxn.commit()
                                                print("###MEDICINE NAME UPDATED SUCCESSFULLY!!!")
                                            if choicem4 == 2:
                                                update_price2 = float(input("###ENTER NEW PRICE:"))
                                                cur.execute("UPDATE MEDICINE1 SET M_PRICE = {} WHERE M_ID = '{}';".format(update_price2,input_mid2))
                                                cnxn.commit()
                                                print("###MEDICINE PRICE UPDATED SUCCESSFULLY!!!")
                                            if choicem4 == 3:
                                                update_availability2 = input("###ENTER NEW AVAILABILITY:")
                                                cur.execute("UPDATE MEDICINE1 SET M_AVAILABILITY = {} WHERE M_ID = '{}';".format(update_availability2,input_mid2))
                                                cnxn.commit()
                                                print("###MEDICINE AVAILABILITY UPDATED SUCCESSFULLY!!!")
                                            editsamemed = input("DO YOU WANT TO UPDATE MORE DETAILS OF SAME MEDICINE?(Y/N)")
                                update_more2 = input("DO YOU WANT TO UPDATE MORE MEDICINE DETAILS?(Y/N)")
                        elif choicem1 == 4:
                            cur.execute("SELECT * FROM MEDICINE1;")
                            result = cur.fetchall()
                            countm1 = cur.rowcount
                            delete_more2 = "y"
                            while delete_more2.lower() == "y":
                                print("""MEDICINE DETAILS CAN BE DELETED ON BASIS OF:\n\t\t1.MEDICINE_ID\n\t\t2.MEDICINE_NAME""")
                                choicem5 = int(input("###ENTER CHOICE:"))
                                if choicem5 == 1:
                                    delete_mid2 = input("###ENTER MEDICINE_ID TO DELETE:")
                                    if countm1 == 0:
                                        print("###NO DETAILS IN MEDICINE TABLE")
                                    count5 = 0
                                    for row in result:
                                        if row[0] == delete_mid2:
                                            count5 += 1
                                    if count5 == 0:
                                        print("###GIVEN MEDICINE_ID DOES NOT EXIST IN MEDICINE TABLE")
                                    else:
                                        cur.execute("DELETE FROM MEDICINE1 WHERE M_ID = '{}';".format(delete_mid2))
                                        cnxn.commit()
                                        print("###DETAILS OF GIVEN MEDICINE_ID ARE DELETED SUCCESSFULLY!!!")
                                elif choicem5 == 2:
                                    delete_mname2 = input("###ENTER MEDICINE_NAME TO DELETE:")
                                    if countm1 == 0:
                                        print("###NO DETAILS IN MEDICINE TABLE")
                                    count5 = 0
                                    for row in result:
                                        if row[1] == delete_mname2:
                                            count5 += 1
                                    if count5 == 0:
                                        print("###GIVEN MEDICINE_NAME DOES NOT EXIST IN MEDICINE TABLE")
                                    else:
                                        cur.execute("DELETE FROM MEDICINE1 WHERE M_NAME = '{}';".format(delete_mname2))
                                        cnxn.commit()
                                        print("###DETAILS OF GIVEN MEDICINE_NAME ARE DELETED SUCCESSFULLY!!!")
                                delete_more2 = input("###DO YOU WANT TO DELETE MORE MEDICINES?(Y/N)")
                        med_more1 = input("###DO YOU WANT TO ACCESS MORE DETAILS IN MEDICINE SECTION?(Y/N)")

                #ADMIN SITE: ORDER SECTION......
                elif choice2 == 3:
                    print("###WELCOME TO ORDER SECTION!!!")
                    print("###SELECT ANY OF THE OPTIONS:\n\t\t1.VIEW ORDER DETAILS\n\t\t2.EDIT ORDER DETAILS\n\t\t3.DELETE ORDER DETAILS")
                    choiceo1 = int(input("###ENTER CHOICE:"))
                    if choiceo1 == 1:
                        view_moreo1 = "y"
                        while view_moreo1.lower() == "y":
                            print("###SELECT AN OPTION TO VIEW ORDERS:\n\t\t0.SHOW ALL ORDERS\n\t\t1.SHOW ALL ORDERS STILL NOT DELIVERED\n\t\t2.SEARCH BY USER_ID\n\t\t3.SEARCH BY MED_ID")
                            choiceo2 = int(input("###ENTER CHOICE:"))
                            cur.execute("SELECT * FROM ORDER1;")
                            result = cur.fetchall()
                            counto1 = cur.rowcount
                            if choiceo2 == 0:
                                if counto1 == 0:
                                    print("###SORRY!!!NO DETAILS IN ORDERS TABLE TO DISPLAY")
                                else:
                                    print("{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format("U_ID", "MED_ID", "QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                    for row in result:
                                        U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                        print("{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format(U_ID, MED_ID, QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                            elif choiceo2 == 1:
                                if counto1 == 0:
                                    print("###SORRY!!!NO DETAILS IN ORDERS TABLE TO DISPLAY")
                                else:
                                    counto2 = 0
                                    for row in result:
                                        if row[3].lower() == "pending":
                                            counto2 += 1
                                    if counto2 == 0:
                                        print("###NO PENDING ORDERS!!!")
                                    else:
                                        print("{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL", ))
                                        for row in result:
                                            if row[3].lower() == "pending":
                                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                                print("{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                            elif choiceo2 == 2:
                                if counto1 == 0:
                                    print("###SORRY!!!NO DETAILS IN ORDERS TABLE TO DISPLAY")
                                else:
                                    search_uido1 = input("###ENTER USER_ID TO SEARCH:")
                                    counto3 = 0
                                    for row in result:
                                        if row[0] == search_uido1:
                                            counto3 += 1
                                    if counto3 == 0:
                                        print("###NO ORDERS OF GIVEN ID!!!")
                                    else:
                                        print(
                                            "{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            if row[0] == search_uido1:
                                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                                print("{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                            elif choiceo2 == 3:
                                if counto1 == 0:
                                    print("###SORRY!!!NO DETAILS IN ORDERS TABLE TO DISPLAY")
                                else:
                                    search_mido1 = input("###ENTER MEDICINE_ID TO SEARCH:")
                                    counto4 = 0
                                    for row in result:
                                        if row[1] == search_mido1:
                                            counto4 += 1
                                    if counto4 == 0:
                                        print("###NO ORDERS OF GIVEN MEDICINE!!!")
                                    else:
                                        print("{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            if row[0] == search_mido1:
                                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                                print("{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                            view_moreo1 = input("###DO YOU WANT TO VIEW MORE ORDERS(Y/N)")
                    elif choiceo1 == 2:
                        update_moreo1 = "y"
                        cur.execute("SELECT * FROM ORDER1;")
                        result = cur.fetchall()
                        counto1 = cur.rowcount
                        while update_moreo1.lower() == "y":
                            print("""###SELECT THE OPTION TO EDIT AN ORDER ON BASIS OF BOTH USER_ID AND MEDICINE_ID""")
                            choiceo5 = 3
                            if counto1 == 0:
                                print("###NO DETAILS IN ORDER TABLE TO UPDATE")
                            if choiceo5 == 1:
                                update_ido1 = input("###ENTER USER_ID TO UPDATE:")
                                counto9 = 0
                                for row in result:
                                    if row[0] == update_ido1:
                                        counto9 += 1
                                    if counto9 == 0:
                                        print("###NO ORDERS OF GIVEN USER_ID IN TABLE")
                                    else:
                                        print("CURRENT ORDERS OF GIVEN USER_ID ARE:")
                                        print("{:<10} {:<10} {:<10} {:<20} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            if row[0] == update_ido1:
                                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                                print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                        print("###THIS OPTION UPDATES ALL ORDERS OF GIVEN USER_ID")
                                        print("###SELECT THE OPTION TO BE UPDATED:\n\t\t1.DELIVERY_STATUS\n\t\t2.PAYMENT_STATUS")
                                        choiceo06 = int(input("###ENTER CHOICE:"))
                                        if choiceo06 == 1:
                                            update_delivery_status = input("###ENTER STATUS TO UPDATE:(DELIVERED/PENDING)")
                                            cur.execute("UPDATE ORDER1 SET DELIVERY_STATUS = '{}' WHERE U_ID = '{}';".format(update_delivery_status, update_ido1))
                                            cnxn.commit()
                                            print("###DELIVERY_STATUS UPDATED SUCCESSFULLY")
                                        elif choiceo06 == 2:
                                            update_payment_status = input("###ENTER STATUS TO UPDATE:(PAID/PENDING)")
                                            cur.execute("UPDATE ORDER1 SET PAYMENT_STATUS = '{}' WHERE U_ID = '{}';".format(update_payment_status, update_ido1))
                                            cnxn.commit()
                                            print("###PAYMENT_STATUS UPDATED SUCCESSFULLY")
                                        else:
                                            print("###INVALID CHOICE")

                            elif choiceo5 == 2:
                                update_mido1 = input("###ENTER MEDICINE_ID TO UPDATE:")
                                counto9 = 0
                                for row in result:
                                    if row[1] == update_mido1:
                                        counto9 += 1
                                    if counto9 == 0:
                                        print("###NO ORDERS OF GIVEN USER_ID IN TABLE")
                                    else:
                                        print("CURRENT ORDERS OF GIVEN USER_ID ARE:")
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            if row[0] == update_mido1:
                                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                                print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                        print("###THIS OPTION UPDATES ALL ORDERS OF GIVEN MEDICINE_ID")
                                        print("###SELECT THE OPTION TO BE UPDATED:\n\t\t1.DELIVERY_STATUS\n\t\t2.PAYMENT_STATUS")
                                        choiceo06 = int(input("###ENTER CHOICE:"))
                                        if choiceo06 == 1:
                                            update_delivery_status = input("###ENTER STATUS TO UPDATE:(DELIVERED/PENDING)")
                                            cur.execute("UPDATE ORDER1 SET DELIVERY_STATUS = '{}' WHERE M_ID = '{}';".format(update_delivery_status, update_mido1))
                                            cnxn.commit()
                                            print("###DELIVERY_STATUS UPDATED SUCCESSFULLY")
                                        elif choiceo06 == 2:
                                            update_payment_status = input("###ENTER STATUS TO UPDATE:(PAID/PENDING)")
                                            cur.execute("UPDATE ORDER1 SET PAYMENT_STATUS = '{}' WHERE M_ID = '{}';".format(update_payment_status, update_mido1))
                                            cnxn.commit()
                                            print("###PAYMENT_STATUS UPDATED SUCCESSFULLY")
                                        elif choiceo06 == 3:
                                            update_delivery_contact = input("###ENTER NEW CONTACT NUMBER:")
                                            cur.execute("UPDATE ORDER1 SET DELIVERY_CONTACT = '{}' WHERE M_ID = '{}';".format(update_delivery_contact, update_mido1))
                                            cnxn.commit()
                                            print("###DELIVERY_CONTACT UPDATED SUCCESSFULLY")
                                        else:
                                            print("###INVALID CHOICE")
                            elif choiceo5 == 3:
                                update_ido2 = input("###ENTER USER_ID WHO MADE THE ORDER TO UPDATE:")
                                update_mido2 = input("###ENTER MEDICINE_ID TO UPDATE:")
                                counto8 = 0
                                for row in result:
                                    if row[0] == update_ido2 and row[1] == update_mido2:
                                        counto8 += 1
                                if counto8 == 0:
                                    print("###NO ORDERS OF GIVEN DETAILS")
                                else:
                                    print("CURRENT ORDERS OF GIVEN USER_ID AND MEDICINE_ID ARE:")
                                    print(
                                        "{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID", "QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                    for row in result:
                                        if row[0] == update_ido2 and row[1] == update_mido2:
                                            U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL, = row
                                            print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                    print("###THIS OPTION UPDATES ALL ORDERS OF GIVEN USER_ID AND MEDICINE_ID")
                                    print("###SELECT THE OPTION TO BE UPDATED:\n\t\t1.DELIVERY_STATUS\n\t\t2.PAYMENT_STATUS")
                                    choiceo06 = int(input("###ENTER CHOICE:"))
                                    if choiceo06 == 1:
                                        update_delivery_status = input("###ENTER STATUS TO UPDATE:(DELIVERED/PENDING)")
                                        cur.execute("UPDATE ORDER1 SET DELIVERY_STATUS = '{}' WHERE U_ID = '{}' AND M_ID = '{}';".format(update_delivery_status, update_ido2, update_mido2))
                                        cnxn.commit()
                                        print("###DELIVERY_STATUS UPDATED SUCCESSFULLY")
                                    elif choiceo06 == 2:
                                        update_payment_status = input("###ENTER STATUS TO UPDATE:(PAID/PENDING)")
                                        cur.execute("UPDATE ORDER1 SET PAYMENT_STATUS = '{}' WHERE U_ID = '{}' AND M_ID = '{}';".format(update_payment_status, update_ido2, update_mido2))
                                        cnxn.commit()
                                        print("###PAYMENT_STATUS UPDATED SUCCESSFULLY")
                                    else:
                                        print("###INVALID CHOICE")
                            else:
                                print("###INVALID CHOICE")
                            update_moreo1 = input("###DO YOU WANT TO UPDATE MORE ORDER DETAILS?(Y/N)")
                    elif choiceo1 == 3:

                        delete_moreo1 = "y"
                        while delete_moreo1.lower() == "y":
                            cur.execute("SELECT * FROM ORDER1;")
                            result = cur.fetchall()
                            counto1 = cur.rowcount
                            print("###SELECT AN OPTION TO DELETE AN ORDER DETAIL:\n\t\t1.ON BASIS OF USER_ID\n\t\t2.ON BASIS OF MEDICINE_ID\n\t\t3.ON BASIS OF BOTH")
                            choiceo7 = int(input("###ENTER CHOICE:"))
                            if counto1 == 0:
                                print("###NO DETAILS IN TABLE TO DELETE")
                            elif choiceo7 == 1:
                                delete_ido1 = input("###ENTER USER_ID TO DELETE:")
                                counto9 = 0
                                for row in result:
                                    if row[0] == delete_ido1:
                                        counto9 += 1
                                    if counto9 == 0:
                                        print("###NO ORDERS OF GIVEN USER_ID IN TABLE")
                                    else:
                                        print("CURRENT ORDERS OF GIVEN USER_ID ARE:")
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            if row[0] == delete_ido1:
                                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                                print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                        print("###THIS OPTION DELETES ALL ORDERS OF GIVEN USER_ID")
                                        cur.execute("DELETE FROM ORDER1 WHERE U_ID = '{}';".format(delete_ido1))
                                        cnxn.commit()
                                        print("###ORDERS OF GIVEN USER_ID ARE DELETED")
                            elif choiceo7 == 2:
                                delete_mido1 = input("###ENTER MEDICINE_ID TO DELETE:")
                                counto9 = 0

                                for row in result:
                                    if row[1] == delete_mido1:
                                        counto9 += 1
                                    if counto9 == 0:
                                        print("###NO ORDERS OF GIVEN MEDICINE_ID IN TABLE")
                                    else:
                                        print("CURRENT ORDERS OF GIVEN MEDICINE_ID ARE:")
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            if row[1] == delete_mido1:
                                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                                print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                        print("###THIS OPTION DELETES ALL ORDERS OF GIVEN MEDICINE_ID")
                                        cur.execute("DELETE FROM ORDER1 WHERE M_ID = '{}';".format(delete_mido1))
                                        cnxn.commit()
                                        print("###ORDERS OF GIVEN MEDICINE_ID ARE DELETED")
                            elif choiceo7 == 3:
                                delete_ido2 = input("###ENTER USER_ID TO DELETE:")
                                delete_mido2 = input("###ENTER MEDICINE_ID TO DELETE:")
                                counto9 = 0
                                for row in result:
                                    if row[0] == delete_ido2 and row[1] == delete_mido2:
                                        counto9 += 1
                                    if counto9 == 0:
                                        print("###NO ORDERS OF GIVEN DETAILS IN TABLE")
                                    else:
                                        print("CURRENT ORDERS OF GIVEN DETAILS ARE:")
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            if row[0] == delete_ido2 and row[1] == delete_mido2:
                                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                                print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                        print("###THIS OPTION DELETES ALL ORDERS OF GIVEN DETAILS")
                                        cur.execute("DELETE FROM ORDER1 WHERE U_ID = '{}' AND M_ID = '{}';".format(delete_ido2,delete_mido2))
                                        cnxn.commit()
                                        print("###ORDERS OF GIVEN DETAILS ARE DELETED")
                            else:
                                print("###INVALID CHOICE")
                            delete_moreo1 = input("###DO YOU WANT TO DELETE MORE ORDER DETAILS?(Y/N)")
                    else:
                        print("###INVALID CHOICE")
                else:
                    print("###INVALID CHOICE")
                admin_more = input("###DO YOU WANT TO PERFORM ANY OTHER FUNCTION IN ADMIN SITE?(Y/N)")


# USER SITE
    elif choice1 == 2:
        print("#_#" * 25)
        print("HELLO USER!!!!WE FEEL GLAD THAT YOU USE OUR SERVICE")
        user_more1 = "y"
        while user_more1.lower() == "y":
            print("###SELECT AN OPTION TO ACCESS OUR SERVICE\n\t\t1.LOGIN TO AN EXISTING USER\n\t\t2.CREATE A NEW ACCOUNT")
            uchoice1 = int(input("###ENTER CHOICE:"))
            u_id, u_name, u_age, u_address, u_city, u_mobile, u_pwd = "", "", 0, "", "", 0, ""
            if uchoice1 == 1:
                id_check01 = "n"
                while id_check01 == "n":
                    uinput_id = input("###ENTER YOUR VALID USER_ID:")
                    cur.execute("SELECT * FROM USER1;")
                    result = cur.fetchall()
                    for row in result:
                        if row[0] == uinput_id:
                            id_check01 = "y"
                            u_id, u_name, u_age, u_address, u_city, u_mobile, u_pwd = row
                    if id_check01 == "n":
                        print("###GIVEN USER_ID IS NOT VALID")
                id_check02 = "n"
                while id_check02 == "n":
                    uinput_pwd = input("###ENTER YOUR PASSWORD:")
                    if uinput_pwd == u_pwd:
                        id_check02 = "y"
                    else:
                        print("###GIVEN PASSWORD IS INCORRECT.TRY AGAIN")
                print("###LOGIN SUCCESSFUL")
            elif uchoice1 == 2:
                uinput_id = ""
                uid_check3 = "n"
                while uid_check3 == "n":
                    uinput_id = input("###ENTER A VALID USER_D:(LIKE'UXXXXXX')")
                    cur.execute("SELECT * FROM USER1;")
                    result = cur.fetchall()
                    ucount1 = 0
                    for row in result:
                        if row[0] == uinput_id:
                            ucount1 += 1
                    if ucount1 != 0:
                        print("###GIVEN USER_ID IS ALREADY TAKEN")
                    else:
                        uid_check3 = "y"
                u_id = uinput_id
                u_name = input("###ENTER YOUR NAME:")
                u_age = int(input("###ENTER YOUR AGE:"))
                u_address = input("###ENTER YOUR ADDRESS:")
                u_city = input("###ENTER THE CITY YOU LIVE IN:")
                u_mobile = int(input("###ENTER YOUR MOBILE NUMBER:"))
                u_pwd = ""
                uid_check4 = "n"
                while uid_check4 == "n":
                    uinput_pwd1 = input("###ENTER YOUR PASSWORD:")
                    uinput_pwd2 = input("###RE-ENTER YOUR PASSWORD TO CONFIRM:")
                    if uinput_pwd1 == uinput_pwd2:
                        u_pwd = uinput_pwd1
                        uid_check4 = "y"
                    else:
                        print("BOTH PASSWORDS DOESN'T MATCH.TRY AGAIN.")
                cur.execute("INSERT INTO USER1 VALUES('{}','{}',{},'{}','{}',{},'{}');".format(u_id, u_name, u_age, u_address,u_city, u_mobile, u_pwd))
                cnxn.commit()
                print("SIGNUP SUCCESSFUL")
            else:
                print("###INVALID CHOICE")
            print("_-_-"*30)
            print("###HELLO {}!!!WE FEEL HAPPY FOR YOU TO BE A PART OF US.".format(u_name.upper()))
            user_more2 = "y"
            while user_more2.lower() == "y":
                print("SELECT ANY OPTION:\n\t\t1.MANAGE ACCOUNT\n\t\t2.BUY A MEDICINE\n\t\t3.MANAGE MY ORDERS\n\t\t4.EXIT")
                uchoice2 = int(input("###ENTER CHOICE:"))

                #USER SITE: ACCOUNT SECTION......
                if uchoice2 == 1:
                    print("###SELECT A FEATURE TO MANAGE YOUR ACCOUNT:\n\t\t1.UPDATE MY PERSONAL DATA\n\t\t2.DELETE MY ACCOUNT")
                    uchoice3 = int(input("###ENTER CHOICE:"))
                    if uchoice3 == 1:
                        print("###YOUR CURRENT DETAILS ARE:")
                        print("###THE CURRENT USER DETAILS ARE:")
                        print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format("USER_ID", "NAME", "AGE","ADDRESS","CITY", "MOBILE_NO","PASSWORD"))
                        print("{:<10} {:<20} {:<10} {:<30} {:<15} {:<15} {:<20}".format(u_id, u_name, u_age, u_address,u_city,u_mobile, u_pwd))
                        print("###CHOOSE THE DETAIL TO BE UPDATED:\n\t\t1.AGE\n\t\t2.ADDRESS\n\t\t3.CITY\n\t\t4.MOBILE_NO")
                        editmore123 = "y"
                        while editmore123.lower() == "y":
                            uchoice4 = int(input("ENTER AN OPTION:"))
                            if uchoice4 == 1:
                                update_age1 = int(input("ENTER NEW AGE:"))
                                cur.execute("UPDATE USER1 SET U_AGE = {} WHERE U_ID = '{}';".format(update_age1, u_id))
                                cnxn.commit()
                                print("###AGE UPDATED SUCCESSFULLY")
                            elif uchoice4 == 2:
                                update_address1 = input("ENTER NEW ADDRESS:")
                                cur.execute("UPDATE USER1 SET U_ADDRESS = '{}' WHERE U_ID = '{}';".format(update_address1, u_id))
                                cnxn.commit()
                                print("###ADDRESS UPDATED SUCCESSFULLY")
                            elif uchoice4 == 3:
                                update_city1 = input("ENTER NEW CITY:")
                                cur.execute("UPDATE USER1 SET CITY = '{}' WHERE U_ID = '{}';".format(update_city1, u_id))
                                cnxn.commit()
                                print("###CITY UPDATED SUCCESSFULLY")
                            elif uchoice4 == 4:
                                update_mno1 = int(input("ENTER NEW MOBILE NUMBER:"))
                                cur.execute("UPDATE USER1 SET U_MOBILE = {} WHERE U_ID = '{}';".format(update_mno1, u_id))
                                cnxn.commit()
                                print("###MOBILE NUMBER UPDATED SUCCESSFULLY")
                            else:
                                print("###INVALID CHOICE")
                            editmore123 = input("DO YOU WANT TO EDIT MORE DETAILS?(Y/N)")

                    if uchoice3 == 2:
                        delete_user = input("ARE YOU SURE YOU WANT TO DELETE THIS ACCOUNT?(Y/N)")
                        if delete_user.lower() == "y":
                            cur.execute("DELETE FROM USER1 WHERE U_ID = '{}';".format(u_id))
                            cnxn.commit()
                            print("WE HAD A GREAT PLEASURE IN PROVIDING YOU WITH OUR SERVICE.WE HOPE YOU'LL BE BACK SOON.")
                            deleted = "y"

                #USER SITE: MEDICINE SECTION......
                elif uchoice2 == 2:
                    ubuy_more = "y"
                    while ubuy_more.lower() == "y":
                        buy_mname = input("###ENTER NAME OF THE MEDICINE:")
                        cur.execute("SELECT * FROM MEDICINE1 WHERE M_NAME = '{}';".format(buy_mname))
                        result = cur.fetchall()
                        umedcount = cur.rowcount
                        if umedcount == 0:
                            print("###SORRY FOR THE INCONVENIENCE!!!IT SEEMS THAT NO MEDICINE IS AVAILABLE WITH GIVEN NAME.")
                        else:
                            print("THE DETAILS OF REQUIRED MEDICINE ARE:")
                            print("{:<10} {:<30} {:<10} {:<10}".format("MED_ID", "MED_NAME", "MED_PRICE", "AVAILABILTY"))
                            MED_ID = ""
                            AVAILABILITY = 0
                            MED_PRICE = 0
                            for row in result:
                                MED_ID, MED_NAME, MED_PRICE, AVAILABILITY = row
                                print("{:<10} {:<30} {:<10} {:<10}".format(MED_ID, MED_NAME, MED_PRICE, AVAILABILITY))
                            buy_check = input("###ARE YOU SURE THAT YOU WANT TO ORDER THIS MEDICINE?(Y/N)")
                            if buy_check == "y":
                                buy_quantity = int(input("###ENTER THE NUMBER OF UNITS YOU WANT TO BUY:"))
                                if buy_quantity >= AVAILABILITY:
                                    print("SORRY!!! WE ARE NOT LEFT WITH THIS MANY UNITS IN STOCK.WE KINDLY REQUEST YOU TO CHECK ON THIS MEDICINE SHORTLY FOR STOCK UPDATION.")
                                else:
                                    total_bill = MED_PRICE * buy_quantity
                                    pay_check = "n"
                                    print("###SELECT YOUR PAYMENT OPTION:\n\t\t1.CASH ON DELIVERY\n\t\t2.CREDIT CARD")
                                    payment_choice = int(input("###ENTER YOUR CHOICE:"))
                                    PAYMENT_STATUS = ""
                                    if payment_choice == 1:
                                        print("###YOU WILL BE ASKED TO PAY THE BILL DIRECTLY TO THE DELIVERY MAN.TILL THEN YOUR PAYMENT STATUS WILL BE KEPT AS 'PENDING'.")
                                        pay_check = "y1"
                                        PAYMENT_STATUS = "PENDING"
                                    elif payment_choice == 2:
                                        credit_card_no = int(input("###ENTER YOUR CREDIT CARD NUMBER:"))
                                        credit_card_pwd = int(input("###ENTER YOUR CREDIT CARD PASSWORD(THIS WILL BE SURELY KEPT IN A SECURE DATA STORAGE):"))
                                        pay_check = "y2"
                                        PAYMENT_STATUS = "PAID"
                                    else:
                                        print("###INVALID CHOICE")
                                    if pay_check[0] == "y":
                                        if pay_check == "y1":
                                            cur.execute("INSERT INTO ORDER1 VALUES('{}','{}',{},'PENDING','PENDING',{});".format(u_id,MED_ID,buy_quantity,total_bill))
                                        elif pay_check == "y2":
                                            cur.execute("INSERT INTO ORDER1 VALUES('{}','{}',{},'PENDING','PAID',{});".format(u_id,MED_ID,buy_quantity,total_bill))
                                        cur.execute("UPDATE MEDICINE1 SET M_AVAILABILITY = M_AVAILABILITY - {} WHERE M_ID = '{}';".format(buy_quantity, MED_ID))
                                        cnxn.commit()
                                        print("###THANKS FOR TRUSTING US!!!!")
                                        print("DETAILS OF YOUR ORDER ARE:")
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(u_id, MED_ID,buy_quantity,"PENDING",PAYMENT_STATUS,total_bill))
                        ubuy_more = input("DO YOU WANT TO BUY MORE MEDICINES?(Y/N)")

                #USER SITE: ORDERS SECTION......
                elif uchoice2 == 3:
                    orders_more = "y"
                    while orders_more.lower() == "y":
                        print("SELECT ANY OPTION TO PERFORM:\n\t\t1.VIEW MY ORDERS\n\t\t2.EDIT MY ORDERS\n\t\t3.DELETE ORDER")
                        uchoice7 = int(input("###ENTER CHOICE:"))
                        if uchoice7 == 1:
                            uview_more = "y"
                            while uview_more == "y":
                                print("SELECT AN OPTION:\n\t\t0.SHOW ALL MY ORDERS\n\t\t1.SHOW ORDERS THAT ARE NOT DELIVERED YET\n\t\t2.SHOW ORDERS THAT ARE NOT PAID YET")
                                uchoice3 = int(input("###ENTER CHOICE:"))
                                if uchoice3 == 0:
                                    cur.execute("SELECT * FROM ORDER1 WHERE U_ID = '{}';".format(u_id))
                                    result = cur.fetchall()
                                    ucount1 = cur.rowcount
                                    if ucount1 == 0:
                                        print("###SORRY!!!NO ORDERS MADE FROM YOUR USER_ID")
                                    else:
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                            print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                elif uchoice3 == 1:
                                    cur.execute("SELECT * FROM ORDER1 WHERE U_ID = '{}' AND DELIVERY_STATUS = 'PENDING';".format(u_id))
                                    result = cur.fetchall()
                                    ucount1 = cur.rowcount
                                    if ucount1 == 0:
                                        print("###SORRY!!!IT SEEMS THAT ALL YOUR ORDERS ARE DELIVERED!!!")
                                    else:
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                            print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                elif uchoice3 == 2:
                                    cur.execute("SELECT * FROM ORDER1 WHERE U_ID = '{}' AND PAYMENT_STATUS = 'PENDING';".format(u_id))
                                    result = cur.fetchall()
                                    ucount1 = cur.rowcount
                                    if ucount1 == 0:
                                        print("###SORRY!!!IT SEEMS THAT ALL YOUR ORDERS ARE PAID!!!")
                                    else:
                                        print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format("U_ID", "MED_ID","QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                        for row in result:
                                            U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                            print("{:<10} {:<10} {:<10} {:<10} {:<20} {:<15}".format(U_ID, MED_ID,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                else:
                                    print("###INVALID CHOICE")
                                uview_more = input("DO YOU WANT TO VIEW MORE ORDERS?(Y/N)")
                        elif uchoice7 == 2:
                            update_more = "y"
                            while update_more.lower() == "y":
                                print("YOU CAN ONLY EDIT THE UNITS OF MEDICINE YOU ORDERED")
                                print("YOUR CURRENT ORDERS TILL NOT DELIVERED ARE:")
                                cur.execute("SELECT * FROM ORDER1 WHERE U_ID = '{}' AND PAYMENT_STATUS = 'PENDING';".format(u_id))
                                result = cur.fetchall()
                                ucount1 = cur.rowcount
                                cur.execute("SELECT M_ID,M_NAME FROM MEDICINE1;")
                                resultm = cur.fetchall()
                                order_mlist = []
                                U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = "","",0,"","",0
                                if ucount1 == 0:
                                    print("###SORRY!!!NO PENDING ORDERS EXIST FOR YOUR USER_ID")
                                else:
                                    print("{:<10} {:<10} {:<20} {:<10} {:<20} {:<20} {:<15}".format("U_ID", "MED_ID","M_NAME", "QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                    for row in result:
                                        if row[3] == "PENDING":
                                            m_name = ""
                                            U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                            for mrow in resultm:
                                                if mrow[0] == MED_ID:
                                                    m_name = mrow[1]
                                                    order_mlist.append(mrow)
                                            print("{:<10} {:<10} {:<20} {:<10} {:<20} {:<20} {:<15}".format(U_ID, MED_ID,m_name,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                    mname_check = "n"
                                    update_mid = ""
                                    update_mname = ""
                                    while mname_check == "n":
                                        update_mname = input("###ENTER NAME OF MEDICINE TO UPDATE THE ORDER:")
                                        for row in order_mlist:
                                            if row[1] == update_mname:
                                                update_mid = row[0]
                                                mname_check = "y"
                                        if mname_check == "n":
                                            print("###THE GIVEN MEDICINE IS NOT VALID.TRY AGAIN.")
                                    cur.execute("SELECT * FROM MEDICINE1 WHERE M_ID = '{}';".format(update_mid))
                                    resultm1 = cur.fetchone()
                                    old_quantity = resultm1[3]
                                    quantity_check = "n"
                                    new_quantity = 0
                                    while quantity_check == "n":
                                        new_quantity = int(input("ENTER NEW NUMBER OF UNITS REQUIRED:"))
                                        if new_quantity - QUANTITY <= old_quantity:
                                            quantity_check = "y"
                                        else:
                                            print("###SORRY!!!WE DO NOT HAVE ENOUGH STOCK FOR YOUR REQUIREMENT.TRY ENTERING A SMALLER NUMBER.")
                                    total_diff = new_quantity - QUANTITY
                                    cur.execute("UPDATE ORDER1 SET QUANTITY = {} WHERE U_ID = '{}' AND M_ID = '{}';".format(new_quantity,u_id,update_mid))
                                    cur.execute("UPDATE MEDICINE1 SET M_AVAILABILITY = M_AVAILABILITY - {} WHERE M_ID = '{}';".format(total_diff,update_mid))
                                    cur.execute("UPDATE ORDER1 SET TOTAL_BILL = TOTAL_BILL + (TOTAL_BILL/{})*{} WHERE U_ID = '{}' AND M_ID = '{}';".format(QUANTITY,QUANTITY,u_id,update_mid))
                                    cnxn.commit()
                                update_more = input("###DO YOU WANT TO UPDATE MORE ORDERS?(Y/N)")
                        elif uchoice7 == 3:
                            delete_more = "y"
                            while delete_more.lower() == "y":
                                print("###YOU CAN DELETE ORDERS WHICH ARE NOT YET DELIVERED")
                                print("###YOUR CURRENT ORDERS TILL NOT DELIVERED ARE:")
                                cur.execute("SELECT * FROM ORDER1 WHERE U_ID = '{}' AND DELIVERY_STATUS = 'PENDING';".format(u_id))
                                result = cur.fetchall()
                                ucount1 = cur.rowcount
                                cur.execute("SELECT M_ID,M_NAME FROM MEDICINE1;")
                                resultm = cur.fetchall()
                                delete_mlist = []
                                QUANTITY = 0
                                if ucount1 == 0:
                                    print("###SORRY!!!IT SEEMS THAT ALL YOUR ORDERS ARE DELIVERED!!!NO ORDER DETAILS CAN BE DELETED!!!")
                                else:
                                    print("{:<10} {:<10} {:<20} {:<10} {:<20} {:<20} {:<15}".format("U_ID", "MED_ID", "M_NAME", "QUANTITY","DELIVERY_STATUS","PAYMENT_STATUS","TOTAL_BILL"))
                                    for row in result:
                                        if row[3] == "PENDING":
                                            m_name = ""
                                            U_ID, MED_ID, QUANTITY, DELIVERY_STATUS, PAYMENT_STATUS, TOTAL_BILL = row
                                            for mrow in resultm:
                                                if mrow[0] == MED_ID:
                                                    m_name = mrow[1]
                                                    delete_mlist.append(mrow)
                                            print("{:<10} {:<10} {:<20} {:<10} {:<20} {:<20} {:<15}".format(U_ID, MED_ID,m_name,QUANTITY,DELIVERY_STATUS,PAYMENT_STATUS,TOTAL_BILL))
                                mname_check = "n"
                                delete_mid = ""
                                delete_mname = ""
                                while mname_check == "n":
                                    delete_mname = input("###ENTER NAME OF MEDICINE TO DELETE THE ORDER:")
                                    for row in delete_mlist:
                                        if row[1] == delete_mname:
                                            delete_mid = row[0]
                                            mname_check = "y"
                                    if mname_check == "n":
                                        print("###THE GIVEN MEDICINE IS NOT VALID")
                                cur.execute("DELETE FROM ORDER1 WHERE M_ID = '{}';".format(delete_mid))
                                cur.execute("UPDATE MEDICINE1 SET M_AVAILABILITY = M_AVAILABILITY + {} WHERE M_ID = {};".format(QUANTITY,delete_mid))
                                cnxn.commit()
                                delete_more_more = input("###DO YOU WANT TO DELETE MORE ORDERS?(Y/N)")
                        else:
                            print("###INVALID CHOICE")
                        orders_more = input("DO YOU WANT TO USE ANY MORE FUNCTIONALITY OF ORDER SECTION?(Y/N)")
                elif uchoice2 == 4:
                    print("THANK YOU FOR VISITING OUR SITE!!!WE LOOK FORWARD FOR MORE MOMENTS WITH YOU...")
                else:
                    print("###INVALID CHOICE")
                user_more2 = input("DO YOU WANT TO CARRY OUT ANY OTHER FUNCTIONALITY IN YOUR SITE?(Y/N)")
            user_more1 = input("DO YOU WANT TO USE ANY OTHER FUNCTIONALITY IN AN USER SITE?(Y/N)")

    elif choice1 != 0:
        print("###INVALID CHOICE")
    quit1 = input("DO YOU WANT TO QUIT?(Y/N):")
    if quit1 == "y":
        print("!!!THANKS FOR USING OUR SERVICE. WE'LL BE EAGERLY WAITING FOR YOUR RETURN")

cnxn.close()

#THE END...........
