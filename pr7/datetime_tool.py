from datetime import datetime
import time

class CurrentDateTime:
    def Display_current_datetime(self):
        current_datetime = datetime.now()
        print("-" * 50)
        print("Current date and time:", current_datetime.strftime("%d-%m-%Y %H:%M:%S"))
        print("-" * 50)

class DateDifference:
    def __init__(self, date1_input, date2_input):
        self.date1_input = date1_input
        self.date2_input = date2_input

    def calculate_difference_between_two_dates(self):
        date1 = datetime.strptime(self.date1_input, "%Y-%m-%d")
        date2 = datetime.strptime(self.date2_input, "%Y-%m-%d")
        difference = date2 - date1
        print(f"The difference between the two dates is: {difference.days} days.")

class Stopwatch:
    def stopwatch(self):
        input("Press Enter to start the stopwatch...")
        start_time = time.time()
        input("Press Enter to stop the stopwatch...")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("*" * 40)
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print("*" * 40)

class Timer:
    def countdown_timer(self):
        seconds = int(input("Enter time in seconds: "))
        while seconds:
            mins, secs = divmod(seconds, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            print(time_format, end="\r")
            time.sleep(1)
            seconds -= 1
        print("*" * 40)
        print("00:00\nTime's up!")
        print("*" * 40)

class Format:
    def custome_format(self):
        current_datetime = datetime.now()
        print("*" * 60)
        print("Current date and time:", current_datetime.strftime("%A, %d %B %Y - %I:%M %p"))
        print("*" * 60)
