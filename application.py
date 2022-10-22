class Automobile:

    def __init__(self):
        self.__make = ""
        self.__model = ""
        self.__color = ""
        self.__year = 0
        self.__mileage = 0

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @property
    def year(self):
        return self.__year

    @property
    def mileage(self):
        return self.__mileage

    @make.setter
    def make(self, make):
        if not isinstance(make, str):
            raise ValueError("Make must be string")
        self.__make = make

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise ValueError("Model must be string")
        self.__model = model

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise ValueError("Color must be string")
        self.__color = color

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise ValueError("Year must be int")
        self.__year = year

    @mileage.setter
    def mileage(self, mileage):
        if not isinstance(mileage, int):
            raise ValueError("Mileage must be int")
        self.__mileage = mileage

    def __str__(self):
        return "{} {} {} {} {}".format(self.make, self.model, self.color, self.year, self.mileage)


class VehicleManager:

    def __init__(self):
        self.__vehicle_list = []

    def run(self):
        EXIT = 0
        ADD = 1
        REMOVE = 2
        UPDATE = 3
        PRINT = 4

        while True:
            print("Commands:")
            print("\t{}: Exit".format(EXIT))
            print("\t{}: Add a new vehicle".format(ADD))
            print("\t{}: Remove a vehicle".format(REMOVE))
            print("\t{}: Update vehicle attributes".format(UPDATE))
            print("\t{}: Print all vehicles".format(PRINT))
            print("")

            try:
                command = int(input("Enter command: "))
            except ValueError:
                print("Unknown command")
                continue

            if command == EXIT:
                self.save_vehicles()
                break
            elif command == ADD:
                self.add_vehicle()
            elif command == REMOVE:
                self.remove_vehicle()
            elif command == UPDATE:
                self.update_vehicle()
            elif command == PRINT:
                self.print_vehicles()
            else:
                print("Unknown command")

            print("")

        print("\nThanks for using our program!")

    def add_vehicle(self):
        vehicle = self.get_vehicle()
        self.__vehicle_list.append(vehicle)
        print("Added")

    def remove_vehicle(self):
        if len(self.__vehicle_list) == 0:
            print("Nothing to remove")
            return

        self.print_vehicles()
        i = self.get_index()
        self.__vehicle_list.pop(i)
        print("Removed")

    def update_vehicle(self):
        self.print_vehicles()

        i = self.get_index()
        vehicle = self.get_vehicle()

        self.__vehicle_list[i] = vehicle
        print("Updated")

    def get_vehicle(self):
        print("Enter vehicle")

        vehicle = Automobile()

        vehicle.make = input("\tMake: ")
        vehicle.model = input("\tModel: ")
        vehicle.color = input("\tColor: ")

        while True:
            try:
                vehicle.year = int(input("\tYear: "))
                break
            except ValueError:
                print("Year must be number")

        while True:
            try:
                vehicle.mileage = int(input("\tMileage: "))
                break
            except ValueError:
                print("Mileage must be number")

        return vehicle

    def get_index(self):
        while True:
            try:
                i = int(input("Enter index: "))
            except ValueError:
                print("Index must be number")
                continue

            if i < 0 or i >= len(self.__vehicle_list):
                print("Incorrect index")
                continue

            return i

    def print_vehicles(self):
        if len(self.__vehicle_list) == 0:
            print("There are no vehicles")
            return

        for i, vehicle in enumerate(self.__vehicle_list):
            print("{}. {}".format(i, vehicle))

    def save_vehicles(self):
        file_name = input("Enter file name to save vehicles: ")
        with open(file_name, 'w') as file:
            for vehicle in self.__vehicle_list:
                file.write(str(vehicle) + "\n")
        print("Saved")


if __name__ == '__main__':
    vehicle_manager = VehicleManager()
    vehicle_manager.run()
