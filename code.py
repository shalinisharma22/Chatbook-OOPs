class chatbook:
    def __init__(self):
        self.username= ''
        self.password=''
        self.loggedin= False
        self.menu()


    
    def menu(self):
        user_input=input("""welcome to chatbook. How would you like to proceed?
                         1. Press 1 to signup
                         2. Press 2 to signin
                         3. Press 3 to write a post
                         4. Press 4 to message a friend
                         5. Press any key to exit""")

        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.post()
        elif user_input=="4":
            self.message()
        else:
            exit()
            
    
    def signup(self):
        self.username=input("Enter your email id here--> ")
        self.password=input("Enter your password here--> ")
        print("You have successfully signed up")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("Please signup first by pressing 1 to the main menu")
        else:
            uname=input("Enter your email id here--> ")
            pwd=input("Enter your password here--> ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully!!")
                self.loggedin=True
            else:
                print("please input correct credentials")
        
        self.menu()
    
    def post(self):
        if self.loggedin==True:
            txt=input("Enter your message here-->")
            print("Following content has been posted--> {txt}")
        else:
            print("In order to post something please login first")

        self.menu()

    def message(self):
        if self.loggedin==True:
            txt=input("Enter your message here-->")
            frnd=input("Whom to send the msg?->")
            print("Your message has been sent to {frnd}") 
        else:
            print("In order to message something please login first")

        self.menu()



    
    



obj=chatbook()



        