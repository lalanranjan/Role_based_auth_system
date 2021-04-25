#=====================================
# Author  : Lalan Ranjan
# @Email  : lalanranjan@hotmail.com
# @Date   : 25-04-2021
#=====================================

class user_db_table:
    def __init__(self):
        pass


    ## User table creation ##
    def table_create(self,con):
        with con:
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE USER (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    User TEXT NOT NULL UNIQUE,                    
                    Password TEXT NOT NULL,
                    Action_type TEXT NOT NULL,
                    Resource TEXT NOT NULL,
                    Role TEXT NOT NULL );""")
            con.commit()

    ## Insert  user to table ##
    def insert_user(self, con, data):
        sql = 'INSERT INTO USER (User, Password, Action_type, Resource, Role ) values(?, ?, ?, ?, ?)'
        with con:
            cur = con.cursor()
            cur.executemany(sql, data)
            con.commit()

    ## table Query ##
    def check_table_info(self,con):
        with con:
            cur = con.cursor()
            data = cur.execute("SELECT * FROM USER")
            for row in data:
                print(row)


    ## Check login user ##
    def check_login_user_info(self,con,username,password):
        sql_query = "SELECT * FROM USER WHERE User ='%s' AND Password ='%s'" % (username, password)
        cur = con.cursor()
        mycursor = cur.execute(sql_query)
        return mycursor.fetchall()

    ## List all user ##
    def list_user_name(self, con):
        sql_query = "SELECT User FROM USER"
        cur = con.cursor()
        mycursor = cur.execute(sql_query)
        val=mycursor.fetchall()
        val_list=[x[0] for x in val]
        return val_list

    ## Check user info ##
    def check_user_info(self, con, username):
        sql_query = "SELECT * FROM USER WHERE User ='%s'" % (username)
        cur = con.cursor()
        mycursor = cur.execute(sql_query)
        return mycursor.fetchall()

    ## Update user info ##
    def update_user_info(self, con,username,action,Resource,Role):
        sql_query = "UPDATE USER set Action_type = '"+action+"',Resource = '"+Resource+"',Role = '"+Role+"' where User = '"+username+"'"
        cur = con.cursor()
        cur.execute(sql_query)
        con.commit()

    ## Delete user from database ##
    def delete_user(self, con,username):
        sql_query = "DELETE FROM USER where User = '"+username+"'"
        cur = con.cursor()
        cur.execute(sql_query)
        con.commit()
