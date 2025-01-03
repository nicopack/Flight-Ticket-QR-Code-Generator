# Flight Ticket QR Code Generator

This script is intended for educational purposes only. It generates a QR code with flight details that resemble a flight ticket. The generated QR code can be scanned to retrieve the flight information. Please ensure that you do not use this tool for any illegal activities or malicious purposes.

## How it Works
1. The script asks for various inputs, such as:
  - First and last name
   - Booking reference
   - Departure and arrival airports (short form, e.g., "LHR" for London Heathrow)
   - Flight operator and number
   - Day of the year for the departure date
   - Class (Economy, Business, or First)
   - Seat

2. After receiving the inputs, it formats the flight details into a string, and the QR code containing this data is generated and saved as `qrcode.png` in the same directory as the script.

## Important Notes
- The QR code will be generated in the same folder where the script is located.
- Make sure to input everything in CAPITAL LETTERS, except the class. Use no spaces and write the airport codes in short form (e.g., "LHR" for London Heathrow).

## Disclaimer
This script is for educational purposes only. I do not condone illegal activities. Use this script responsibly.
