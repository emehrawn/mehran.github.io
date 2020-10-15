class Human:
    def __init__(self,n,o):   #Constructor
        self.name = n
        self.occupation = o
    def do_work(self):        #Function
        if self.occupation =="tennis player":
            print(self.name, "Plays Tennis")
        elif self.occupation =="Actor":
            print(self.name, "Acts in movies")
    def speaks(self):          #Function
        print(self.name, "Says, How are you!")

tom = Human("Tom Cruise", "Actor")
tom.do_work()
tom.speaks()                            

'''
maria=Human("Maria Shavapora", "tennis Player")
maria.do_work()
maria.speaks
'''
