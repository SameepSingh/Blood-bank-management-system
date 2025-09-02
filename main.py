print("\t\t WELCOME TO THE HEARTLAND BLOOD DONATION CENTRE")
print("\t\t\tAN INITIAITIVE SAVING LIVES")


def enter():
    ent = str(input("PRESS ENTER TO PROCEED"))


import mysql.connector as m
import random as r

con = m.connect(host="localhost", user="root", password="Tiger@80804", database="blood_bank")


def dash():
    print(
        "--------------------------------------------------------------------------------------------")


def under():
    print(
        "_____________________________________________________________________________________________")


def star():
    print(
        "*********************************************************************************************")



cur = con.cursor()


def display(C="", D=""):
    if D.upper() == "STAFF":
        under()
        who3 = input("Enter the phone number or ID :")
        under()

        if C == 1:
            q4 = "select NAME ,LAST_DATE_of_blood_received ,blood_Group,donor_id from {} where ID='{}' OR PHONE_NO='{}' ".format(
                constants(C), who3, who3)
            l1 = ["NAME", "LAST DATE OF RECEIVING BLOOD", "BLOOD GROUP", "DONOR'S ID WHO DONATED BLOOD"]
        elif C == 2:
            q4 = "select NAME ,LAST_DATE_of_donation ,blood_group,patient_ID from {} where ID='{}' OR PHONE_NO='{}' ".format(
                constants(C), who3, who3)
            l1 = ["NAME", "LAST DATE OF DONATION", "BLOOD GROUP", "PATIENT'S ID WHO RECEIVED BLOOD"]
        cur.execute(q4)
        gama = cur.fetchall()

        N = 0
        star()
        for i in gama:
            for j in i:
                if j == "":
                    j = "N/A"
                print(N + 1, l1[N] + ": " + j)
                N = N + 1

        star()
        enter()
    elif D.upper() == "ADMIN":
        star()
        print("Type 'F' for full information ")
        print("Type 'G'  to be a combined information about patient and the related donor")
        print("TYPE 'C' to get the count of staff")
        print("Type 'A' to check the availability")
        star()

        under()
        aak1 = input("Choose one Option:")
        print()

        under()

        print()

        if aak1.upper() == "F":
            print("Type 1 for 'PATIENT'")
            print("Type 2 for 'DONOR'")
            print("Type 3 for 'EMPLOYEE'")
            who1 = int(input("enter the designation of person who's information has to be displayed:"))
            C = who1
            if C == 3:
                aak2 = input("Enter the ID of the staff:")
                l1 = ["ID", "PASSWORD", 'NAME ', "PHONE NUMBER", 'ADDRESS', 'SHIFT DURATION', 'DESIGNATION', 'DOB']
                q = "select * from staff where  id='{}'".format(aak2)

                cur.execute(q)
                v = cur.fetchall()

                dash()
                for i in v:
                    N = 0
                    for j in i:
                        print(str(N + 1) + " " + l1[N], " : ", j)
                        N = N + 1
                dash()
                enter()

                print()

            elif C == 1:
                aak2 = input("Enter the ID of the patient:")
                q1 = "select * from patient where  id='{}'".format(aak2)
                l1 = ["ID", "PASSWORD ", "NAME", "ADDRESS", "PHONE NUMBER ", "DONOR'S ID WHO DONATED THE BLOOD",
                      "BLOOD GROUP", "LAST DATE WHEN BLOOD WAS RECEIVED"]

                cur.execute(q1)
                v = cur.fetchall()

                N = 0
                dash()
                for i in v:

                    for j in i:
                        if j == "":
                            j == "N/A"
                        print(str(N + 1) ,l1[N] , " : " + j)
                        N = N + 1
                dash()
                enter()
            elif C == 2:
                aak2 = input("Enter the ID of the donor:")
                q2 = "select * from donor where  id='{}'".format(aak2)
                l1 = ["ID OF THE DONOR", "PASSWORD OF DONOR ", "NAME OF DONOR", "ADDRESS OF DONOR", "PHONE NUMBER OF DONOR ", "PATINT'S ID WHO RECEIVED THE BLOOD",
                      "BLOOD GROUP OF DONOR", "LAST DATE WHEN BLOOD  WAS DONATED BY THE DONOR","AVAILABILITY STATUS"]

                cur.execute(q2)
                v = cur.fetchall()

                N = 0
                dash()
                for i in v:

                    for j in i:

                        if j == "":
                            j = "N/A"
                        print(str(N + 1), l1[N] , " : " , j)
                        N = N + 1
                dash()
                enter()

        elif aak1.upper() == "G":

            aak2 = input("Enter the ID of the patient:")

            N = 0
            l1 = ["ID OF PATIENT", "NAME OF PATIENT", "ADDRESS OF PATIENT", "PHONE NUMBER OF PATIENT ", "DONOR'S ID WHO DONATED THE BLOOD",
                  "BLOOD GROUP OF PATIENT", "LAST DATE WHEN BLOOD WAS RECEIVED BY PATIENT"]
            l2 = ["NAME OF THE DONOR", "ADDRESS OF DONOR", "PHONE NUMBER OF DONOR "]
            l3 = l1 + l2
            q5 = "select  patient.id,patient.name,patient.address,patient.phone_no,patient.donor_id,patient.blood_group,patient.last_date_of_blood_received,donor.name,donor.address,donor.phone_no from patient  join donor  on patient.donor_id=donor.id where patient.id='{}'".format(
                aak2)
            cur.execute(q5)
            ww3 = cur.fetchall()
            dash()
            for z in ww3:

                for h in z:
                    if h == "":
                        h = "N/A"
                    print(str(N + 1), l3[N], ":", h)
                    N = N + 1
            dash()
            enter()
        elif aak1.upper() == 'C':

            Q = "select designation,count(*) from staff group by designation"
            cur.execute(Q)
            l1 = ["DESIGNATION", "COUNT"]

            s = cur.fetchall()
            dash()
            for i in s:
                N = 0  # TO ENABLE ITERATION

                for j in i:
                    print(N + 1, l1[N], ":", j)
                    N = N + 1
            dash()
            enter()
        elif aak1.upper() == "A":
            under()
            ask16 = input("Enter your Blood group:")
            c = "select  blood_group,count(*) from donor where blood_group='{}' and availability='Y' ".format(ask16)
            cur.execute(c)
            a = cur.fetchall()
            l1 = ["BLOOD GROUP", "COUNT"]
            N = 0
            dash()
            for i in a:
                for j in i:

                    if j == None:
                        j = ask16.upper()
                    print(N + 1, l1[N], ":", j)
                    N = N + 1
            dash()
            enter()


