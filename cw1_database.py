import sqlite3
import os
import pandas as pd
con = sqlite3.connect("cw1.db")
cur = con.cursor()

p = 0
a = 0
f = 0
ap = 0

#create tables needed
#Check if pilot table exists
try:
    cur.execute("SELECT * FROM pilot")

except sqlite3.OperationalError:
    p = 1
    cur.execute("create table pilot (pilotid smallint unsigned primary key, firstname varchar(20), surname varchar(20))")

#Check if aircraft table exists
try:
    cur.execute("SELECT * FROM aircraft")

except sqlite3.OperationalError:
    a = 1
    cur.execute("create table aircraft (aircraftid smallint unsigned primary key, name varchar(20))")

#Check if flight table exists
try:
    cur.execute("SELECT * FROM flight")

except sqlite3.OperationalError:
    f = 1
    cur.execute("create table flight (flightid varchar(20), aircraftid smallint unsigned, destination varchar(20), departure varchar(20), dateofflight date, timeofflight time, FOREIGN KEY(aircraftid) REFERENCES aircraft(aircraftid))")

#Check if aircraftpilot table exists
try:
    cur.execute("SELECT * FROM aircraftpilot")

except sqlite3.OperationalError:
    ap = 1
    cur.execute("create table aircraftpilot (aircraftid smallint unsigned, pilotid smallint unsigned, FOREIGN KEY(aircraftid) REFERENCES aircraft(aircraftid),FOREIGN KEY(pilotid) REFERENCES pilot(pilotid))")


#insert sample data into pilot table
if p == 1:
    cur.execute("insert into pilot (pilotid, firstname, surname) values (1001, 'Ivan', 'Yeung'),(1002, 'Jim', 'Kwok'),(1003, 'Jason', 'Kwok'),(1004, 'Boris', 'Chang'),(1005, 'Milton', 'Lee'),(1006, 'Trinity', 'Ho'),(1007, 'Ivan', 'Lee'),(1008, 'Brian', 'Wu'),(1009, 'Edward', 'Wong'),(1010, 'Ian', 'Leung')")

#insert sample data into aircraft table
if a == 1:
    cur.execute("insert into aircraft (aircraftid, name) values (2111, 'Plane A'),(2112, 'Plane B'),(2113, 'Plane C'),(2114, 'Plane D'),(2115, 'Plane E'),(2116, 'Plane F'),(2117, 'Plane G'),(2118, 'Plane H'),(2119, 'Plane I'),(2110, 'Plane J')")

#insert sample data into aircraftpilot table
if ap == 1:
    cur.execute("insert into aircraftpilot (aircraftid, pilotid) values (2111,1001),(2111,1002),(2112,1003),(2112,1004),(2113,1005),(2113,1006),(2114,1007),(2114,1008),(2115,1009),(2115,1010),(2116,1001),(2116,1002),(2117,1003),(2117,1004),(2118,1005),(2118,1006),(2119,1007),(2119,1008),(2110,1009),(2110,1010)")

if f == 1:
    cur.execute("insert into flight (flightid, aircraftid, destination, departure, dateofflight, timeofflight) values ('AB1001', 2111, 'London', 'New York', '2023-10-17', '08:30:00'),('CC2002', 2112, 'Paris', 'Tokyo', '2023-10-18', '15:45:00'),('CD3113', 2113, 'Sydney', 'Los Angeles', '2023-10-19', '12:00:00'),('EJ3414', 2114, 'Dubai', 'Moscow', '2023-10-20', '10:15:00'),('JJ16479', 2115, 'Singapore', 'Hong Kong', '2023-10-21', '16:20:00'),('KX2786', 2116, 'Berlin', 'Rome', '2023-10-22', '14:30:00'),('HF4787', 2117, 'Toronto', 'Mexico City', '2023-10-23', '09:45:00'),('KG7428', 2118, 'Cairo', 'Athens', '2023-10-24', '11:00:00'),('KD8399', 2119, 'Seoul', 'Shanghai', '2023-10-25', '18:10:00'),('TR84210', 2110, 'Rio de Janeiro', 'Buenos Aires', '2023-10-26', '13:20:00'),('LK4711', 2111, 'Amsterdam', 'Madrid', '2023-10-27', '10:30:00'),('HK8312', 2112, 'Bangkok', 'Ho Chi Minh City', '2023-10-28', '17:40:00'),('VY0613', 2113, 'Stockholm', 'Helsinki', '2023-10-29', '14:50:00'),('TV9914', 2114, 'New Delhi', 'Mumbai', '2023-10-30', '09:00:00'),('PV7415', 2115, 'Sao Paulo', 'Lima', '2023-10-31', '11:15:00'),('UH0316', 2116, 'Vienna', 'Zurich', '2023-11-01', '18:25:00'),('UI9317', 2117, 'Jakarta', 'Kuala Lumpur', '2023-11-02', '15:35:00'),('GV0218', 2118, 'Dublin', 'Edinburgh', '2023-11-03', '10:45:00'),('QN7319', 2119, 'Brussels', 'Luxembourg', '2023-11-04', '12:55:00'),('OA2320', 2110, 'Budapest', 'Prague', '2023-11-05', '19:05:00')")


