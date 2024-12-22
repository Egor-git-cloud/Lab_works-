class vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        print(self.make, self.model)

# class car(vehicle):
#     def __init__(self, make, model, fuel_type):
#         vehicle.__init__(self, make, model)
#         self.fuel_type = fuel_type
#     def get_info(self):
#         print(self.make, self.model, self.fuel_type)

        
class car(vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        print(self.make, self.model, self.fuel_type)
# x = vehicle('toyota', 'x5')
x = car('toyota', 'x5', 'benz')
x.get_info()
