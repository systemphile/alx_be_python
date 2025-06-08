# Pytthon script that uses the datetime module
from datetime import datetime, timedelta

#function displays the current date
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date():
    future = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=future)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

display_current_datetime()
calculate_future_date()