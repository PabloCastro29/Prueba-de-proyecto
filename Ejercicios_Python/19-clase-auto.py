class Car:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def status(self):
        if self.is_on:
            print("El auto está encendido.")
        else:
            print("El auto está apagado.")

my_car = Car()
my_car.turn_on()
my_car.status()
my_car.turn_off()
my_car.status()
