
#task 1.1
for i in range(5, 2, -1):
    print(i)
    
#task 1.2

import random
mood = ["Happy", "Sad", "Angry", "Excited", "Nervous"]

for i in range(len(mood)):
    indx = random.randint(0, 4)
    print(mood[indx])

#task 1.3

for i in range(10, 0, -1):
    print(i)
    print("\n")

     


#task 2.1

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print("\n")
    
#task 2.2
mood_list = ["Happy", "Sad", "Angry", "Excited", "Nervous"]

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

time = ["morning", "afternoon", "evening"]

for i in range(0, 6):
    print(days[i])
    for i in range(len(time)):
        print("    ", time[i], ": ", mood_list[random.randint(0, 4)])
        print("\n")
    
    print("\n")
        
# task 2.3

for i in range(1,6):
    for k in range(1,6):
        print(i * k, end=" ")
    
    print("\n")
        
# task 3.1

for i in range(1, 11):
    if i == 5:
        continue
    else:
      print(i)     
      
# task 3.2

list = ["Happy", "Sad", "Angry", "Excited", "Nervous"]


for i in range(1, 25):
    
    if i == 12:
        print("Lunchtime")
        continue
    else:
        print("Hour: ", i, " -->", list[random.randint(0, 4)])

# task 3.3

numFound = False

want_to_find = 7

numList = [1, 2, 3, 4, 5, 8, 9, 10]

for i in range(len(numList)):
    if numList[i] == want_to_find:
        numFound = True
        break

if numFound == False:
    print("Number not found")
else:
    print(want_to_find, " is found")
        
# task 4.1


# I predict that the print statement will print 5 times with 
# the number of marshmellows being 1-5
marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")  
    
# the output is just expected because we increment before the print statement so we don't 
# start at 0 in the statement

# task 4.2

# I predict that the print statement will print 5 times with 
# the number of marshmellows being 0-4
marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")  
    marshmallows += 1
    
# the output is just expected because we now increment after the print statement so we
# start at 0 in the statement instead of 1, but after 4, once we increment, marshmellows is not less than 5
# so the while loop stops. The previous printed 5 because we entered the loop with 4 and 4 < 5, but we
# immediately increment to 5 for the print statement

# task 4.3

marsh_in_bag = 1

print("------------")

while marsh_in_bag < 10:
    print("There are now " + str(marsh_in_bag) + " marshmallows  in the bag.") 
    marsh_in_bag += 1
    
# to correct this error (make it 10 in the bag) we should move the increment to before
# the print statement this time because we are starting at 1, but after printing 9,
# the marsh_in_bag increments to 10 which would cause us to break out of the loop
# before there are 10 marshmellows in the bag

# task 5.1

infinite = 0

while infinite > -1:
    
    infinite += 1
    if infinite == 5:
        break
    
# this will give infinite loop because the condition of the loop will always be true
# so it will execute forever, but since we put a break after 5 iterations, the loop
# will automatically break out of the loop and stop
    
# task 5.2

infinite = 0

while infinite != 4:
    
    infinite += 1
    print(infinite)
    
# the condition breaks out of the loop because once the loop runs while the condition is
# true, so once the condition turns false, it stops

# task 5.3

infinite = 0
idx = 0

while (idx < 4) and (infinite != 4):
    
    infinite += 1
    idx += 1
    print("infinite: ", infinite)
    print("indx: " , idx)
    
# this is more complex because both conditions need to be true for the loop to continue.
# If one condition is false then the loop will stop


#task 6.1

numFound = False

idx = 0

want = 7

numList = [1, 2, 3, 4, 5, 8, 9, 10]

while idx < len(numList) -1 :
    if numList[idx] == want:
        numFound = True
        break
    idx += 1

if numFound == False:
    print("Number not found")
else:
    print(want_to_find, " is found")
    
# the else works with the loop because if the number is found then the loop breaks 
# taking the user straight to the end to go through the final if statement

# task 6.2

target = 7

curr = 0

while curr != -1:
    if curr == target:
        
        break
    curr += 1

# the the if condition is true and it enters the break, it will leave the loop
# even though the while loop will go on infinitely


# task 6.3
i = 0
while i in range(27):
    i += 1
    if i % 2 == 0:
        continue
    else:
      print(i)     
      
#  if the loop enters the continue statment it skips everything in the code and continues
# to the next iteration


# task 6.4

i = 0
while i in range(27):
    if i == 18:
        pass
    else:
      print(i) 
      
    i += 1
    
# if the loop enters the pass statment it continues
# to the next part of the code, so its helpful for when you are planning to implement more code
# later on

# task 7.1

import random

# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary--> already updates it
    roll_count[dice_roll] += 1 
    print("You rolled a " + str(dice_roll) + "!")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")
    
    
# task 7.2
list = [1, 6, 87, 90, 100]
computer = random.choice(list) 

inpt = int(input("Guess the choice: "))

if inpt == computer:
    print("winner")
    
else:
    print("loser")
    
# guessed correctly

# task 7.3
card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
computer = random.shuffle(card)

for auto in card:
    print(auto)
      
# task 8.1
computer = random.randint(0, 10)
inpt = int(input("Guess the number: "))
correct = False

while not correct:
    if inpt < computer:
        print("Too low")
        
    elif (inpt > computer):
        print("Too high")
        
    else:
        correct = True
        
# task 8.2

import random
advice = ["get help", "seek therapy", "laugh", "dont procrastinate"]
inpt = input("Question: ")
computer = random.choice(advice) 

while inpt != "Done":
    
    print(computer)
    inpt = input("Question: ")
    
# task 8.3
import random
card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
computer = random.choice(card)

inpt = input("user guess: ")

if inpt == str(computer):
    print("win")
else:
    print("lose")
        

# task 9.1

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Initialize track number --> already made a counter
track_number = 1 

# Spinning through the genres --> already made a for loop
for genre in genres:
    print(f"Track {track_number}: Now playing {genre}") # already has message
    track_number += 1
    
# task 9.2 --> I think this task was already solved

# Our playlist is still going
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0  # We start at the first track

# Keep the party alive until we've reached a specific genre
stop_genre = 'Hip-hop'

# Keep the party alive until we've reached the end or the stop_genre
while i < len(genres) and genres[i] != stop_genre:
    print("Remixing: " + genres[i])
    i += 1  # Move to the next track

# task 9.3 --> already answered

# Our playlist needs a light show
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
unsuitable_genre = 'Classical'

for index in range(len(genres)):
    if genres[index] == unsuitable_genre:
        continue  # Skip the light show for this genre
    print(f"Track {index + 1}: {genres[index]} - Light show is on!")
    
    
# task 10.1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
# Selective playlist slice
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)
    
    
#task 10.2

music_genres = [genre + " Music" for genre in genres]
print(music_genres)

# task 10.3
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")