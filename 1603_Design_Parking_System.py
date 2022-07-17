"""
https://leetcode.com/problems/design-parking-system/
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small,
with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get
into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and
3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false,
else park the car in that size space and return true.


Example 1:

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

Result:
<Results are very inaccurate for this problem>
Runtime: 161 ms, faster than 74.55% of Python3 online submissions for Design Parking System.
Memory Usage: 14.5 MB, less than 14.28% of Python3 online submissions for Design Parking System.
"""


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.car_types = {1: big,
                          2: medium,
                          3: small}

    def addCar(self, carType: int) -> bool:
        if self.car_types[carType] > 0:
            self.car_types[carType] -= 1
            return True
        return False

# Tested directly on leetcode.
