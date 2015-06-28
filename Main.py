class Reserve(object):
    UsersTable = {}
    srv1 = []
    srv1.extend(range(1, 21))
    UserSession = False
    iBooked = 0

    def __init__(self):
        self.line = "=" * 25

    def UserExists(self):
        if self.Des_username in self.UsersTable.keys():
            return 0
        else:
            return 1

    def iLogin(self):
        print self.line
        self.Des_username = raw_input("Username : ")
        self.ifUserExists = self.UserExists()
        if self.ifUserExists > 0:
            print "Sorry !! Invalid User"
            print self.line
            self.iLogin()
        else:
            self.Des_password = raw_input("Password : ")
            if self.UsersTable[self.Des_username] == self.Des_password:
                print " User %s Successfully Logged in !!" % (self.Des_username)
                self.UserSession = True
                print self.line
                self.HomeMenu()
            else:
                print "Sorry !!! Invalid credentials"
                print self.line
                self.iLogin()

    def ValidatePass(self):
        if len(self.Des_password) <= 3:
            return 1
        else:
            return 0

    def PrintUsers(self):
        print self.UsersTable

    def UserAdd(self):
        self.UsersTable[self.Des_username] = self.Des_password
        print "User Added Successfully !!!"
        print self.line
        # self.PrintUsers()
        print self.line
        self.HomeMenu()

    def iSignup(self):
        print self.line
        self.Des_username = raw_input("Enter desired username : ")
        self.iUserReturn = self.UserExists()
        if self.iUserReturn == 0:
            print "User Exists !!!! "
            self.iSignup()
        self.Des_password = raw_input("Enter your password [Minimum 4 chars] : ")
        self.ValidPassword = self.ValidatePass()
        if self.ValidPassword == 1:
            print "Sorry !!! Password Didn't match the requirements !!"
            self.iSignup()
        else:
            self.UserAdd()

    def HomeMenu(self):
        print "  !!!!!!!!!  Welcome to iReserve !!!!!!!!!!!!!"
        print " 1. Login : "
        print " 2. Signup : "
        print " 3. Reserve : "
        print " 4. Exit! : "
        print " ----------- "
        menuChoice = str(raw_input("Enter the input :"))
        if menuChoice == "1":
            self.iLogin()
        elif menuChoice == "2":
            self.iSignup()
        elif menuChoice == "4":
            exit()
        elif menuChoice == "3":
            self.iReserve()
        else:
            print "Option Invalid !!!!"
            self.HomeMenu()

    def iReserve(self):
        def iBook(self):
            print "Book !!!"
            print self.line
            while (self.UserSession):
                print self.srv1
                print self.line
                print "Legend : 'B' - Booked Seat . 'R' - Reserved Seat"
                print self.line
                self.userseat = raw_input("Enter your choice :")
                self.iBooked = self.userseat
                if int(self.userseat) > 20 or self.srv1[int(self.userseat)] == "B":
                    print "Sorry !! Seat Already booked !!!"
                    print self.line
                    self.iReserve()
                else:
                    self.srv1[int(self.userseat) - 1] = self.userseat.replace(self.userseat, "B")
                print "Seat Booked Successfully !!!"
                print self.srv1
                self.HomeMenu()
            else:
                print "Sorry !!! Login first"
                self.HomeMenu()

        def iCancel(self):
            print "Cancel"
            print self.line
            while (self.UserSession):
                print self.srv1
                print self.line
                if self.iBooked == 0:
                    print "Sorry !!! You don't have reservations "
                    self.iReserve()
                print "Legend : 'B' - Booked Seat . 'R' - Reserved Seat"
                print "You've booked the seat %s" % (self.iBooked)
                print self.line
                self.cancel = raw_input("Enter the Cancellation seat :")
                if int(self.cancel) > 20 or self.srv1[int(self.cancel) - 1] != "B":
                    print "Sorry !! Seat cannot be cancelled !!!"
                    print self.line
                    self.iReserve()
                else:
                    self.srv1[int(self.cancel) - 1] = int(self.cancel)
                print "Seat Cancelled Successfully !!!"
                print self.srv1
                self.HomeMenu()
            else:
                print "Sorry !!! Login first"
                self.HomeMenu()

        def iList(self):
            print "List"

        print "1. Book : "
        print "2. Cancel: "
        print "3. List : "
        self.iResMenu = str(raw_input("Enter option : "))
        if self.iResMenu == "1":
            iBook(self)
        elif self.iResMenu == "2":
            iCancel(self)
        elif self.iResMenu == "3":
            iList(self)
        else:
            print "Invalid Option Selected "
            self.iReserve()

####### Objects #########
kickoff = Reserve()
kickoff.HomeMenu()
