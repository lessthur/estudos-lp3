import usableAquarium

length = float(input("Enter with the aquarium's length: "))
height = float(input("Enter with the aquarium's height: "))
width = float(input("Enter with the aquarium's width: "))
desiredTemperature = float(input("In degrees Celsius, enter with the desired temperature, to calculate the thermostat power: "))
roomTemperature = float(input("In degrees Celsius, enter with the usual room temperature: "))

volume = usableAquarium.calculate_volume(length, height, width)

thermostatPower = usableAquarium.calculate_thermostat_power(volume, desiredTemperature, roomTemperature)

minFiltrationPerHour, maxFiltrationPerHour = usableAquarium.calculate_filtration_per_hour(volume)

print(f"\nThe aquarium's volume is: {volume:.2f} Liters.")
print(f"The aquarium's necessary thermostat power is: {thermostatPower:.2f} Watts.")
print(f"The aquarium's necessary filtration per hour is between: {minFiltrationPerHour:.2f} and {maxFiltrationPerHour:.2f} Liters per hour.")

