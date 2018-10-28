import sqlite3 as bank


def create_table(path: str):
    try:
        conn = bank.connect(path)
        with conn:
            cur = conn.cursor()
            sql = "DROP TABLE IF EXISTS tbl_personal" 
            cur.execute(sql)
            sql = "create table tbl_personal (Personal_id varchar(25) not null primary key, name varchar(250) not null, family varchar(250) not null,bio text);"

    except:
        print("Error Connection")


def add_staff(db_path: str, staff_id: str, name: str, family: str, bio: str):
    # TODO etelate farrd azafe shavad
    pass


def update_staff(db_path: str, staff_id: str, name: str, family: str, bio: str):
    # TODO etelate farrd azafe shavad
    pass


def show_staff(db_path: str, staff_id: str):
    # TODO etelaate fard ra neshan midahad
    pass


def show_all_staff(db_path: str):
    # TODO etelaate koliye afrad ra neshan midahad
    pass


def remove_staff(db_path: str, staff_id: str):
    # TODO etelate farrd remove shavad
    pass
