class ParkingLot:

    def __init__(self, id, address):
        self.id = id
        self.address = address

    def addParkingFloor():
        pass

    def addEntrancePanel():
        pass

    def getNewParkingTicket():
        pass

    def isFull():
        pass

class ParkingFloor:

    def __init__(self, name):
        self.name = name

    def updateDisplayBoard():
        pass

    def addParkingSlot():
        pass

    def assignVehicleToSlot():
        pass

    def freeSlot():
        pass


class ParkingDisplayBoard:

    def __init__(self, id, handicappedSpot, compactSpot, largeSpot, motorbikeSpot) :
        self.id = id
        self.handicappedFreeSpot = handicappedSpot
        self.compactFreeSpot = compactSpot
        self.largeFreeSpot = largeSpot
        self.motorbikeFreeSpot = motorbikeSpot
        
    def showEmptySpotNumber() :
        pass