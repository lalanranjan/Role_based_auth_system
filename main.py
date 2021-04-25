#=====================================
# Author  : Lalan Ranjan
# @Email  : lalanranjan@hotmail.com
# @Date   : 25-04-2021
#=====================================

from sqlite_database import user_db_table
import sqlite3 as sl
# import stdiomask

class demo_app:
    def __init__(self):
        pass

    ## Database connection ##
    con = sl.connect('application_user_info.db')

    ## Create a new user ##
    def create_user(self,data):
        from sqlite_database import user_db_table
        db=user_db_table()
        try:
            db.insert_user(self.con,data)
            print("\nUser created successfully !!")
        except:
            print("\nNot able to create user! May be User already present or wrong input !!")

    ## Login to application ##
    def login_db(self):
        print("\nWelcome to Demo of Role based authentication system!!")
        username=input("Please enter the username: ")
        password=input("Please enter the password: ")
        # password=stdiomask.getpass("Enter Password: ")

        ############# Logic to check database for login credential ################

        user_check=user_db_table()
        user_check_list=user_check.check_login_user_info(self.con,username,password)
        try:
            if (username and password) in user_check_list[0]:
                print('\nHi! You are logged in as ' + username)
        except:
            print("\nUsername or Password is wrong. Try Again !")
            exit()

        while (True):
            if ('Administrator') in user_check_list[0]:

                run = input("\nSelect the option below to proceed:\n Press 1 for create user. "
                            "\n Press 2 for login as another user. \n Press 3 for edit user.\n Press 4 for delete user. \n Press 5 for Exit.\nChoice: ")

                if run not in ['1', '2', '3', '4', '5']:
                    print('Wrong Choice !! Try again.')
                    continue

                elif int(run)==5:
                    print('Thank You !!')
                    exit()
                else:
                    self.check_option(run, user_check_list[0][5], user_check_list[0][1], user_check_list[0][2])

            else:

                run = input("\nSelect the option below to proceed:\n Press 1 for login as another user. "
                            "\n Press 2 for view roles. \n Press 3 for access resource. \n Press 4 for Exit. \nChoice: ")

                if run not in ['1', '2', '3', '4']:
                    print('Wrong Choice !! Try login again.')
                    continue

                elif int(run) == 4:
                    print('Thank You !!')
                    exit()
                else:
                    self.check_option(run, user_check_list[0][5], user_check_list[0][1], user_check_list[0][2])


    ## Action function with choice ##
    def actionfun(self,action):
        if action == 1:
            actio = 'Read'
        if action == 2:
            actio = 'Read_Write'
        # print(action)
        if action != 1 and action != 2:
            print("Wrong input in 'Action type'. Please start again! ")
            return
        return actio

    ## Resource function with choice ##
    def resourcefun(self,resour):
        resour = int(resour)
        if resour == 1:
            resourr = 'Product'
        if resour == 2:
            resourr = 'Sales'
        if resour == 3:
            resourr = 'Payment'
        if resour != 1 and resour != 2 and resour != 3:
            print("Wrong input in 'Resources'. Please start again! ")
            return
        return resourr+','

    ## Role function with choice ##
    def rolefun(self,rol):
        rol = int(rol)
        if rol == 1:
            rooll = 'Accountant'
        if rol == 2:
            rooll = 'Store Manager'
        if rol == 3:
            rooll = 'Sales Manager'
        if rol != 1 and rol != 2 and rol != 3:
            print("Wrong input in 'Role'. Please start again! ")
            return
        return rooll+','

    ## function to check user choice ##
    def check_option(self,run,role,username,password):
        run = int(run)

        if run == 1 and role=='Administrator':
            print('\nFor creating User enter the following: ')
            user=input("Enter Username for the user: ").strip()
            passw=input("Enter Password for the user: ").strip()

            if user=='' or passw =='':
                print("\nUsername or Password can't be empty. ")
                return

            rol = input(
                "\nSelect Role for the user: \nYou can select multiple Role like 1,2 or 1,3 or ... \n Press 1 for 'Accountant'. \n Press 2 for 'Store Manager'. \n Press 3 for 'Sales Manager'.\nChoice: ")
            try:
                rol=rol.split(',')
                rool=''
                for item in rol:
                    rool=rool+self.rolefun(item)
            except:
                print('Wrong Format of option selected. Try again !!')
                return

            resour = input(
                "\nSelect Resources to assign to user:\nYou can select multiple Resource like 1,2 or 1,3 or ...\n Press 1 for 'Product'. \n Press 2 for 'Sales'. \n Press 3 for 'Payment'.\nchoice: ")
            try:
                resour=resour.split(',')
                resourr=''
                for item in resour:
                    resourr=resourr+self.resourcefun(item)
            except:
                print('Wrong Format of option selected.Try again !!')
                return


            action=input("\nSelect ONE Action type for user to Access Resources:\n Press 1 for 'Read'. \n Press 2 for 'Read Write'.\nChoice: ")
            try:
                action=int(action)
                acti = self.actionfun(action)
            except:
                print("Wrong input in 'Action type'. Try again !! ")
                return



            data=[(user,passw,acti,resourr,rool)]
            self.create_user(data)


        elif (run == 2 and role == 'Administrator') or (run == 1 and (role != 'Administrator')):
            self.login_db()

        elif (run == 3 and role == 'Administrator'):
            user_check = user_db_table()
            list_user = user_check.list_user_name(self.con)
            print("List of users:" )
            print(list_user)
            edit_user=input("Enter the user you want to edit :")
            user_info = user_check.check_user_info(self.con,edit_user)
            try:
                act = user_info[0][3]
                resourr = user_info[0][4]
                rool = user_info[0][5]
                while(True):
                    print('\nUser current info are: ')
                    print(' Press 1 for change in Role: ' + rool)
                    print(' Press 2 for change in Resource: ' + resourr)
                    print(' Press 3 for change in Action Type :'+act)
                    print(' Press 4 to save data.')
                    print(' Please select the option to edit. It will clear the Old info. and will freshly add the new info.')
                    val= input('Enter Choice: ')
                    val=int(val)

                    if val == 1:
                        rol = input(
                            "\nOld asigned Role is clear for the user.\nSelect the new Role for the user.\nYou can select multiple Role like 1,2 or 1,3 or ... \n Press 1 for 'Accountant'. \n Press 2 for 'Store Manager'. \n Press 3 for 'Sales Manager'.\nChoice: ")
                        try:
                            rol = rol.split(',')
                            rool = ''
                            for item in rol:
                                rool = rool + self.rolefun(item)
                        except:
                            print('Wrong Format of option selected. Try again !!')
                            continue
                        continue
                    if val==2:
                        resour = input(
                            "\nOld asigned Resource is clear for the user.\nSelect the new Resource for the user.\nYou can select multiple Resource like 1,2 or 1,3 or ...\n Press 1 for 'Product'. \n Press 2 for 'Sales'. \n Press 3 for 'Payment'.\nchoice: ")
                        try:
                            resour = resour.split(',')
                            resourr = ''
                            for item in resour:
                                resourr = resourr + self.resourcefun(item)
                        except:
                            print('Wrong Format of option selected.Try again !!')
                            continue
                        continue
                    if val==3:
                        acttt = input(
                            "\nOld asigned Action type is clear for the user.\nSelect one option to asign new Action type for user to access resources.\n Press 1 for 'Read'. \n Press 2 for 'Read Write'.\nChoice: ")
                        try:
                            actionnn = int(acttt)
                            act = self.actionfun(actionnn)
                        except:
                            print("Wrong input in 'Action type'. Try again !! ")
                            continue
                        continue

                    if val == 4:
                        user_check.update_user_info(self.con, edit_user,act,resourr,rool)
                        print('\nUser Details saved to Database !!')
                        break
                    else:
                        print('Wrong Input!! Try Again')
                        continue

            except:
                print("\nUsername selected is Incorrect or Wrong Input. Try again !!")



        elif (run == 4 and role == 'Administrator'):
            user_check = user_db_table()
            list_user = user_check.list_user_name(self.con)
            print("List of users:")
            print(list_user)
            delete_user = input("Enter the user you want to delete :")
            if delete_user not in list_user:
                print('\nUsername incorrect. Try again!!')
            else:
                user_check.delete_user(self.con,delete_user)
                print('Successfully removed user !!')

        elif (run == 2 and role != 'Administrator'):
            user_check = user_db_table()
            user_rolee = user_check.check_user_info(self.con,username)
            print('Current Role is:'+user_rolee[0][5])

        elif (run == 3 and role != 'Administrator'):
            user_check = user_db_table()
            user_rolle = user_check.check_user_info(self.con,username)
            print("List Of resources want to access: ")
            re=input("You can select multiple Resource like 1,2 or 1,3 or ...\n Press 1 for 'Product'. \n Press 2 for 'Sales'. \n Press 3 for 'Payment'.\nchoice: ")
            try:
                resoour = re.split(',')
                resourrr = ''
                for item in resoour:
                    resourrr = resourrr + self.resourcefun(item)
                print('Wants to Access Resource: '+resourrr)
                rresoour = resourrr.split(',')
                rresoour.pop(-1)
                ur=user_rolle[0][4].split(',')
                ur.pop(-1)
                res_acc=list(set(rresoour) - set(ur))
                if len(res_acc)==0:
                    print('You have access to the selected resources: ',rresoour,'with',user_rolle[0][3],'permission.')
                else:
                    print('Access Denied to Selected Resource: ',res_acc)
                    print('You have access to resource:',ur,'with',user_rolle[0][3],'permission.')
            except:
                print('Wrong Format of option selected.Try again !!')

        else:
            print("Wrong Choice !! Try again.")
            exit()

    ## Create admin User ##
    def create_admin(self):
        data = [('admin', 'admin', 'RWD', 'Product, Sales, Payment', 'Administrator')]
        self.create_user(data)






