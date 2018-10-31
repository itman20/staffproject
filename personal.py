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
staff_id=input("Enter Your ID For Show Info : ")
database_utilities.show_staff(db_path="staff.db",staff_id=staff_id)
database_utilities.show_all_staff(db_path="staff.db")

staff_id=input("Enter Your ID For Show Info : ")
database_utilities.remove_staff(db_path="staff.db",staff_id=staff_id)

database_utilities.show_all_staff(db_path="staff.db")