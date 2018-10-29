from staff import database_utilities

#database_utilities.create_table(path="staff.db")
id=input("id")
name=input("name")
family=input("family")
bio=input("bio")


database_utilities.add_staff(db_path="staff.db",staff_id=id,name=name,family=family,bio=bio)