con.commit()

#Select function

def printmenu():
    os.system("clear")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("─██████████████─██████─────────██████████─██████████████─██████──██████─██████████████────████████████───██████████████───██████──────────██████─██████████████─")
    print("─██░░░░░░░░░░██─██░░██─────────██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██────██░░░░░░░░████─██░░░░░░░░░░██───██░░██████████████░░██─██░░░░░░░░░░██─")
    print("─██░░██████████─██░░██─────────████░░████─██░░██████████─██░░██──██░░██─██████░░██████────██░░████░░░░██─██░░██████░░██───██░░░░░░░░░░░░░░░░░░██─██░░██████████─")
    print("─██░░██─────────██░░██───────────██░░██───██░░██─────────██░░██──██░░██─────██░░██────────██░░██──██░░██─██░░██──██░░██───██░░██████░░██████░░██─██░░██─────────")
    print("─██░░██████████─██░░██───────────██░░██───██░░██─────────██░░██████░░██─────██░░██────────██░░██──██░░██─██░░██████░░████─██░░██──██░░██──██░░██─██░░██████████─")
    print("─██░░░░░░░░░░██─██░░██───────────██░░██───██░░██──██████─██░░░░░░░░░░██─────██░░██────────██░░██──██░░██─██░░░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─")
    print("─██░░██████████─██░░██───────────██░░██───██░░██──██░░██─██░░██████░░██─────██░░██────────██░░██──██░░██─██░░████████░░██─██░░██──██████──██░░██─██████████░░██─")
    print("─██░░██─────────██░░██───────────██░░██───██░░██──██░░██─██░░██──██░░██─────██░░██────────██░░██──██░░██─██░░██────██░░██─██░░██──────────██░░██─────────██░░██─")
    print("─██░░██─────────██░░██████████─████░░████─██░░██████░░██─██░░██──██░░██─────██░░██────────██░░████░░░░██─██░░████████░░██─██░░██──────────██░░██─██████████░░██─")
    print("─██░░██─────────██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─────██░░██────────██░░░░░░░░████─██░░░░░░░░░░░░██─██░░██──────────██░░██─██░░░░░░░░░░██─")
    print("─██████─────────██████████████─██████████─██████████████─██████──██████─────██████────────████████████───████████████████─██████──────────██████─██████████████─")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("\n")
    for i in range(56):
        print(" ",end="")
    print("Please choose the function that you want:")
    for i in range(67):
        print(" ",end="")
    print("1. View Record")
    for i in range(67):
        print(" ",end="")
    print("2. Search Record")
    for i in range(67):
        print(" ",end="")
    print("3. Add Record")
    for i in range(67):
        print(" ",end="")
    print("4. Update Record")
    for i in range(67):
        print(" ",end="")
    print("5. Delete Record")
    for i in range(67):
        print(" ",end="")
    print("6. Sql Query")
    for i in range(67):
        print(" ",end="")
    print("7. Exit")
    for i in range(67):
        print(" ",end="")
    print("Your Choice: ", end="")
    return()

