class Reserve(object):
    UsersTable={}
    def __init__(self):
        self.line="=" * 25


    def iLogin(self):
        pass

    def UserExists(self):
        if self.Des_username in self.UsersTable.keys():
            return 0
        else:
            return 1

    def ValidatePass(self):
        if len(self.Des_password) <=3:
            return 1
        else:
            return 0

    def PrintUsers(self):
        print self.UsersTable

    def UserAdd(self):
        self.UsersTable[self.Des_username]=self.Des_password
        print "User Added Successfully !!!"
        print self.line
        self.PrintUsers()
        print self.line
        self.HomeMenu()

    def iSignup(self):
        print self.line
        self.Des_username=raw_input("Enter desired username : ")
        self.iUserReturn=self.UserExists()
        if self.iUserReturn == 0:
            print "User Exists !!!! "
            self.iSignup()
        self.Des_password=raw_input("Enter your password [Minimum 4 chars] : ")
        self.ValidPassword=self.ValidatePass()
        if self.ValidPassword ==1:
            print "Sorry !!! Password Didn't match the requirements !!"
            self.iSignup()
        else:
            self.UserAdd()

    def HomeMenu(self):
        print "  !!!!!!!!!  Welcome to iReserve !!!!!!!!!!!!!"
        print " 1. Login : "
        print " 2. Signup : "
        print " 3. Exit! : "
        print " ----------- "
        menuChoice=str(raw_input("Enter the input :"))
        if menuChoice == "1":
            self.iLogin()
        elif menuChoice == "2":
            self.iSignup()
        elif menuChoice =="3":
            exit()
        else:
            print "Option Invalid !!!!"
            self.HomeMenu()





####### Objects #########
kickoff=Reserve()
kickoff.HomeMenu()