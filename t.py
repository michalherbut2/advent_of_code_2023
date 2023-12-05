# Define the initial seeds in pairs
seed_ranges = [(79, 14), (14, 55), (55, 13), (13, 1)]  # Adjust according to your input

# Initialize a dictionary to store the mappings
mappings = {}

# Function to process a map and update the mappings
def process_map(mapping, source_category, dest_category):
    for dest_start, source_start, length in mapping:
        for i in range(length):
            source_number = source_start + i
            dest_number = dest_start + i
            mappings[(source_category, source_number)] = (dest_category, dest_number)

# Process each map
seed_to_soil_map = [(50, 98, 2), (52, 50, 48)]  # Adjust according to your input
process_map(seed_to_soil_map, "seed", "soil")

soil_to_fertilizer_map = [(0, 15, 37), (37, 52, 2), (39, 0, 15)]  # Adjust according to your input
process_map(soil_to_fertilizer_map, "soil", "fertilizer")

# Repeat the process for other maps...

soil_to_fertilizer_map = [(0, 15, 37), (37, 52, 2), (39, 0, 15)]  # Adjust according to your input
process_map(soil_to_fertilizer_map, "soil", "fertilizer")

fertilizer_to_water_map = [(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)]  # Adjust according to your input
process_map(fertilizer_to_water_map, "fertilizer", "water")

water_to_light_map = [(88, 18, 7), (18, 25, 70)]  # Adjust according to your input
process_map(water_to_light_map, "water", "light")

light_to_temperature_map = [(45, 77, 23), (81, 45, 19), (68, 64, 13)]  # Adjust according to your input
process_map(light_to_temperature_map, "light", "temperature")

temperature_to_humidity_map = [(0, 69, 1), (1, 0, 69)]  # Adjust according to your input
process_map(temperature_to_humidity_map, "temperature", "humidity")

humidity_to_location_map = [(60, 56, 37), (56, 93, 4)]  # Adjust according to your input
process_map(humidity_to_location_map, "humidity", "location")

# Function to convert a source number through the mappings
def convert(source_category, source_number):
    current_category, current_number = source_category, source_number
    while (current_category, current_number) in mappings:
        current_category, current_number = mappings[(current_category, current_number)]
    return current_category, current_number

# Find the lowest location number that corresponds to any of the initial seed numbers
lowest_location_number = float('inf')
for seed_start, seed_length in seed_ranges:
    for i in range(seed_length):
        current_category, current_number = convert("seed", seed_start + i)
        print(current_category)
        if current_category == "location" and current_number < lowest_location_number:
            lowest_location_number = current_number
print(seed_ranges)
print("The lowest location number is:", lowest_location_number)
