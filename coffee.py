class coffee:
    def get_milk(self):
        print("Get the Milk")

    def pour_milk_into_pan(self):
        print("Pour the milk into the Pan")

    def mix_water(self):
        print('Mix a small amount of water')

    def turn_on_stove(self):
        print("Turn on the Stove")

    def wait_for_boiling(self):
        print("Wait for the Milk to boil")

    def add_coffee_powder(self):
        print("Add Coffee powder")

    def add_sugar(self):
        print("Add Sugar")

    def stir_gently(self):
        print("Stir gently")

    def pour_into_glasses(self):
        print("Pour into two glasses")

    def serve_hot(self):
        print("Serve before it cools down")

    def check_sweetness(self):
        print("Coffee should not be too sweet")

    def check_strength(self):
        print("Coffee should not be too strong")

    def add_water(self):
        print("Add enough water in the mix")

    def prepare_coffee(self):
        print("Preparing coffee for people:")
        self.get_milk()
        self.pour_milk_into_pan()
        self.mix_water()
        self.turn_on_stove()
        self.wait_for_boiling()
        self.add_coffee_powder()
        self.add_sugar()
        self.stir_gently()
        self.pour_into_glasses()
        self.serve_hot()
        print("Coffee is ready to be served!")

    def coffee_taste(self):
        self.check_sweetness()
        self.check_strength()
        self.add_water()
coffee_machine = coffee()
coffee_machine.prepare_coffee()
coffee_machine.coffee_taste()

