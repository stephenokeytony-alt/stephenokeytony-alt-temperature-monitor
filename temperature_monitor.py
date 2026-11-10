# CTE 123 PYTHON MINI PROJECT
# Project: Temperature Monitor and Alarm Checker
# Department: Mechatronics Engineering
# Institution: Yaba College of Technology

# Function to collect temperature readings
def collect_temperatures():

    # Create an empty list to store temperatures
    temperatures = []

    print("\nTEMPERATURE MONITOR AND ALARM CHECKER")
    print("--------------------------------------")

    # Collect five temperature readings
    for i in range(5):

        while True:
            try:
                reading = float(input(f"Enter temperature reading {i + 1} (°C): "))

                if reading < 0:
                    print("Temperature cannot be below 0°C. Try again.")
                else:
                    temperatures.append(reading)
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

    return temperatures


# Function to analyse temperature readings
def analyse_temperatures(temperatures):

    # Calculate highest, lowest and average temperatures
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    # Set the safe temperature limit
    safe_limit = 60

    print("\nTEMPERATURE ANALYSIS")
    print("--------------------")

    print(f"Highest temperature: {highest}°C")
    print(f"Lowest temperature: {lowest}°C")
    print(f"Average temperature: {average:.2f}°C")

    # Check for temperatures above the safe limit
    print("\nALARM CHECK")
    print("-----------")

    alarm_triggered = False

    for temperature in temperatures:
        if temperature > safe_limit:
            print(f"WARNING! High temperature detected: {temperature}°C")
            alarm_triggered = True

    if alarm_triggered:
        print("ALERT: Machine temperature exceeded the safe limit.")
    else:
        print("NORMAL: All temperature readings are within the safe limit.")

    # Extra feature: Machine condition classification
    print("\nMACHINE CONDITION")
    print("-----------------")

    if highest > safe_limit:
        print("CRITICAL: Machine requires immediate inspection.")
    elif highest >= 50:
        print("CAUTION: Machine temperature is approaching the limit.")
    else:
        print("NORMAL: Machine temperature is within the normal range.")


# Main function
def main():

    # Collect temperature readings
    readings = collect_temperatures()

    # Analyse the collected readings
    analyse_temperatures(readings)

    print("\nTemperature monitoring completed.")


# Run the program
main()