def register():
    star()
    print("Press 'N' if you don't have a registered account")
    print()
    print("Type 'R' if you are a registered user")
    star()
    global reg
    reg = input("Do you have an registered account:")
    if reg.upper() == "R":
        password()
    else:
        print("Type 'P' for 'PATIENT'")
        print("Type 'D' for 'DONOR'")
        ask7 = input("Choose one option")
        admin(constants(ask7))
def password():
    global _phid, _pass, who
    star()
    print("Type 'P' for 'PATIENT'")
    print("Type 'D' for 'DONOR'")
    print("Type 'E' for 'STAFF'")

    star()
    under()
    who = str(input("Pls enter your designation:"))
    _phid = str(input("Enter your phone number or ID :"))

    _pass = input("Enter your password:")
    under()
    table(who)
def available():
    q = "select blood_group ,count(*) from donor group by blood_group where availability='Y'  "
    cur.execute(q)
    charlie = cur.fetchall()

    l1 = ["BLOOD GROUP", "QUANTITY LEFT"]
    dash()
    print("LIST OF BLOOD GROUPS ")
    for i in charlie:
        N = 0
        star()
        for j in i:
            print(N + 1, l1[N], " : ", j, sep=" ", end="\t\n")

            N = N + 1

    print()
    print()




def admin(desi, what="edit"):
    while True:

        global who1
        ask4 = ""

        a = "patient"
        b = "donor"

        c = "employee"

        if desi.upper() == "ADMIN":
            star()
            print("Type 'E' to insert ")
            print("Type 'V' to view   ")
            print("Type 'U' to update")
            print("Type 'D' for delete")
            print("Type 'B' to exit")
            star()

            under()
            ask4 = input("what do you want to do:")

            under()
        if ask4.upper() == "B":

            bye("C")
            break


        elif desi.upper() == "PATIENT":
            who1 = 1
        elif desi.upper() == "DONOR":
            who1 = 2
        elif desi.upper() == "STAFF" or ask4.upper() == "E" or ask4.upper() == "U" or ask4.upper() == "D" or ask4.upper() == "V":

            if ask4.upper() == "V":
                display(D=desi)
                who1=""


            else:
                under()
                print("Type 1 for 'PATIENT'")
                print("Type 2 for 'DONOR'")
                if  desi.upper() == "ADMIN":
                    print("Type 3 for 'EMPLOYEE'")
                if what.upper() == "DISPLAY":
                    who1 = int(input("Enter the designation of person  who's information has to be displayed:"))
                    under()
                else:
                    who1 = int(input("enter the designation of person who's entry has to be done :"))
                under()
                if what == "update" or ask4.upper() == "U":
                    update(who1, desi)

                    print("INFORMATION IS UPDATED")
                    enter()
                    who1=""




                elif ask4.upper() == "D":

                    delete(who1, desi)
                    print("THE  RECORD OF THE GIVEN  ID  IS DELETED ")
                    enter()
                    who1=""




                elif what == "display":

                    display(who1, desi)
                    who1=""



        if who1 == 3:

            if desi.upper() == "ADMIN":
                while True:
                    ID = r.randint(1000000000, 9999999999)
                    print("ID=",ID)
                    _pass = input("enter the password to be assigned to the " + c + ":")
                    name = str(input("Enter the name of the " + c + ":"))
                    add = input("enter the address of the " + c + ":")
                    phone = str(input("enter the phone number of the " + c + ":"))
                    oper = str(input("enter the duration hours of the " + c + ":"))
                    desig = input("enter the designation of the " + c + ":")
                    DOB = input("Enter the date of birth (YYYY,MM,DD):")
                    query = "insert into staff values({},'{}','{}','{}',{},{},'{}','{}')".format(ID, _pass, name, add,
                                                                                                 phone, oper, desig, DOB)

                    ask = input("Confirm(y=yes/n=redo)")
                    if ask.upper() == "Y":
                        cur.execute(query)
                        con.commit()
                        ask2 = input("Do you want to add more records:(Y/N)")
                        if ask2.upper() == "Y":
                            pass
                        else:
                            print("Redirecting to main menu")


                    else:
                        enter()
                        continue
            elif desi.upper() == "STAFF":
                print("Access not granted")
                print("REDIRECTING TO THE LOGIN WINDOW")
                password()
        if who1 == 1:
            while True:
                ID2 = r.randint(100000000, 999999999)
                print("ID=", ID2)
                _pass = input("enter the password to be assigned :")
                name = str(input("Enter the name of the " + a + ":"))
                add = input("enter the address of the " + a + ":")
                phone = str(input("enter the phone number of the " + a + ":"))
                donor_ID = ""
                Blood = input("Blood group of the " + a + ":")

                got = ""

                query1 = "insert into patient values({},'{}','{}','{}',{},'{}','{}','{}')".format(ID2, _pass, name,
                                                                                                  add,
                                                                                                  phone, donor_ID,
                                                                                                  Blood, got)

                ask = input("Do you want to continue[VERIFY THE DATA](y=yes/n=redo):")
                if ask.upper() == "Y":
                    cur.execute(query1)
                    con.commit()
                    if desi.upper() == "PATIENT":
                        print("REDIRECTING TO THE LOGIN PAGE")
                        print()
                        password()
                        break
                    else:
                        ask2 = input("do you want to add more records:(Y/N)")

                    if ask2.upper() == "Y":
                        pass
                    else:
                        star()
                        print("REDIRECTING TO THE MAIN MENU")
                        star()


                else:
                    dash()
                    continue
        if who1 == 2:
            while True:
                ID2 = r.randint(100000000, 999999999)
                print("ID=", ID2)
                _pass = input("enter the password  to be assigned :")
                name = str(input("Enter the name of the " + b + ":"))
                add = input("enter the address of the " + b + ":")
                phone = str(input("enter the phone number of the " + b + ":"))



                patient_ID = ""
                Blood = input("Blood group of the " + b + ":")
                if desi.upper() == "ADMIN" or desi.upper() == "STAFF":
                    giv=input("Enter the date of donation:")
                else:
                    giv = ""
                ava="Y"

                query2 = "insert into donor values({},'{}','{}','{}',{},'{}','{}','{}','{}')".format(ID2, _pass, name, add,
                                                                                                phone, patient_ID,
                                                                                                Blood, giv,ava)

                ask = input("Do you want to continue[VERIFY THE ENTRIES](y=yes/n=redo):")
                if ask.upper() == "Y":
                    cur.execute(query2)
                    con.commit()
                    if desi.upper() == "DONOR":
                        password()
                        break

                    else:
                        ask2 = input("do you want to add more records:(Y/N)")
                    if ask2.upper() == "Y":
                        pass
                    else:

                        star()
                        print("REDIRECTING TO THE MAIN MENU")
                        star()
                else:
                    dash()
                    continue


