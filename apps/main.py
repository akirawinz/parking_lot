# There are 6 spots available in the parking lot

# Two classes:

# Car class
# Constructor with information about the car

# Garage class
# Dsiplays spots availables on Garage
# Add cars to Garage
# Remove cars from garage
# show cars of garage


# Defining the Car class
class Car:

    # You can think of the __init__ function as the class Constructor.
    # Whenever we create an instance of this class we will need to add the license plate and color.
    def __init__(self, license_plate, color):
        self.license_plate = license_plate
        self.color = color

    # this dunder method returns the license plate, model and color whenever we print an instance of the class to the console
    def __repr__(self):
        return f'{self.license_plate}, {self.color}'


# Defining the Garage class
class Garage:

    # Class Constructor with four attributes (cars_added, spots, car_info)
    def __init__(self):
        self.cars_added = []
        self.spots = 6
        self.car_info = {}

        # This identifiers will be assigned to every car that enters the parking lot.
        # There are 6 identifiers because there are 6 spots available for parking.
        self.identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']


    # this function returns the number of spots availables
    def spots_available(self):
        return self.spots

    # the add_car function adds a car to the parking lot. It takes one input parameter
    # That input parameter must be the license plate, Model and Color
    def add_car(self, car):

        # Here we check if we have any spots available
        if self.spots > 0:
            print("Start Parking car")
            # if we have spots available we make a list from the input using the built-in function .split()
            # and then we append that list to the self.cars_added attribute that we created before
            self.cars_added.append(str(car).split(', '))

            # subtract one from self.spots because we have one less spot available
            self.spots -= 1

            # Here we modify the dict attribute car_info that we created before and we create the keys 'code', 'license plate', 'model', 'color'
            # and we put lists as the values of the dictionary
            self.car_info = {'code': [], 'license plate': [], 'Color': []}
            #print("before add cars :", self.car_info)

            # we loop through the cars_added list to access all the cars on the parking lot
            for index, i in enumerate(self.cars_added):

                # then we append the code to the 'code' key, we append the license plate to the 'license plate' key and so on and so forth
                self.car_info['code'].append(self.identifier[index])
                self.car_info['license plate'].append(i[0])
                self.car_info['Color'].append(i[1])
                
            #print("total add cars :", self.car_info)
            
            return "car successfully added to the parking lot"

        # if zero is greater than spots then we don't add the car to the parking lot
        else:
            print(f"We have {self.spots} spots available. I am sorry ")

    # this function removes the car from the parking lot
    # it takes two inputs parameters: the code that was assigned to your car and the time that you had your car parked in hours
    def remove_car(self, given_code):

        # here we check how many codes we have in the car_info dict, we want to see how many cars are currently parked
        past_len = len(self.car_info['code'])

        # if the code passed to the function is not stored in our car_info dictionary
        if given_code not in self.car_info['code']:
            print("car not found")

        else:
            # if the given_code is in the dictionary then we loop through every code on our dictionary till we find it the matching code and its index
            #print("befor remove cars :", self.car_info)
            for index, value in enumerate(self.car_info['code']):
                if value == given_code:

                    # using the index then we can find all the car's information
                    print("Remove code's:",self.car_info['code'][index], self.car_info['license plate'][index], self.car_info['Color'][index])

                    # here we remove all the information about the car using .pop(index)
                    # and we store the code from the removed car on the removed_car_index variable
                    removed_car_index = self.car_info['code'].pop(index)
                    self.car_info['license plate'].pop(index)
                    self.car_info['Color'].pop(index)

                    # once the car is successfully removed, we add one to self.spots because we have one more spot available
                    self.spots += 1
                    self.identifier.append(given_code)

            #print("total remove cars :", self.car_info)
            return "car successfully remove from the parking lot"
    # displayes all cars in garage
    def cars_in_garage(self):
            for i in self.car_info.items():
                print(i)

    # displayes registration_numbers in garage
    def registration_numbers(self, given_color):

        # if the license plate passed to the function is not stored in our car_info dictionary
        if given_color not in self.car_info['Color']:
            return("car not found")
        else:
            # if the given_code is in the dictionary then we loop through every code on our dictionary till we find it the matching code and its index
            summary = []
            for index, value in enumerate(self.car_info['Color']):
                if value == given_color:

                    # using the index then we can find all the car's information
                    summary.append(self.car_info['license plate'][index])

            return (summary)

    # displayes slot_number by color in garage
    def slot_number_color(self, given_color):

        # if the license plate passed to the function is not stored in our car_info dictionary
        if given_color not in self.car_info['Color']:
            return("car not found")
        else:
            # if the given_code is in the dictionary then we loop through every code on our dictionary till we find it the matching code and its index
            summary = []
            for index, value in enumerate(self.car_info['Color']):
                if value == given_color:

                    # using the index then we can find all the car's information
                     summary.append(self.car_info['code'][index])

            return (summary)

    # displayes slot_number by plate in garage
    def slot_number_plate(self, given_code):

        # if the license plate passed to the function is not stored in our car_info dictionary
        if given_code not in self.car_info['license plate']:
            return("car not found")
        else:
            # if the given_code is in the dictionary then we loop through every code on our dictionary till we find it the matching code and its index
            for index, value in enumerate(self.car_info['license plate']):
                if value == given_code:

                    # using the index then we can find all the car's information
                    return (self.car_info['code'][index])

my_garage = Garage()
print('create_parking_lot',my_garage.spots_available())

print("Start Operation 6 cars parking.......")
print(my_garage.add_car(Car("KA-01-HH-1234","white")))
print(my_garage.add_car(Car("KA-01-HH-9999","white")))
print(my_garage.add_car(Car("KA-01-BB-0001","Black")))
print(my_garage.add_car(Car("KA-01-HH-7777","Red")))
print(my_garage.add_car(Car("KA-01-HH-2701","Blue")))
print(my_garage.add_car(Car("KA-01-HH-3141","Black")))
print("End Operation car parking.......")

print("Start Operation 4 cars leaving.......")
print(my_garage.remove_car("A1"))
print(my_garage.remove_car("B1"))
print(my_garage.remove_car("C1"))
print(my_garage.remove_car("D1"))
print("end Operation car leaving.......")

print("Start Operation status.......")
my_garage.cars_in_garage()
print("spots_available :", my_garage.spots_available())   
print("End Operation status.......")

print("Start Operation 2 cars parking.......")
print(my_garage.add_car(Car("KA-01-P-333","White")))
print(my_garage.add_car(Car("DL-12-AA-9999","White")))
print("End Operation car parking.......")

print("registration_numbers_for_cars_with_colour White :",my_garage.registration_numbers("white"))
print("slot_numbers_for_cars_with_colour White :",my_garage.slot_number_color("white"))
print("slot_number_for_registration_number KA-01-HH-3141 :",my_garage.slot_number_plate("KA-01-HH-3141")) 
print("slot_number_for_registration_number MH-04-AY-1111 :", my_garage.slot_number_plate("MH-04-AY-1111")) 

print("Exit Program")