def delete():
    loop = 0
    while (loop != 1) :
        query = ""
        l_tables = ["pilot","aircraft","flight","aircraftpilot"]
        l_tablekeys = ["pilotid","aircraftid","flightid","aircraftid"]
        print("List of tables:")
        print("1. Pilot\n2. Aircraft\n3. Flight\n4. AircraftPilot")
        print("Type 'back' to go back to main screen")
        print("Select a table: ", end='')
        choice = input()
        try:
            os.system("clear")
            if (choice == 'back'):
                break
            elif (choice == '1'):
                query = "Select * from pilot"
            elif (choice == '2'):
                query = "Select * from aircraft"
            elif (choice == '3'):
                query = "Select * from flight"
            elif (choice == '4'):
                query = "Select * from aircraftpilot"
            queryresult = pd.read_sql_query(query, con, index_col=None)
            print(queryresult.to_string(index=False))
            print("Type 'back' to go back to main screen")
            print("select the record that you want to delete (Please input the primary key): ")
            p_key = input()
            if type(p_key) is int:
                delete_query = "delete from " + l_tables[int(choice)-1] + " where " + l_tablekeys[int(choice)-1] + " = "  + p_key
            else:
                delete_query = "delete from " + l_tables[int(choice)-1] + " where " + l_tablekeys[int(choice)-1] + " = "  + "\'" + p_key + "\'"
            if (delete_query != 'back'):
                if (choice == '1'):
                    query = "Select * from pilot"
                elif (choice == '2'):
                    query = "Select * from aircraft"
                elif (choice == '3'):
                    query = "Select * from flight"
                elif (choice == '4'):
                    query = "Select * from aircraftpilot"
                cur.execute(delete_query)
                os.system("clear")
                print("Result: ")
                queryresult = pd.read_sql_query(query, con, index_col=None)
                print(queryresult.to_string(index=False))
                con.commit()
            else:
                os.system("clear")
        except:
            os.system("clear")
            print("Please input a valid input")
    return()

def insert():
    loop = 0
    while (loop != 1) :
        l_tables = ["pilot","aircraft","flight","aircraftpilot"]
        query_col = []
        query = ""
        print("List of tables:")
        print("1. Pilot\n2. Aircraft\n3. Flight\n4. AircraftPilot")
        print("Type 'back' to go back to main screen")
        print("Select which table you want to insert record(s): ", end='')
        choice = input()
        try:
            os.system("clear")
            if (choice == 'back'):
                break
            elif (choice == '1'):
                query = "Select * from pilot"
            elif (choice == '2'):
                query = "Select * from aircraft"
            elif (choice == '3'):
                query = "Select * from flight"
            elif (choice == '4'):
                query = "Select * from aircraftpilot"
            queryresult = pd.read_sql_query(query, con, index_col=None)
            print(queryresult.to_string(index=False))
            print_col = cur.execute(query)
            for i in print_col.description:
                print("Type the value of",end =" ")
                print (i[0], end = "")
                print (":")
                a = input()
                try:
                    a = int(a)
                except:
                    a = a
                query_col.append(a)
            insert_query = "insert into " + l_tables[int(choice)-1] + " ("
            for i in range(len(print_col.description)):
                if i != len(print_col.description) - 1:
                    insert_query = insert_query + print_col.description[i][0] + ", "
                else:
                    insert_query = insert_query + print_col.description[i][0]
            insert_query = insert_query + ") values (" 
            for j in range(len(query_col)):
                a = query_col[j]
                if (type(a) is int):
                    if j != len(query_col) - 1:
                        insert_query = insert_query + str(a) + ", "
                    else:
                        insert_query = insert_query + str(a)
                else:
                    if j != len(query_col) - 1:
                        insert_query = insert_query + "\'" + a + "\'" + ", "
                    else:
                        insert_query = insert_query + "\'" + a + "\'"
            insert_query = insert_query + ")"
            if (insert_query != 'back'):
                if (choice == '1'):
                    query = "Select * from pilot"
                elif (choice == '2'):
                    query = "Select * from aircraft"
                elif (choice == '3'):
                    query = "Select * from flight"
                elif (choice == '4'):
                    query = "Select * from aircraftpilot"
                cur.execute(insert_query)
                os.system("clear")
                print("Result: ")
                queryresult = pd.read_sql_query(query, con, index_col=None)
                print(queryresult.to_string(index=False))
                con.commit()
            else:
                os.system("clear")
        except:
            os.system("clear")
            print("Please use a valid input")
    return()