def update(w, what="staff"):
    counter = 0
    if counter == 0:
        pass
    else:
        enter()
    if w == 2:
        counter = counter + 1
        q1 = "select * from donor"
        cur.execute(q1)
        delta = cur.fetchall()
        print("Type N to update 'NAME'")
        print("Type A to update 'ADDRESS'")
        print("Type H to update 'PHONE_NO'")

        print("Type B to update 'BLOOD GROUP'")
        if what.lower() == "staff" or what.upper() == "ADMIN":
            print("Type PI to update 'PATIENT_ID'")
            print("Type LD to update 'LAST DATE OF BLOOD DONATED'")

        print()
        ch = input("Choose one option from the list fiven above: ")
        if what.upper() == "STAFF" or what.upper() == "ADMIN":
            ask8 = str(input("Enter the ID  /Phone Number of candidate who information has to be edited"))

        else:
            ask8 = _phid
        ch2 = input("Enter the amendment:")
        for i in delta:
            if ask8 == i[0] or ask8 == i[4]:
                q = "update {} set {}='{}' where ID='{}'".format(constants(w), constants(ch.upper()), ch2, ask8)
                cur.execute(q)
                con.commit()

                if ch.upper() == "LD":

                    ques=input("WANT TO UPDATE THE AVAILABILITY STATUS TO 'YES' (Y/N):")
                    if ques.upper()=="Y":
                        q2 = "update donor set availability='Y' where id='{}'".format(ask8)
                        cur.execute(q2)
                        con.commit()
                    else:
                        pass


                elif ch.upper() == "PI":

                    q2 =  "update donor set availability='N' where id='{}'".format(ask8)
                    cur.execute(q2)
                    con.commit()



    elif w == 1:
        conter = counter + 1
        q = "select * from {}".format(constants(w))
        cur.execute(q)
        delta = cur.fetchall()

        print("Type N to update 'NAME'")
        print("Type A to update 'ADDRESS'")
        print("Type H to update 'PHONE_NO'")

        print("Type B to update 'BLOOD GROUP'")
        if what == "staff" or what == "admin":
            print("Type I to update 'DONOR_ID'")
            print("Type L to update 'DATE  WHEN BLOOD WAS RECEIVED'")

        print()
        ch = input("Choose one option from the list fiven above: ")

        if what.upper() == "STAFF" or what.upper() == "ADMIN":
            ask8 = str(input("Enter the ID  /Phone Number of candidate who information has to be edited"))

        else:
            ask8 = _phid
        ch2 = input("Enter the amendment:")
        for i in delta:
            if ask8 == i[0] or ask8 == i[4]:
                q = "update {} set {}='{}' where ID='{}'".format(constants(w), constants(ch.upper()), ch2, ask8)
                cur.execute(q)
                con.commit()

                if ch.upper() == "L":
                    patient_id = input("Enter the DONOR ID who's blood is given:")
                    q2 = "update patient set donor_id='{}' where ID='{}'".format(patient_id, ask8)
                    cur.execute(q2)
                    con.commit()
                    q3 = "update donor set patient_id='{}'  where id='{}'".format(ask8, patient_id)

                    cur.execute(q3)
                    con.commit()

                    q4 = "update donor set availability='N' where ID='{}'".format(patient_id)

                    cur.execute(q4)
                    con.commit()
                elif ch.upper() == "I":
                    last = input("Enter the   date of  receiving blood (YYYY-MM-DD):")
                    q2 = "update patient set last_date_of_blood_received='{}' where ID='{}'".format(last, ask8)
                    cur.execute(q2)
                    con.commit()
                    q3 = "update donor set patient_id='{}' where id='{}'".format(ask8,ch2)

                    q4 = "update donor set availability='N' where ID='{}' ".format(ch2)

                    cur.execute(q4)
                    con.commit()
                    cur.execute(q3)
                    con.commit()


    elif w == 3 and what.upper() == "ADMIN":
        counter = counter + 1
        q = "select * from {}".format(constants(w))
        cur.execute(q)
        delta = cur.fetchall()
        print("Type N to update 'NAME'")
        print("Type A to update 'ADDRESS'")
        print("Type H to update 'PHONE_NO'")
        print("Type DE to update 'DESIGNATION'")
        print("Type OH to update 'OPERATING HOURS'")
        print("Type  DOB to update 'DATE OF BIRTH' ")
        print()
        ch = input("Choose one option from the list fiven above: ")

        ask8 = str(input("Enter the ID  /Phone Number of candidate who information has to be edited"))

        ch2 = input("Enter the amendment:")
        for i in delta:
            if ask8 == i[0] or ask8 == i[4]:
                q = "update {} set {}='{}' where ID='{}'".format(constants(w), constants(ch.upper()), ch2, ask8)
                cur.execute(q)
                con.commit()
                admin()
                return
    else:
        print("ACCESS NOT GRANTED ")


