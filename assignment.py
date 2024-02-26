# 1. Nested Decisions: The Adventure Game
# Task 1: Code Correction
# Task 2: Setting the Scene
# Task 3: Default Path
place = input("Choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("you light a torch to see a treasure in the corner of the room!")
    elif action == "proceed in the dark":
        print("you get eaten by a skeleteon")
    else:
        pass

# 2. Quick Decisions: The Event Planner
# Task 1: Code Correction
# Task 2: Venue Selection
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
projector = "xl" if attendees > 100 else "medium"
audio_system = "surround sound" if attendees > 100 else "device sound should be okay"
print(venue)
print(projector)
print(audio_system)

# Task 3: Catering Choices
food_choice = input("Do you want vegetarian food? (yes/no) ")
catering_choice = "Veggie Delight Caterers" if food_choice == "yes" else "Gourmet Meals Caterers"
print(catering_choice)

# 3. Silent Failures: The Error Handler
# Task 1: Code Correction
# Task 2: Division Calculator
def strangeDivision(x):
    try:
        y = 1 / x
    except ZeroDivisionError:
        pass
    except TypeError:
        pass
strangeDivision(0)
strangeDivision("test")

# Task 3: File Reader
file_name = input("Please enter a file name, including its extension: ")
try:
    f = open(file_name, 'rb')
except FileNotFoundError:
    pass

# 4. Nested Quick Decisions: The Shopping Assistant 
# Task 1: Code Correction
weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)

# 5. The Silent Logger: System Monitor
# Task 1: Code Correction
# Task 2: System Check
import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)
if cpu_usage > 90 and memory_usage > 90 and disk_space > 90:
    print("High CPU, memory, and disk space usage!")
elif cpu_usage > 80 and cpu_usage <= 90 or memory_usage > 80 and memory_usage <= 90 or disk_space > 80 and disk_space <= 90:
    pass
