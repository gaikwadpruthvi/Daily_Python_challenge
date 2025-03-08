##Store temperature readings in a dictionary by date and allow searching for past data. 
class TemperatureLog:
    def __init__(self):
        self.temperatures = {}

    def record_temperature(self, date, temp):
        self.temperatures[date] = temp
        print(f"Recorded temperature {temp}°C on {date}.")

    def get_temperature(self, date):
        return self.temperatures.get(date, "No data for this date.")

def main():
    temp_log = TemperatureLog()

    while True:
        print("\nTemperature Log System")
        print("1. Record Temperature")
        print("2. Get Temperature")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            temp = float(input("Enter temperature: "))
            temp_log.record_temperature(date, temp)
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            print(f"Temperature on {date}: {temp_log.get_temperature(date)}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
