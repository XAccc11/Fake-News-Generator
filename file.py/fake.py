#import the random module
import random

subjects = [
      "sharukh khan",
      "virat kohli",
      "cristiano ronaldo",
      "lebron james",
      "a group of monkeys",
      "a pack of wolves",
      "prime minister of india"
 ]

actions = [
   "launches",
   "destroys",
   "creates",
   "writes",
   "throws",
   "eats",
   "sells",
   "dance"
]

Places_of_things = [
   "at red fort",
   "in the moon",
   "at the white house",
   "during ipl match",
   "at the olympics",
   "at india gate"
]

while True:
   subject = random.choice(subjects)
   action = random.choice(actions)
   place_of_thing = random.choice(Places_of_things)
   Headline = print(f"{subject} {action} {place_of_thing}")
   user_input = input("\n Do you want another headline?(Yes/No): ").strip().lower()
   if user_input != 'yes':
      break

print("\nThank you for using the fake news generator!")