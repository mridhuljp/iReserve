class Reserve(object):
    def __init__(self):
        self.line="=" * 25

    def iLogin(self):
        pass

    def iSignup(self):
        print self.line
        self.Des_username=raw_input("Enter desired username : ")


    def HomeMenu(self):
        print "  !!!!!!!!!  Welcome to iReserve !!!!!!!!!!!!!"
        print " 1. Login : "
        print " 2. Signup : "
        print " ----------- "
        menuChoice=str(raw_input("Enter the input :"))
        if menuChoice == "1":
            self.iLogin()
        elif menuChoice == "2":
            self.iSignup()
        else:
            print "Option Invalid !!!!"
            self.HomeMenu()





####### Objects #########
kickoff=Reserve()
kickoff.HomeMenu()