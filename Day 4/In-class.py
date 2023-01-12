''' LESSON 1 - RANDOM MODULE '''
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.pi)

randomFloat = random.random()  # For random float between 0 and 0.999999999999
print(randomFloat)

randomFloat = random.random() * 5  # For random float between 0 and and 4.99999999999
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

''' LESSON 2 - Undertanding the offset and appending items to a list'''

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])  # "Delaware"
print(states_of_america[-1])  # "Hawaii"

states_of_america[1] = "Pencilvania"

states_of_america.append("Honeyland")
print(states_of_america)

states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)
print()

# Take note f Index Out Of Range Error
