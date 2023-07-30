import time
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.cleanliness = 50
        self.health = 100

    def adventure(self):
        print(f"{self.name} and you go on an adventure.")
        
        # Probability of each event happening during the adventure
        event_probabilities = {
            "found_treasure": 0.2,
            "got_sick": 0.15,
            "new_friend": 0.3,
            "lost_in_forest": 0.1,
            "mysterious_encounter": 0.1,
            "rainy_weather": 0.25
        }

        event_occurred = False

        for event, probability in event_probabilities.items():
            if random.random() < probability:
                event_occurred = True
                if event == "found_treasure":
                    print(f"Congratulations! {self.name} found a treasure chest.")
                    self.happiness += 20
                    self.energy -= 10
                elif event == "got_sick":
                    print(f"Oh no! {self.name} got sick.")
                    self.health -= 20
                    self.happiness -= 10
                elif event == "new_friend":
                    print(f"{self.name} made a new friend!")
                    self.happiness += 15
                elif event == "lost_in_forest":
                    print(f"{self.name} got lost in the forest!")
                    self.energy -= 15
                elif event == "mysterious_encounter":
                    print(f"{self.name} had a mysterious encounter.")
                    self.happiness += 10
                elif event == "rainy_weather":
                    print(f"It's raining during the adventure.")
                    self.happiness -= 10
                    self.cleanliness -= 20

                self._update_status()

        if not event_occurred:
            print("Nothing happened during the adventure.")

    def feed(self):
        print(f"{self.name} happily eats the food.")
        self.hunger -= 20
        self.happiness += 10
        self.health += 15
        self._update_status()

    def play(self):
        print(f"{self.name} enjoys playing with you.")
        self.hunger += 10
        self.happiness += 20
        self.energy -= 15
        self.cleanliness -= 10
        self._update_status()

    def sleep(self):
        print(f"{self.name} goes to sleep.")
        self.energy += 30
        self.hunger += 10
        self.health += 20
        self._update_status()

    def bathe(self):
        print(f"{self.name} takes a bath.")
        self.cleanliness += 30
        self.happiness += 5
        self.health += 15
        self._update_status()

    def age_up(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

    def _update_status(self):
        self.hunger = max(0, min(self.hunger, 100))
        self.happiness = max(0, min(self.happiness, 100))
        self.energy = max(0, min(self.energy, 100))
        self.cleanliness = max(0, min(self.cleanliness, 100))
        self.health = max(0, min(self.health, 100))

    def show_status(self):
        print(f"{self.name}'s Status:")
        print(f"Age: {self.age}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")
        print(f"Cleanliness: {self.cleanliness}")
        print(f"Health: {self.health}")
        if self.hunger < 30:
            print(f"⚠️ {self.name} is hungry! Feed {self.name} to keep them happy and healthy.")
        if self.energy < 30:
            print(f"⚠️ {self.name} is low on energy! Let {self.name} sleep to replenish their energy.")
        if self.cleanliness < 30:
            print(f"⚠️ {self.name} is dirty! Give {self.name} a bath to improve their cleanliness.")
        if self.health < 30:
            print(f"⚠️ {self.name} is not feeling well! Take care of {self.name}'s health.")


def get_random_name():
    names = ["Buddy", "Fluffy", "Whiskers", "Spike", "Luna", "Nibbles", "Coco", "Oreo"]
    return random.choice(names)

def main():
    name = input("Enter a name for your virtual pet: ")
    if not name:
        name = get_random_name()

    pet = VirtualPet(name)
    print(f"Welcome to the Virtual Pet game! Meet your new pet, {pet.name}!")

    
    start_time = time.time()

    while True:
        print("\nCommands: feed, play, sleep, bathe, status, adventure, exit")
        command = input("Enter a command: ").lower()

        if command == "feed":
            pet.feed()
        elif command == "adventure":
            pet.adventure()
        elif command == "play":
            pet.play()
        elif command == "sleep":
            pet.sleep()
        elif command == "bathe":
            pet.bathe()
        elif command == "status":
            pet.show_status()
        elif command == "exit":
            print("Thanks for playing with your Virtual Pet! See you again!")
            break
        else:
            print("Invalid command. Try again.")
       
        current_time = time.time()
        elapsed_minutes = int((current_time - start_time) / 60)
        pet._update_status()

        if elapsed_minutes >= 1:
            for _ in range(elapsed_minutes):
                pet.age_up()
                pet.hunger += 5
                pet.happiness -= 5
                pet.energy -= 5
                pet.cleanliness -= 3
                pet.health -= 1
            start_time = current_time

if __name__ == "__main__":
    main()