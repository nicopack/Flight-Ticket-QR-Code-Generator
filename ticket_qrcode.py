print("Please write everything in CAPITAL LETTERS, except the class, don't use spaces and write the airport as short form (ex. London Heathrow Airport --> LHR) \n")

first_name = input("First Name: ")   #NAME

last_name = input("Last Name: ")   #LAST NAME

booking_ref = input("Booking-Ref: ")   #BOOKING REFERENCE

from_ = input("From: ")   #DEPARTURE (short form)

to = input("To: ")   #ARRIVAL (short form)

flight_operator = input("Flight Operator: ")   #FLIGHT OPERATOR

flight_number = input("Flight Number: ")   #FLIGHT NUMBER

day_in_year = input("Day in year: ")   #DAY OF DEPARTURE IN YEAR (ex. 254)

class_ = input("Class: ")   #Class you fly with... make sure the first letter is capital, to access lounge you will need to put "First" or "Business"

seat = input("Seat: ")   #Put a random seat that goes with the class you choose

boarding_index = "0001"

if class_ == "Economy":
    class_ = "Y"

elif class_ == "Business":   #Some selection for the code generation
    class_ = "C"

elif class_=="First":
    class_="F"

else:
    print("Please write Economy, Business or First.")

ticket = "M1" + last_name + "/" + first_name + "            " + "E" + booking_ref + from_ + to + flight_operator + " " + flight_number + " " + day_in_year + "0" + class_ + seat + boarding_index + "\n"

print(ticket)

print("The QRcode has been generated:)")

import qrcode
img = qrcode.make(ticket)   #QRCode generation
type(img)
img.save("qrcode.png")