def staff(_phi):
    counter = 0
    while True:
        if counter == 0:
            pass
        else:
            enter()
        star()
        print("TYPE D TO DISPLAY INFORMATION")
        print("TYPE I TO INSERT")
        print("TYPE E TO EDIT")

        print("TYPE F TO CHECK THE LEFT OVER QUANTITIES OF BLOOD GROUPS")
        print("TYPE B TO EXIT")

        star()

        under()
        ask6 = input("Choose one option:")
        under()

        if ask6 == "B":

            bye("C")
            break
        elif ask6.upper() == "D":
            counter = counter + 1
            d = "select * from staff"
            cur.execute(d)
            cc = cur.fetchall()
            for gg in cc:
                if gg[0]==_phi or gg[4]==_phi:

                    admin("staff", "display")


        elif ask6.upper() == "I":
            counter = counter + 1
            d = "select * from staff"
            cur.execute(d)
            cc = cur.fetchall()
            for gg in cc:
                if gg[0]==_phi or gg[4]==_phi:
                    if gg[6].upper() == "RECEPTIONIST":
                        admin("staff")

                    elif  not gg[6].upper() == "RECEPTIONIST" :
                        print("ACCESS NOT GRANTED")
                        print()
                        print("RETURNING BACK TO THE MAIN MENU ")



        elif ask6.upper() == "E":
            counter = counter + 1
            d = "select * from staff"
            cur.execute(d)
            cc = cur.fetchall()
            for gg in cc:
                if gg[0]==_phi or gg[4]==_phi:
                    if gg[6].upper() == "RECEPTIONIST" or gg[6].upper() == "DOCTOR":

                        admin("Staff", "update")

                    elif not gg[6].upper() == "RECEPTIONIST" or not gg[6].upper() == "DOCTOR":
                        print("ACCESS NOT GRANTED")
                        print()
                        print("RETURNING BACK TO THE MAIN MENU ")






        elif ask6.upper() == "F":

            counter = counter + 1
            d = "select * from staff"
            cur.execute(d)
            cc = cur.fetchall()
            for gg in cc:



                if gg[0] == _phi or gg[4] == _phi:
                    if gg[6].upper() == "RECEPTIONIST" or gg[6].upper() == "DOCTOR":
                        available()


                    elif not gg[6].upper() == "RECEPTIONIST" or not gg[6].upper() == "DOCTOR":
                        print("ACCESS NOT GRANTED")

                        print("RETURNING BACK TO THE MAIN MENU ")


