class Reserve(object):
    def __init__(self):
        pass

    def iLogin(self):
        pass

    def iSignup(self):
        pass

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