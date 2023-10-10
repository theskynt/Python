class ExitPanel:

    def __init__(self, id) :
        self.id = id

    def scanTick():
        pass

    def processPayment():
        pass

class ParkingAttendantPortal:

    def __init__(self, id) :
        self.id = id

    def scanTick():
        pass

    def processPayment():
        pass


class Payment:

    def __init__(self, creationData, amount, status) :
        self.creationData = creationData
        self.amount = amount
        self.status = status

    def initiateTransaction():
        pass

class CreditCardTransaction(Payment):

    def __init__(self, creationData, amount, status, nameOnCard):
        super().__init__(creationData, amount, status)
        self.nameOnCard = nameOnCard 

class CardTransaction(Payment):

    def __init__(self, creationData, amount, status, cashTendered):
        super().__init__(creationData, amount, status)
        self.cashTendered = cashTendered