def patient(Q):
    while True:
        star()
        print("Type 'A' to check availability")
        print("Type 'S'  to display your info")
        print("Type 'M' to edit your info")
        print("Type 'B' to exit")
        star()
        under()
        ask12 = input("Choose one option : ")
        under()
        if ask12.upper() == "A":


            ask16 = input("Enter your Blood group:")
            c = "select  distinct blood_group,availability from donor where blood_group='{}'".format(ask16)
            cur.execute(c)
            a = cur.fetchall()

            l1 = ["BLOOD GROUP", "AVAILABILITY STATUS"]

            dash()
            if a!=[]:
                for i in a:

                    N = 0
                    for j in i:
                        if N==1:
                            if j=="Y":
                                j="AVAILABLE "
                        elif N==1:
                            if j=="N":
                                j="NOT AVAILABLE"



                        print(N + 1, l1[N], ":",j )
                        N = N +1

            elif a==[]:
                print("1 ",l1[0],":",ask16)
                print("1 ", l1[1], " : UNAVAILABLE")
            dash()
            enter()


        elif ask12.upper() == "S":

            q1 = "select * from patient where phone_no='{}' or id='{}'".format(Q, Q)
            l1 = ["ID", "PASSWORD ", "NAME", "ADDRESS", "PHONE NUMBER ", "DONOR'S ID WHO DONATED THE BLOOD", "BLOOD GROUP",
                  "LAST DATE WHEN BLOOD WAS RECEIVED"]
            cur.execute(q1)
            mm = cur.fetchall()
            N = 0
            dash()
            for i in mm:

                for j in i:
                    if j == "":
                        j = "N/A"
                    print(N + 1, l1[N], " : ", j)
                    N = N + 1
            dash()
            enter()

        elif ask12.upper() == "M":

            update(1, "patient")
            print("YOUR INFORMATION HAS BEEN UPDATED")
            enter()
        elif ask12.upper()=="B":
            bye("C")
            return

