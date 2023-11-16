"""main module for the interaction"""
from vehicle import Vehicle
from parking_lot import ParkingLot



class ParkingInterface:
    """parkinginterface class"""
    @staticmethod
    def display_menu() -> None:
        """method to display parking options"""
        print("1. Assign Parking Space")
        print("2. Retrieve Parking Spot")
        print("3. Unpark Vehicle")
        print("4. Exit")

    @staticmethod
    def get_user_choice() -> int:
        """method to fetch user input"""
        return int(input("Enter your choice: "))

if __name__ == "__main__":
    parking_lot: ParkingLot = ParkingLot()
    terminal: ParkingInterface = ParkingInterface()

    while True:
        terminal.display_menu()
        choice: int = terminal.get_user_choice()

        if choice == 1:
            vehicle_number: str = input("Enter vehicle number (such as HR123): ")
            vehicle: Vehicle = Vehicle(vehicle_number)
            result: dict = parking_lot.assign_parking_space(vehicle)
            print(result)

        elif choice == 2:
            vehicle_number: str = input("Enter vehicle number (such as HR123): ")
            result: dict = parking_lot.retrieve_parking_spot(vehicle_number)
            print(result)

        elif choice == 3:
            vehicle_number: str = input("Enter vehicle number (such as HR123): ")
            result: dict = parking_lot.unpark_vehicle(vehicle_number)
            print(result)

        elif choice == 4:
            print("Exited")
            break

        else:
            print("Invalid choice. Please try again.")
