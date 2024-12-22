# 1. Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car1:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model



my_car1 = Car1("Renault", "Duster")
print(my_car1.brand + " --> " + my_car1.model)

# -----------------------------------------------------------------------------

# 2. Add a method to the Car class that displays the full name of the car (brand and model).

class Car2:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def getfullName(self):
        return f"{self.brand} {self.model}"
        

my_car_2 = Car2("Maruti" , "Swift")

print(my_car_2.getfullName())

# -----------------------------------------------------------------------------

# 3. Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car2):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

electric_car = ElectricCar("Tesla", "Model s" , "84kWh")

print(electric_car.getfullName())

# -----------------------------------------------------------------------------

# 4.  Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Cars():
    def __init__(self,brand,model):
        # self.brand = brand

        # to make brand variable private we use 2 underscores before the variable declaration
        self.__brand = brand
        # being private means the variable cannot be accessed outside the class , but it can be accessible inside the class.

        self.model = model
    
    def get_brand_name(self):
        return f"{self.__brand} !"

    
cars = Cars("Toyata" , "Model Sx")
# print(cars.brand)
print(cars.get_brand_name())

# -----------------------------------------------------------------------------

# 5. Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class TradCar():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectCar(TradCar):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electric Charged"
    

trad_car = TradCar("Suzuki" , "Wagonr")
elect = ElectCar("Tata" , "Avanen")

print(trad_car.fuel_type())
print(elect.fuel_type())

# -----------------------------------------------------------------------------

# 6. Add a class variable to Car that keeps track of the number of cars created.

class CarsNumber():

    total_cars = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        CarsNumber.total_cars += 1

    
CarsNumber("Renault" , "Kwid")
CarsNumber("Tata" , "Nexon")

print(CarsNumber.total_cars) 
    
# -----------------------------------------------------------------------------

# 7. Add a static method to the Car class that returns a general description of a car.

class CarClass():
    def __init__(self , brand, model):
        self.brand = brand
        self.model = model

    @staticmethod  # static methods refers to such functions of class that can only be called by an actual class and can't be called by object or instance of that class, otherwise will cause conflict.
    def get_description():
        return "Cars have become a daily neccesity to travel"

print(CarClass.get_description())

# -----------------------------------------------------------------------------

# 8. Use a property decorator in the Car class to make the model attribute read-only.

class ModelCar():
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

    @property
    def car_model(self):
        return self.__model


car_prop = ModelCar("Maruti" , "Dx 8")
# car_prop.car_model = "Suzuki" --> Gives Error, since now its a read only variable

print(car_prop.car_model)

# -----------------------------------------------------------------------------

# 9. Demonstrate the use of isinstance() to check if electric_car is an instance of Car2 and ElectricCar.

print(isinstance(electric_car,Car2)) # -> True
print(isinstance(electric_car , ElectricCar)) # -> True

# -----------------------------------------------------------------------------

# 10. Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery():
    def battery_info(self):
        return "This is battery"
    
class Engine():
    def engine_info(self):
        return "This is Engine Info"
    
class CarsReverb(Battery,Engine,Car1):
    pass

multiple_inheritance = CarsReverb("Ford", "Eco-Sports")

print(multiple_inheritance.model + " " + multiple_inheritance.brand)
print(multiple_inheritance.battery_info())
print(multiple_inheritance.engine_info())