def donor(Q):
    while True:
        star()

        print("Type 'S'  to display your info")
        print("Type 'M' to edit your info")
        print("Type 'B'to exit")
        star()
        under()
        ask12 = input("Choose one option : ")
        under()

        if ask12.upper() == "S":

            q1 = "select * from donor where phone_no='{}' or id='{}'".format(Q, Q)
            l1 = ["ID", "PASSWORD ", "NAME", "ADDRESS", "PHONE NUMBER ", "PATIENT'S ID WHO GOT THE BLOOD", "BLOOD GROUP",
                  "LAST DATE WHEN BLOOD WAS DONATED","AVAILABILITY STATUS"]
            cur.execute(q1)
            mm = cur.fetchall()
            N = 0
            dash()
            for i in mm:

                for j in i:
                    if j == "":
                        j = "N/A"
                    print(l1[N] + " : " + j)
                    N = N + 1
            dash()
            enter()


        elif ask12.upper() == "M":

            update(2, "donor")
            print("YOUR INFORMATION HAS BEEN UPDATED")
            enter()


        elif ask12.upper() == "B":

            break


def constants(x):
    if x == "P" or x == 1:
        return "Patient"
    elif x == "E" or x == 3:
        return "staff"

    elif x == "D" or x == 2:
        return "donor"
    elif x == "N":
        return "name"
    elif x == "H":
        return ("phone_no")
    elif x == "A":
        return ("Address")
    elif x == "I":
        return ("Donor_ID")
    elif x == "B":
        return ("blood_group")
    elif x == "L":
        return ("last_date_of_blood_recEIved")
    elif x == "PI":
        return ("patient_id")
    elif x == "LD":
        return ("last_date_of_donation")
    elif x == "DE":
        return "designation"
    elif x == "DOB":
        return ("DOB")
    elif x == "OH":
        return ("Shift_duration")
    elif x=="AV":
        return ("AVAILABILITY")

