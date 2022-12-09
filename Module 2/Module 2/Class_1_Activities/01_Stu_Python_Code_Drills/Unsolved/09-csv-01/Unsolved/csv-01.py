# Import the necessary libraries for reading csv files

import csv 
from pathlib import Path

# Set the path for the csv file
file_path=Path('09-csv-01/Resources/pokemon.csv')

# Create new lists to store data for heaviest and tallest Pokemon


# Open the csv
with open(file_path, 'r') as f:

    csv_reader=csv.reader(f)
    #print(len(list(csv_reader)))
    #[[id,identifier,species_id,height,weight,base_expereince,order,is_default] <-
    # [1,bulbasaur,1,7,69,64,1,1] <-, etc]

    # Iterate through the data and search for the number the user inputted. Remember to skip the header of the CSV.
    next(csv_reader)
    for each_pokemon in csv_reader:
        # each_pokemon <=> [1,bulbasaur,1,7,69,64,1,1]


        # Print the name of the Pokemon(identifier) and Pokedex number(species id) at that number. For example, "Pokemon No. 25 - Pikachu".
        print(f'Pokemon No. {each_pokemon[2]} - {each_pokemon[1].capitalize()}')

        # Iterate through the data and search for Pokemon whose weight is greater than 3000. Append only the Pokemon's name and weight to the 'heaviest' list.
        if int(each_pokemon[4]) > 3000:
            heavy_list.append([each_pokemon[1], each_pokemon [4]])


        # Iterate through the data and search for Pokemon whose height is greater than 50. Append only the Pokemon's name and height to the 'tallest' list.
        if int(each_pokemon[3]) > 50:
            tall_list.append([each_pokemon[1], each_pokemon [4]])


# Print the list of heaviest and tallest pokemon

print(tall_list)
print(heavy_list)

write_file_path=Path('output.csv')
with open(write_file_path)(f, delimiter='|')
    for each_row
