from staff import database_utilities

#database_utilities.create_table(path="staff.db")
# id=input("id")
# name=input("name")
# family=input("family")
# bio=input("bio")
#
# database_utilities.add_staff(db_path="staff.db",staff_id=id,name=name,family=family,bio=bio)
#
# id=input("id")
# name=input("name")
# family=input("family")
# bio=input("bio")
#
# database_utilities.update_staff(db_path="staff.db",staff_id=id,name=name,family=family,bio=bio)

# staff_id=input("Enter Your ID For Show Info : ")
# database_utilities.show_staff(db_path="staff.db",staff_id=staff_id)
# database_utilities.show_all_staff(db_path="staff.db")
#
# staff_id=input("Enter Your ID For Show Info : ")
# database_utilities.remove_staff(db_path="staff.db",staff_id=staff_id)
#
# database_utilities.show_all_staff(db_path="staff.db")

# database_utilities.create_table(db_path="")

def chooseMenu(option:int):
    switcher = {
        1: showMenu2_1,
        2: showMenu2_2,
        3: showMenu2_3,
        4: showMenu1,
        11: "showMenu2_1",
        12: createDataBase,
        13: "July",
        14: Back,
        21: showMenu3_1,
        22: Back,
        31: "November",
        32: "December",
        33: Back,
        41: "December",
        42: Back,
        51: "December",
        52: "December",
        53: "December",
        54: "December",
        55: "December",
        56: showMenu2_2,
    }
    return switcher.get(option, "Invalid Number")

def chooseMenu2_1(option:int):
    switcher = {
        1: "list",
        2: "ADD",
        3: "Delete",
        4: "Back",
    }
    return switcher.get(option, "Invalid Number")


def chooseMenu2_2(option:int):
    switcher = {
        1: "SelectDB",
        2: "Back",
    }
    return switcher.get(option, "Invalid Number")

def chooseMenu2_3(option:int):
    switcher = {
        1: "Disable",
        2: "Enable",
        3: "Back",
    }
    return switcher.get(option, "Invalid Number")

def chooseMenu2_4(option:int):
    switcher = {
        1: "List",

    }
    return switcher.get(option, "Invalid Number")

def Back():
    showMenu()

def createDataBase():
    dbName=input("Enter Your DataBase Name : ")
    database_utilities.create_table(db_path=dbName)

def addStaff():
    db_path=print("Your DataBase Name")
    id=input("id: ")
    name=input("name: ")
    family=input("family: ")
    bio=input("bio: ")
    database_utilities.add_staff(db_path=db_path,staff_id=id,name=name,family=family,bio=bio)

def updateStaff():
    db_path=input("Your DataBase Name: ")
    id=input("id: ")
    name=input("name: ")
    family=input("family: ")
    bio=input("bio: ")
    database_utilities.update_staff(db_path=db_path,staff_id=id,name=name,family=family,bio=bio)

def show_all_staff():
    db_path = input("Your DataBase Name: ")
    database_utilities.show_all_staff(db_path)

#########################################################
def showMenu():
    print(20*"#"+"_Please Seletct One Option_"+20*"#")
    print("1. Data Base")
    print("2. Table")
    print("3. Log")
    print("4. Exit")

def showMenu1():
    print("\n")
    print(20*"#"+"_GOOD BAY_"+20*"#")
    exit()

def showMenu2_1():
    print(20*"#"+"_Please Seletct One Option_"+20*"#")
    print("11. List")
    print("12. Add")
    print("13. Delete")
    print("14. Back")

def showMenu2_2():
    print(20*"#"+"_Please Seletct One Option_"+20*"#")
    print("21. Select Table")
    print("21. Delete Table")
    print("22. Back")

def showMenu3_1():
    print(20*"#"+"_Please Seletct One Option_"+20*"#")
    print("51. Show All")
    print("52. Update")
    print("53. Add")
    print("54. Delete")
    print("55. Enable/Disable")
    print("56. Back")

def showMenu2_3():
    print(20*"#"+"_Please Seletct One Option_"+20*"#")
    print("31. Disable")
    print("32. Enable")
    print("33. Back")

def showMenu2_4():
    print(20*"#"+"_Please Seletct One Option_"+20*"#")
    print("41. List")
    print("42. Back")



showMenu()
while(1):

    num = int(input("Enter Your Numbr Of Options : "))
#    if (num == 2):
    func = chooseMenu(num)
    func()

#num+=s
#    continue

#while(1):

#    num = int(input("Enter Your Numbr Of Options : "))
#    if (num == 2):
#    func = chooseMenu(s/num)
#    func()
#    continue
#    if (num ==1 ):
#        chooseMenu1()


