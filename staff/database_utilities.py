import sqlite3 as bank
#from sqlite3 import Error
import logging

logging.basicConfig(filename="DB_Utilities_Logs.log",level=logging.DEBUG,format="format='%(asctime)-15s %(name)-5s %(levelname)-8s  %(message)s'")
 
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s ")

l_conectDB=logging.getLogger("Module_Connect_To_DataBase")

console_handler = logging.StreamHandler()
console_handler.setFormatter(FORMATTER)
l_conectDB.addHandler(console_handler)



def create_table(db_path: str):
    try:
        conn = bank.connect(db_path)

        l_conectDB.info("Successful Connect To  DataBase Server For Create Table Into {} DB".format(db_path))

        with conn:
            cur = conn.cursor()

            l_conectDB.info("Join curser Into  DataBase Server!")

            sql = "DROP TABLE IF EXISTS tbl_personal"
            cur.execute(sql)
            l_conectDB.info("Drop tbl_personal successfully!")

            sql = "CREATE TABLE tbl_personal ( personal_code int PRIMARY KEY NOT NULL,name varchar(250) NOT NULL,family varchar(250) NOT NULL,bio varchar(250) NOT NULL, show int DEFAULT 1);"

            cur.execute(sql)
            sql= "CREATE UNIQUE INDEX tbl_personal_personal_code_uindex ON tbl_personal (personal_code);"
            cur.execute(sql)

            l_conectDB.info("Create tbl_personal successfully!")
    except:
        l_conectDB.critical("Error connect To DataBase Server for {} DB".format(db_path))


def add_staff(db_path: str, staff_id: str, name: str, family: str, bio: str):

    try:
        conn = bank.connect(db_path)

        l_conectDB.info("Successful Connect To  DataBase Server For Add Staff with ID {} Into ".format(staff_id,db_path))

        with conn:
            cur = conn.cursor()

            l_conectDB.info("Join curser Into  DataBase Server! ")

            sql = "INSERT INTO tbl_personal ( personal_code,name ,family ,bio) VALUES (?,?,?,?)"
            staff = (staff_id,name , family,bio)
            cur.execute(sql,staff)

            l_conectDB.info("Added Staff to Table tbl_personal From {} DB! ".format(db_path))


    except:
        l_conectDB.critical("Error connect To DataBaseServer For {} DB".format(db_path))




def update_staff(db_path: str, staff_id: str, name: str, family: str, bio: str):

    try:
        conn = bank.connect(db_path)
        l_conectDB.info(
            "Successful Connect To  DataBase Server For Update Staff with ID {} Into ".format(staff_id, db_path))

        with conn:
            cur = conn.cursor()

            l_conectDB.info("Join curser Into  DataBase Server! ")

            sql = "Update tbl_personal SET name=? ,family=? ,bio=? WHERE personal_code=?"
            staff = (name , family,bio,staff_id)
            cur.execute(sql,staff)

            l_conectDB.info("Updated Staff in Table tbl_personal From {} DB! ".format(db_path))

    except:
        l_conectDB.critical("Error connect To DataBaseServer For {} DB".format(db_path))

def show_staff(db_path: str, staff_id: str):


    try:
        conn = bank.connect(db_path)
        l_conectDB.info(
            "Successful Connect To  DataBase Server For Staff Staff with ID {} Into ".format(staff_id, db_path))

        with conn:
            cur = conn.cursor()
            l_conectDB.info("Join curser Into  DataBase Server! ")
            sql = "Select * FROM tbl_personal where personal_code=?"
            id=(staff_id,)
            cur.execute(sql,id)

            rows = cur.fetchone()
            print(rows)
            l_conectDB.info("Show Staff in Table tbl_personal From {} DB! ".format(db_path))

    except:
        l_conectDB.critical("Error connect To DataBaseServer For {} DB".format(db_path))



def show_all_staff(db_path: str):

    try:
        conn = bank.connect(db_path)
        l_conectDB.info("Successful Connect To  DataBase Server For Show All Staffs")
        with conn:
            cur = conn.cursor()
            l_conectDB.info("Join curser Into  DataBase Server! ")
            sql = "Select * FROM tbl_personal WHERE show IS NOT 0"
            cur.execute(sql)
            results = cur.fetchall()
            for row in results:
                print(row)
                l_conectDB.info("ShowALL_Staff")

    except:
        l_conectDB.critical("Error connect To DataBaseServer For DB")


def remove_staff(db_path: str, staff_id: str):

    try:
        conn = bank.connect(db_path)
        l_conectDB.info(
            "Successful Connect To  DataBase Server For Remove Staff with ID {} Into ".format(staff_id, db_path))

        with conn:
            cur = conn.cursor()
            l_conectDB.info("Join curser Into  DataBase Server! ")
            # sql = "DELETE FROM tbl_personal where personal_code=?"
            sql = "Update tbl_personal SET show=0 WHERE personal_code=?"
            id=(staff_id,)
            cur.execute(sql,id)
            l_conectDB.info("Removed Staff From Table tbl_personal From {} DB! ".format(db_path))

    except:
            l_conectDB.critical("Error connect To DataBaseServer For {} DB".format(db_path))


