"""
This is a demo application which shows a role based authentication system.
=====================================================================

Requirements
------------
Need Python3 in local System.
This application uses sqlite database, which doesn't need any installation it works from command line. 
Can install sqlite from pip command.
command:
    pip install pysqlite3
	
How to run: 
-----------
	1.Install a python library using pip command.
	2.open cmd and type "pip install pysqlite3"
	3.Once done. Keep 4 files in the folder.i.e. 
		-__init__.py
		-main.py
		-sqlite_database.py
		-application_user_info.db
	4. open cmd in the folder path.
	5. type "python __init__.py
	6. Follow the on screen instruction.


Assumptions:
------------
  - Here "admin" user is already created with username as 'admin' and password as 'admin'.
  - "admin" user has the role of "Administrator"
  - There are 3 roles defined in the application.
        - Accountant
        - Store Manager
        - Sales Manager
  - There are 3 Resources defined in the application.
        - Product_info
        - Sales_info
        - Payment_info    
  - There are 2 Action Type defined in the application.
        - Read
        - Read Write
  - admin user which is "Administrator" role has all rights and permission to ASSIGN ANY ROLE,ANY RESOURCE,
    ANY ACTION TYPE to a user in the application.
  - "admin" user is created at the beginning of the application with "Administrator" Role and access to all 
    resource and Read Write and Delete permission.
  

Main Features
-------------
Here are just a few of the things that application does well:

  - "admin" user has various functionality like
        - It can create a User.
        - It edit a User for Role, Resource and Action Type. 
          i.e. "admin" user can assign new or remove old role for a user
          vice versa for Resource and Action Type.
        - It can delete a user.
  - Normal User has various functionality like
        - It can view the roles assign to itself.
        - it can check the access to the other resources.
  - In the application you can any time login as another user with Username and password.
  - This application uses the oops concept with classes and methods.
  - Application is triggered through the init script.
  """
