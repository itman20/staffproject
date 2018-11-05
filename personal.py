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
        1: createDataBase,
        2: addStaff,
        3: updateStaff,
        4: "April",
        5: show_all_staff,
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(option, "Invalid Number")



def createDataBase():
    dbName=input("Enter Your DataBase Name : ")
    database_utilities.create_table(db_path=dbName)

def addStaff():
    db_path=input("Your DataBase Name: ")
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
print(20*"#"+"_Please Seletct One Option_"+20*"#")
print("1. Create DataBase")
print("2. Add Staff")
print("3. Update Staff")
print("4. Show Staff")
print("5. Show Staffs")
print("6. Remove Staff")

while(1):
    num = int(input("Enter Your Numbr Of Options : "))
    func=chooseMenu(num)
    func()



