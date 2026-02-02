class Oreo:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            self.happiness += 1
            return f"You fed {self.name}. Hunger is now {self.hunger}."
        else:
            return f"{self.name} is not hungry."

    def play(self):
        if self.energy > 0:
            self.happiness += 2
            self.energy -= 1
            self.hunger += 1
            return f"You played with {self.name}. Happiness is now {self.happiness}."
        else:
            return f"{self.name} is too tired to play."

    def sleep(self):
        self.energy = 5
        self.hunger += 2
        return f"{self.name} slept and restored energy to {self.energy}."

    def status(self):
        return (f"{self.name}'s status:\n"
                f"Hunger: {self.hunger}\n"
                f"Energy: {self.energy}\n"
                f"Happiness: {self.happiness}")

    def is_alive(self):
        if self.hunger >= 10:
            return False, f"{self.name} has starved."
        if self.happiness <= 0:
            return False, f"{self.name} is too sad and ran away."
        return True, ""

def main():
    oreo = Oreo("Oreo")
    print(f"Welcome to the virtual pet game! You have a pet named {oreo.name}.")

    while True:
        print("\nWhat would you like to do? (feed/play/sleep/status/quit)")
        action = input("> ").strip().lower()

        if action == "feed":
            print(oreo.feed())
        elif action == "play":
            print(oreo.play())
        elif action == "sleep":
            print(oreo.sleep())
        elif action == "status":
            print(oreo.status())
        elif action == "quit":
            print(f"Goodbye! Thanks for taking care of {oreo.name}.")
            break
        else:
            print("Invalid action. Please choose feed, play, sleep, status, or quit.")

        alive, message = oreo.is_alive()
        if not alive:
            print(message)
            print(f"{oreo.name} has passed away. Game over.")
            break

if __name__ == "__main__":
    main()
