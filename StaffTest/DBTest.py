from staff import database_utilities

def testdbfile():
    assert(database_utilities.create_table("staff.db"))