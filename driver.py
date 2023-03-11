from getRouteTime import getRouteTimeWithoutStops, getTimeHours, getRouteDistanceKilometers

class Driver:
    def __init__(self, adresses):

        # счет движения и отдыха
        self.trips = []
        self.totalTripTimeWithStops = 0
        self.rideTimeForTheDay = 8
        self.rideTimeInARow = 0
        self.restInARow = 0
        self.currentTrip = 0

        # подсчет дней и времени поездки
        self.getTripTime(adresses)
        self.trips.reverse()
        self.days = round(self.totalTripTimeWithStops / 8)

        # бухгалтерия
        self.dailyPayment = self.days * 700
        self.distance = getRouteDistanceKilometers(adresses)
        self.fuelPayment = self.distance / 100 * 22 * 57.25
        self.bonusPayment = self.distance * 4
        self.totalPayment = self.bonusPayment + self.dailyPayment

    def getTripTime(self, adresses):
        for i in range(0, len(adresses)):
            if i == len(adresses) - 1:
                self.totalTripTimeWithStops += getTimeHours(adresses[i], adresses[0])
                self.trips.append(round(getTimeHours(adresses[i], adresses[0])))
            else:
                self.totalTripTimeWithStops += getTimeHours(adresses[i], adresses[i + 1]) + 1
                self.trips.append(round(getTimeHours(adresses[i], adresses[i + 1])))


