# Classes & Objects
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla', 'Model 3')

my_car.get_make_model()
# print(my_car.make)
# print(my_car.model)
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

# all of these classes depend on 'Vehicle' class so they inherit its properties
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model) # this means we will inherit these from the parent so we don't have to re-set these
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')
    
class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

# Polymorphism - the ability to behave differently in response to the same input messages (ie. we will get different responses from these objects even though we are using the same methods)
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()

