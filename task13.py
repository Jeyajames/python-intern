#coffee machine
class CoffeeMachine:
    running = False
    def _init_(self ,water ,milk ,cup,coffee,money):
        self.water =water
        self.milk =milk
        self.coffee=coffee
        self.cup=cup
        self.money =money

        if not CoffeeMachine.running:
            self.start()
    def start(self):
        self.running= true
        self.action =input("the action are (buy,fill,take,report,off):\n")
        print()

        if self.action == "buy":
            self.buy()
        elif self.action == "fill":
            self.fill()
        elif self.action == "take":
            self.take()
        elif self.action == "exit":
            self.exit()
        elif self.action == "report":
            self.status()
    def return_to_menu(self):#return to the menu after action
        print()
        self.start()
    def available_check(self):
        self.not_available =""
        if self.water - self.reduced[0 ] <0:
            self.not_available ="water"
        elif self.milk - self.reduced[1 ] <0:
            self.not_availabe ="milk"
        elif self.coffee - self.reduced[2]<0:
            self.not_available ="coffee"
        elif self.cup- self.reduced[3]<0:
            self.not_available="disposable cup"
        if self.not_available !='':
            print(f"sorry not enough{self.not_available}")
        else:
            print("i have enough resource")
    def deduct_supplies(self):
        self.water = self.reduced[0]
        self.milk = self.reduced[1]
        self.coffee= self.reduced[2]
        self.cup=self.reduced[3]
        self.money = self.reduced[4]
    def buy(self):
        self.choice=input("what would you like?1:espresso,2:latte,3:cappuccino,back-to main menu,off-turn off the machine:\n")
        if self.choice == '1':
            self.reduced=[200,0,15,1,4]
            if self.available_check():
                self.deduct_supplies()
        elif self.choice=='2':
            self.reduced=[100,50,76,1,2.5]
            if self.available_check():
                self.deduct_supplies()
        elif self.choice=="3":
            self.reduced=[150,100,20,1,5]
            if self.availabe_check():
                self.deduct_supplies()
        elif self.choice=="back":
            self.return_to_menu()
        self.return_to_menu()
        elif self.choice=="off"
             self.return_to_off
    def fill(self):
        self.water = int(input("how many ml water do you want to add:\n"))
        self.milk = int(input("how many ml of milk do you want to add:\n"))
        self.coffee_bean=int(input("how many gram of coffee do you want to add:\n"))
        self.return_to_menu()
    def take(self):
        print(f"enter the money ${self.money}")
        if self.money = self.money:
           print("transaction successfull")
        elif self.money < self.money:
            print("sorry that is not enough money.money refunded")
        elif self.money > self.money:
            print("collect remaing amount")
        self.return_to_menu()
    def report(self):
        print("Report- current resource value:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee")
        print(f"${self.money} of money")
        self.return_to_menu()
CoffeeMachine(600,800,120,9,550)

