import sqlite3 as bank


def create_table(path: str):
    try:
        conn = bank.connect(path)
        print("connect To DB successfully!")
        with conn:
            cur = conn.cursor()
            print("Join curser Into DB!")
            sql = "DROP TABLE IF EXISTS tbl_personal" 
            cur.execute(sql)
            print("Drop tbl_personal successfully!")
            sql = "CREATE TABLE tbl_personal ( personal_code int PRIMARY KEY NOT NULL,name varchar(250) NOT NULL,family varchar(250) NOT NULL,bio varchar(250) NOT NULL);"
            cur.execute(sql)
            sql= "CREATE UNIQUE INDEX tbl_personal_personal_code_uindex ON tbl_personal (personal_code);"
            cur.execute(sql)
            print("Create tbl_personal successfully!")
    except:
        print("Error Connection")


def add_staff(db_path: str, staff_id: str, name: str, family: str, bio: str):
    # TODO etelate farrd azafe shavad
    try:
        conn = bank.connect(db_path)
        print("connect To DB successfully!")
        with conn:
            cur = conn.cursor()
            print("Add_Staff_Join curser Into DB!")
            sql = "INSERT INTO tbl_personal ( personal_code,name ,family ,bio) VALUES (?,?,?,?)"
            staff = (staff_id,name , family,bio)
            cur.execute(sql,staff)
            print("Add_Staff_Created!")

    except:
        print("Error Connection")



def update_staff(db_path: str, staff_id: str, name: str, family: str, bio: str):
    # TODO etelate farrd azafe shavad
    try:
        conn = bank.connect(db_path)
        print("Update_connect To DB successfully!")
        with conn:
            cur = conn.cursor()
            print("Update_Staff_Join curser Into DB!")
            sql = "Update tbl_personal ( personal_code,name ,family ,bio) VALUES (?,?,?,?)"
            staff = (staff_id,name , family,bio)
            cur.execute(sql,staff)
            print("Add_Staff_Created!")
            print(cur.lastrowid)
    except:
        print("Error Connection")


def show_staff(db_path: str, staff_id: str):
    # TODO etelaate fard ra neshan midahad
    pass


def show_all_staff(db_path: str):
    # TODO etelaate koliye afrad ra neshan midahad
    pass


def remove_staff(db_path: str, staff_id: str):
    # TODO etelate farrd remove shavad
    pass
