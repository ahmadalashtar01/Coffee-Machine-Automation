class CoffeeMachine:
    water_state = 0
    milk_state = 0
    beans_state = 0
    cups_state = 0
    money_state = 0
    power = True
    # Espresso Ingredient
    espresso_water = 250
    espresso_beans = 16
    espresso_price = 4
    # Latte Ingredient
    latte_water = 350
    latte_milk = 75
    latte_beans = 20
    latte_price = 7
    # Cappuccino Ingredient
    cappuccino_water = 200
    cappuccino_milk = 100
    cappuccino_beans = 12
    cappuccino_price = 6

    def __init__(self, water_state, milk_state, beans_state, cups_state, money_state, power):
        self.water_state = water_state
        self.milk_state = milk_state
        self.beans_state = beans_state
        self.cups_state = cups_state
        self.money_state = money_state
        self.power = power

    def check_espresso(self):
        if self.water_state < self.espresso_water:
            return False
        elif self.beans_state < self.espresso_beans:
            return False
        elif self.cups_state == 0:
            return False
        else:
            return True

    def check_latte(self):
        if self.water_state < self.latte_water:
            return False
        elif self.beans_state < self.latte_beans:
            return False
        elif self.milk_state < self.latte_milk:
            return False
        elif self.cups_state == 0:
            return False
        else:
            return True

    def check_cappuccino(self):
        if self.water_state < self.cappuccino_water:
            return False
        elif self.beans_state < self.cappuccino_beans:
            return False
        elif self.milk_state < self.cappuccino_milk:
            return False
        elif self.cups_state == 0:
            return False
        else:
            return True

    def main(self):
        task = input("Write action (buy, fill, take, remaining, exit):")
        if task == "buy":
            inquiry = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            if inquiry == "back":
                self.main()
            else:
                inquiry = int(inquiry)
                self.buy(inquiry)

        elif task == "fill":
            water_addition = int(input("Write how many ml of water do you want to add:"))
            milk_addition = int(input("Write how many ml of milk do you want to add:"))
            beans_addition = int(input("Write how many grams of coffee beans do you want to add:"))
            cups_addition = int(input("Write how many disposable cups of coffee do you want to add:"))
            self.fill(water_addition, milk_addition, beans_addition, cups_addition)

        elif task == "take":
            self.take()
        elif task == "remaining":
            self.declare_state()
        elif task == "exit":
            self.power = False

    def declare_state(self):
        print("The coffee machine has:")
        print(str(self.water_state) + " of water")
        print(str(self.milk_state) + " of milk")
        print(str(self.beans_state) + " of coffee beans")
        print(str(self.cups_state) + " of disposable cups")
        print("$" + str(self.money_state) + " of money")

    def buy(self, inquiry):

        if inquiry == 1:
            if self.check_espresso():
                print("I have enough resources, making you a coffee!")
                self.water_state = self.water_state - self.espresso_water
                self.beans_state = self.beans_state - self.espresso_beans
                self.cups_state -= 1
                self.money_state += 4
            else:
                print("Out of Resources")
        elif inquiry == 2:
            if self.check_latte():
                print("I have enough resources, making you a coffee!")
                self.water_state = self.water_state - self.latte_water
                self.milk_state = self.milk_state - self.latte_milk
                self.beans_state = self.beans_state - self.latte_beans
                self.cups_state -= 1
                self.money_state += 7
            else:
                print("Out of Resources")
        elif inquiry == 3:
            if self.check_cappuccino():
                print("I have enough resources, making you a coffee!")
                self.water_state = self.water_state - self.cappuccino_water
                self.milk_state = self.milk_state - self.cappuccino_milk
                self.beans_state = self.beans_state - self.cappuccino_beans
                self.cups_state -= 1
                self.money_state += 6
            else:
                print("Out of Resources")

    def fill(self, water_addition, milk_addition, beans_addition, cups_addition):
        self.water_state += water_addition
        self.milk_state += milk_addition
        self.beans_state += beans_addition
        self.cups_state += cups_addition

    def take(self):
        print("I gave you " + str(self.money_state))
        self.money_state = 0


MachineX = CoffeeMachine(400, 540, 120, 9, 550, True)


while MachineX.power is True:
    MachineX.main()
