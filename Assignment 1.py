# Customer class
class Customer:
    def __init__(self, customerID, firstName, lastName, email):
        self.__customerID = customerID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email

    # Getters
    def get_customerID(self):
        return self.__customerID

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_email(self):
        return self.__email

    # Setters
    def set_customerID(self, customerID):
        self.__customerID = customerID

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_email(self, email):
        self.__email = email

    def display_customer_info(self):
        return f"Your Name: {self.__firstName} {self.__lastName}\nYour Email: {self.__email}"

# Room class
class Room:
    def __init__(self, roomID, roomType, pricePerNight, isAvailable):
        self.__roomID = roomID
        self.__roomType = roomType
        self.__pricePerNight = pricePerNight
        self.__isAvailable = isAvailable

    # Getters
    def get_roomID(self):
        return self.__roomID

    def get_roomType(self):
        return self.__roomType

    def get_pricePerNight(self):
        return self.__pricePerNight

    def get_isAvailable(self):
        return self.__isAvailable

    # Setters
    def set_roomID(self, roomID):
        self.__roomID = roomID

    def set_roomType(self, roomType):
        self.__roomType = roomType

    def set_pricePerNight(self, pricePerNight):
        self.__pricePerNight = pricePerNight

    def set_isAvailable(self, isAvailable):
        self.__isAvailable = isAvailable

    def display_room_info(self):
        return f"Room Type: {self.__roomType}"

# Reservation class
class Reservation:
    def __init__(self, reservationID, checkInDate, checkOutDate, numNights, room, customer):
        self.__reservationID = reservationID
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__numNights = numNights
        self.__room = room
        self.__customer = customer

    # Getters
    def get_reservationID(self):
        return self.__reservationID

    def get_checkInDate(self):
        return self.__checkInDate

    def get_checkOutDate(self):
        return self.__checkOutDate

    def get_numNights(self):
        return self.__numNights

    def get_room(self):
        return self.__room

    def get_customer(self):
        return self.__customer

    # Setters
    def set_reservationID(self, reservationID):
        self.__reservationID = reservationID

    def set_checkInDate(self, checkInDate):
        self.__checkInDate = checkInDate

    def set_checkOutDate(self, checkOutDate):
        self.__checkOutDate = checkOutDate

    def set_numNights(self, numNights):
        self.__numNights = numNights

    def set_room(self, room):
        self.__room = room

    def set_customer(self, customer):
        self.__customer = customer

    def display_reservation_info(self):
        return (f"Check-In: {self.__checkInDate} - 3:00 PM\nCheck-Out: {self.__checkOutDate} - 12:00 PM\n"
                f"Number of Nights: {self.__numNights}\nNumber of Rooms: 1\n"
                f"Room 1: {self.__customer.get_firstName()} {self.__customer.get_lastName()}\n"
                f"{self.__room.display_room_info()}")

# Payment class
class Payment:
    def __init__(self, paymentID, billingName, creditCard, roomCost, nights, taxesFees, totalAmount):
        self.__paymentID = paymentID
        self.__billingName = billingName
        self.__creditCard = creditCard
        self.__roomCost = roomCost
        self.__nights = nights
        self.__taxesFees = taxesFees
        self.__totalAmount = totalAmount

    # Getters
    def get_paymentID(self):
        return self.__paymentID

    def get_billingName(self):
        return self.__billingName

    def get_creditCard(self):
        return self.__creditCard

    def get_roomCost(self):
        return self.__roomCost

    def get_nights(self):
        return self.__nights

    def get_taxesFees(self):
        return self.__taxesFees

    def get_totalAmount(self):
        return self.__totalAmount

    # Setters
    def set_paymentID(self, paymentID):
        self.__paymentID = paymentID

    def set_billingName(self, billingName):
        self.__billingName = billingName

    def set_creditCard(self, creditCard):
        self.__creditCard = creditCard

    def set_roomCost(self, roomCost):
        self.__roomCost = roomCost

    def set_nights(self, nights):
        self.__nights = nights

    def set_taxesFees(self, taxesFees):
        self.__taxesFees = taxesFees

    def set_totalAmount(self, totalAmount):
        self.__totalAmount = totalAmount

    def display_payment_info(self):
        return (f"Billing Name: {self.__billingName}\nCredit Card: {self.__creditCard}\n"
                f"Room Cost: {self.__roomCost} AED per night\n"
                f"Nights: {self.__nights}\nRoom Subtotal: {self.__roomCost * self.__nights:.2f} AED\n"
                f"Taxes and Fees: {self.__taxesFees:.2f} AED\nTotal Charges: {self.__totalAmount:.2f} AED")


# Creating objects and displaying the information
customer = Customer(101, "Khaled", "Ali", "khaled.ali@gmail.com")
room = Room(1, "2 Queen Beds / No Smoking / Desk / Safe / Coffee Maker", 970.00, True)
reservation = Reservation(1001, "Mon, Sep 30, 2024", "Wed, Oct 2, 2024", 2, room, customer)
payment = Payment(2001, "Khaled Ali", "Visa (ending in 1234)", 970.00, 2, 97.00, 2037.00)

# Displaying all the reservation and payment information
print("Your Reservation Is Confirmed")
print(customer.display_customer_info())
print("Hotel Confirmation Number: 52523687")
print()
print("Emirates Palace")
print(reservation.display_reservation_info())
print()
print("Summary of Charges")
print(payment.display_payment_info())
