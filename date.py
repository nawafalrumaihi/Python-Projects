import pytz
from datetime import datetime

# Set the time zones for Vancouver and Bahrain
vancouver_tz = pytz.timezone('America/Vancouver')
bahrain_tz = pytz.timezone('Asia/Bahrain')

# Loop until the user types 'quit'
while True:
    # Get the current time in Vancouver and Bahrain
    vancouver_time = datetime.now(vancouver_tz)
    bahrain_time = datetime.now(bahrain_tz)

    # Print the current time in Vancouver and Bahrain
    print("Current time in Vancouver:", vancouver_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
    print("Current time in Bahrain:", bahrain_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

    # Ask the user if they want to quit
    user_input = input("Type 'quit' to end the program: ")
    if user_input.lower() == 'quit':
        break