def forgot_pass():
    st = constants(who.upper())
    print("WELCOME TO FORGOT PASSWORD WINDOW")
    q1 = "select phone_no,Id from {}".format(constants(who.upper()))

    cur.execute(q1)

    beta = cur.fetchall()

    for i in beta:
        if i[1] == _phid or i[0] == _phid:
            under()
            new_p = input("Enter the new password:")
            q2 = "update {} set password='{}' where phone_no='{}' or  id='{}'".format(constants(who.upper()), new_p,
                                                                                      _phid, _phid)
            under()
            cur.execute(q2)
            con.commit()
        else:
            print("THE ID YOU HAVE ENTERED IS NOT VALID")
            under()
            print("REDIRECTING TO NEW REGISTRATION WINDOW")
            under()
            register()

    password()


def bye(x):
    if x.upper() == "F":
        dash()
        print("EITHER OF YOUR ID AND PASSWORD IS WRONG  ")
        dash()
        star()
        print("Type 1 to EXIT")
        print("Type 2 IF YOU HAD FORGOT PASSWORD")
        print("Type 3 to TRY AGAIN")
        star()
        under()
        ask3 = int(input("choose one option from the list given above"))
        under()
        if ask3 == 3:
            password()
        elif ask3 == 1:
            bye("C")
        elif ask3 == 2:
            forgot_pass()
    elif x.upper() == "C":
        a = constants(who.upper())
        print("THANK YOU DEAR:", a.upper())
        print("WE HOPE WE WERE ABLE TO PROVIDE YOU THE REQUIRED HELP")


def delete(r, what="staff"):
    under()
    ask10 = input("Enter the ID or  phone number of the candidate whose record has to be deleted: ")
    under()
    q = "select * from {}".format(constants(r))
    cur.execute(q)
    c = cur.fetchall()
    for i in c:
        if what.upper() == "STAFF" and (i[0] == ask10 or i[4] == ask10) and r != 3:

            q = "delete from {} where ID='{}' or phone_no='{}'".format(constants(r), ask10, ask10)
            cur.execute(q)
            con.commit()

        elif what.upper() == "ADMIN" and (i[0] == ask10 or i[4] == ask10):
            q = "delete from {} where ID='{}' or phone_no='{}'".format(constants(r), ask10, ask10)
            cur.execute(q)
            con.commit()  # ASK






def table(w):  # who designation
    n = 0

    q = "select * from {}".format(constants(who.upper()))

    cur.execute(q)
    alpha = cur.fetchall()

    for i in alpha:

        if w.upper() == "E":

            if i[1] == _pass and (i[0] == _phid or i[4] == _phid):

                if i[6].upper() == "ADMIN":
                    admin(i[6])
                    return
                else:
                    staff(_phid)
                    return
            else:
                n = n + 1
                if cur.rowcount == n:
                    bye("F")

        elif w.upper() == "P":

            if i[1] == _pass and (i[0] == _phid or i[4] == _phid):
                patient(_phid)

                break
            else:
                n = n + 1
                if cur.rowcount == n:
                    bye("F")
        elif w.upper() == "D":

            if i[1] == _pass and (i[0] == _phid or i[4] == _phid):
                donor(_phid)
                break
            else:
                n = n + 1
                if cur.rowcount == n:
                    bye("F")


register()