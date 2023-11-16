"""Module for parking related operations"""
import logging
import inspect

from vehicle import Vehicle

logging.basicConfig(filename='error.log')



class ParkingLot:
    """Parkinglot class"""

    def __init__(self) -> None:
        self.levels: dict = {"A": list(range(1, 21)), "B": range(21, 41)}
        self.parked_vehicles: dict = {}

    def assign_parking_space(self, vehicle: Vehicle) -> str:
        """method to assign parking space"""
        try:
            for level, spots in self.levels.items():
                if spots:
                    spot_number: int = spots.pop(0)
                    self.parked_vehicles[vehicle.vehicle_number] = {
                        "level": level,
                        "spot": spot_number,
                    }
                    return f"Parking assigned - Level: {level}, Spot: {spot_number}"
            return "Parking lot is full"
        except Exception as ex:
            method = inspect.currentframe().f_code.co_name
            logging.error("Exception %s occured in method %s",ex,method)
            return {}

    def retrieve_parking_spot(self, vehicle_number: str) -> dict:
        """method to fetch parking spot"""
        try:
            if vehicle_number in self.parked_vehicles:
                return self.parked_vehicles[vehicle_number]
            else:
                return "Vehicle not found in the parking lot"
        except Exception as ex:
            method = inspect.currentframe().f_code.co_name
            logging.error("Exception %s occured in method %s",ex,method)
            return ""

    def unpark_vehicle(self, vehicle_number: str) -> str:
        """method to unpark vehicle from parking"""
        try:
            if vehicle_number in self.parked_vehicles:
                level, spot = self.parked_vehicles.pop(vehicle_number).values()
                self.levels[level].append(spot)
                self.levels[level].sort()
                return f"Vehicle unparked from Level: {level}, Spot: {spot}"
            else:
                return "Vehicle not found in the parking lot"
        except Exception as ex:
            method = inspect.currentframe().f_code.co_name
            logging.error("Exception %s occured in method %s",ex,method)
            return ""