def update():
    loop = 0
    while (loop != 1) :
        l_tables = ["pilot","aircraft","flight","aircraftpilot"]
        l_tablekeys = ["pilotid","aircraftid","flightid","aircraftid"]
        query = ""
        p_key = ""
        col = ""
        print("List of tables:")
        print("1. Pilot\n2. Aircraft\n3. Flight\n4. AircraftPilot")
        print("Type 'back' to go back to main screen")
        print("Select which table you want to update: ", end='')
        choice = input()
        try:
            os.system("clear")
            if (choice == 'back'):
                break
            elif (choice == '1'):
                query = "Select * from pilot"
            elif (choice == '2'):
                query = "Select * from aircraft"
            elif (choice == '3'):
                query = "Select * from flight"
            elif (choice == '4'):
                query = "Select * from aircraftpilot"
            queryresult = pd.read_sql_query(query, con, index_col=None)
            print(queryresult.to_string(index=False))
            print("Select the record that you want to update (Please input the primary key):")
            p_key = input()
            p_key = str(p_key)
            print("Select the column that you want to update:")
            col = input()
            print("Please type the the new value:")
            val = input()
            if (type(val) is int and type(p_key) is int):
                update_query = "update " + l_tables[int(choice)-1] + " set " + col + " = " + val + " where " + l_tablekeys[int(choice)-1] + " = " + p_key
            elif (type(val) is str and type(p_key) is int):
                update_query = "update " + l_tables[int(choice)-1] + " set " + col + " = " + "\'" + val + "\'" + " where " + l_tablekeys[int(choice)-1] + " = " + p_key
            elif (type(val) is int and type(p_key) is str):
                update_query = "update " + l_tables[int(choice)-1] + " set " + col + " = " + val + " where " + l_tablekeys[int(choice)-1] + " = " + "\'" + p_key + "\'"
            elif (type(val) is str and type(p_key) is str):
                update_query = "update " + l_tables[int(choice)-1] + " set " + col + " = " + "\'" + val + "\'" + " where " + l_tablekeys[int(choice)-1] + " = " + "\'" + p_key + "\'"
            if (update_query != 'back'):
                if (choice == '1'):
                    query = "Select * from pilot"
                elif (choice == '2'):
                    query = "Select * from aircraft"
                elif (choice == '3'):
                    query = "Select * from flight"
                elif (choice == '4'):
                    query = "Select * from aircraftpilot"
                cur.execute(update_query)
                os.system("clear")
                print("Result: ")
                queryresult = pd.read_sql_query(query, con, index_col=None)
                print(queryresult.to_string(index=False))
                con.commit()
            else:
                os.system("clear")
        except:
            os.system("clear")
            print("Please input a valid input")
    return()

def search():
    loop = 0
    while (loop != 1) :
        print("Type 'back' to go back to main screen")
        print("Type the Flight ID to search: ")
        flightid = input()
        querypilot = "select pilot.firstname, pilot.surname from pilot join aircraftpilot on pilot.pilotid = aircraftpilot.pilotid join flight on aircraftpilot.aircraftid = flight.aircraftid where flight.flightid = \'" + flightid + "\'"
        queryflight = "select * from flight where flightid = \'" + flightid + "\'"
        try:
            os.system("clear")
            if (flightid == 'back'):
                break
            print("Flight details:")
            queryresult = pd.read_sql_query(queryflight, con, index_col=None)
            print(queryresult.to_string(index=False))
            print("Pilot details:")
            queryresult = pd.read_sql_query(querypilot, con, index_col=None)
            print(queryresult.to_string(index=False))

        except:
            print("Plese input a valid query")
    return()

def select():
    loop = 0
    while (loop != 1) :
        print("Type 'back' to go back to main screen")
        print("Type the query to choose what you want to search in the records: ")
        query = input()
        try:
            os.system("clear")
            if (query == 'back'):
                break
            queryresult = pd.read_sql_query(query, con, index_col=None)
            print(queryresult.to_string(index=False))
        except:
            print("Plese input a valid query")
    return()

def view():
    loop = 0
    while (loop != 1) :
        query = ""
        print("List of tables:")
        print("1. Pilot\n2. Aircraft\n3. Flight\n4. AircraftPilot")
        print("Type 'back' to go back to main screen")
        print("Select which table you want to view: ", end='')
        choice = input()
        try:
            os.system("clear")
            if (choice == 'back'):
                break
            elif (choice == '1'):
                query = "Select * from pilot"
            elif (choice == '2'):
                query = "Select * from aircraft"
            elif (choice == '3'):
                query = "Select * from flight"
            elif (choice == '4'):
                query = "Select * from aircraftpilot"
            queryresult = pd.read_sql_query(query, con, index_col=None)
            print(queryresult.to_string(index=False))
        except:
            print("Please input a valid number")
    return()

#Main interface
loop = 0
choice = 0
a = 1
while (loop != 1):
    printmenu()
    choice = input()

    #searching
    if (choice == '2'):
        os.system('clear')
        search()
    #adding
    elif (choice == '3'):
        os.system('clear')
        insert()
        a = 1
    #updating
    elif (choice == '4'):
        os.system('clear')
        update()
    #deleting
    elif (choice == '5'):
        os.system('clear')
        delete()
        a = 1
    #view
    elif (choice == '1'):
        os.system('clear')
        view()
    elif (choice == '6'):
      os.system('clear')
      select()
    elif (choice == '7'):
        os.system("clear")
        print("Godbye! Thank you for using Flight DBMS")
        break






con.close