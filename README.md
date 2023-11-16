# Parking Lot Management System

## File Structure

1. **main.py:** Terminal interface operations.
2. **vehicle.py:** Vehicle information class.
3. **parking_lot.py:** Parking utility functions.

## Exception Handling

Exceptions are handled, and any errors during execution are logged in a separate file named **error.log**.

## Approach

### Vehicle Class
- Contains vehicle unique number and is expandable to add further information.

### ParkingLot Class
- Functions:
  1. `assign_parking_space`: Assigns a parking space to a vehicle.
  2. `retrieve_parking_spot`: Retrieves information about a parked vehicle.
  3. `unpark_vehicle`: Unparks a vehicle.

### ParkingInterface Class
- Terminal UI for user interaction.
- Options for users to select various parking operations.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/GSHitesh/leegality_parkinglot.git
    cd leegality_parkinglot
    ```

2. Run the program:
    ```bash
    python3 main.py
    ```

## Code Readability

- Comments and annotations are used throughout the code for clarity.
- Variable types and return types are clearly documented.
