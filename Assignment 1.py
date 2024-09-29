# Customer class
class Customer:
    def __init__(self, customerID, firstName, lastName, email):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def display_customer_info(self):
        return f"Your Name: {self.firstName} {self.lastName}\nYour Email: {self.email}"

# Room class
class Room:
    def __init__(self, roomID, roomType, pricePerNight, isAvailable):
        self.roomID = roomID
        self.roomType = roomType
        self.pricePerNight = pricePerNight
        self.isAvailable = isAvailable

    def display_room_info(self):
        return f"Room Type: {self.roomType}"

# Reservation class
class Reservation:
    def __init__(self, reservationID, checkInDate, checkOutDate, numNights, room, customer):
        self.reservationID = reservationID
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.numNights = numNights
        self.room = room
        self.customer = customer

    def display_reservation_info(self):
        return (f"Check-In: {self.checkInDate} - 3:00 PM\nCheck-Out: {self.checkOutDate} - 12:00 PM\n"
                f"Number of Nights: {self.numNights}\nNumber of Rooms: 1\n"
                f"Room 1: {self.customer.firstName} {self.customer.lastName}\n"
                f"{self.room.display_room_info()}")

# Payment class
class Payment:
    def __init__(self, paymentID, billingName, creditCard, roomCost, nights, taxesFees, totalAmount):
        self.paymentID = paymentID
        self.billingName = billingName
        self.creditCard = creditCard
        self.roomCost = roomCost
        self.nights = nights
        self.taxesFees = taxesFees
        self.totalAmount = totalAmount

    def display_payment_info(self):
        return (f"Billing Name: {self.billingName}\nCredit Card: {self.creditCard}\n"
                f"Room Cost: {self.roomCost} AED per night\n"
                f"Nights: {self.nights}\nRoom Subtotal: {self.roomCost * self.nights:.2f} AED\n"
                f"Taxes and Fees: {self.taxesFees:.2f} AED\nTotal Charges: {self.totalAmount:.2f} AED")


# Creating objects and displaying the information
customer = Customer(101, "Khaled", "Ali", "khaled.ali@gmail.com")
room = Room(1, "2 Queen Beds / No Smoking / Desk / Safe / Coffee Maker", 970.00, True)
reservation = Reservation(1001, "Mon, Sep 30, 2024", "Wed, Oct 2, 2024", 2, room, customer)
payment = Payment(2001, "Khaled Ali", "Visa (ending in 1234)", 970.00, 2, 97.00,2037.00)

# Displaying all the resvation and payment information
print("Your Reservation Is Confirmed")
print(customer.display_customer_info())
print("Hotel Confirmation Number: 52523687")
print()
print("Emirates Palace")
print(reservation.display_reservation_info())
print()
print("Summary of Charges")
print(payment.display_payment_info())
