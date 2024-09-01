import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# List of times of the day
times_of_day = ["Morning", "Afternoon", "Evening"]

# Loop through each day of the week
for day in range(7):
    print(f"Day {day + 1}:")
    # Loop through each time of the day
    for time in times_of_day:
        # Randomly select a mood from the list
        mood = random.choice(moods)
        # Print the time of day and the selected mood
        print(f"  {time}: {mood}")
    print()  # Print a blank line between days
