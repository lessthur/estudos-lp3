def calculate_volume(length, height, width):
    return (length * height * width) / 1000

def calculate_thermostat_power(volume, desiredTemperature, roomTemperature):
    return volume * 0.05 * (desiredTemperature - roomTemperature)

def calculate_filtration_per_hour(volume):
    return volume *2, volume * 3 