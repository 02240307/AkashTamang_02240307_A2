MAX_POKEDEX = 1025
CARDS_PER_PAGE = 9  # 9 cards per page, 3x3

class PokemonCard:
    def __init__(self, pokedex_number):
        self.pokedex_number = pokedex_number
        # Figure out where to put this card
        self.page, self.slot = self.position()

    def position(self):
        number = self.pokedex_number - 1
        page = number // CARDS_PER_PAGE + 1 
        slot = number % CARDS_PER_PAGE + 1   
        return page, slot

class Binder:
    def __init__(self, max_pokedex=MAX_POKEDEX):
        self.max_pokedex = max_pokedex
        self.cards = {}  #  to keep track of cards

    def add_card(self, pokedex_number):
        # Check if we already have this card
        if pokedex_number in self.cards:
            card = self.cards[pokedex_number]
            return False, card.page, card.slot  # Already have it
        # Otherwise, make a new card and add it
        card = PokemonCard(pokedex_number)
        self.cards[pokedex_number] = card
        return True, card.page, card.slot

    def reset(self):
        # Clear all cards from the binder
        self.cards.clear()

    def get_status(self):
        count = len(self.cards)
        percent = (count / self.max_pokedex) * 100
        return count, self.max_pokedex, percent

    def has_card(self, pokedex_number):
        return pokedex_number in self.cards

class BinderManager:
    def __init__(self):
        self.binder = Binder()

    def run(self):
        while True:
            self.print_menu()
            choice = input("Pick an option (1-4): ").strip()
            if choice == "1":
                self.add_card()
            elif choice == "2":
                self.reset_binder()
            elif choice == "3":
                self.show_status()
            elif choice == "4":
                print("Thanks for using the Pokémon Card Binder Manager. Bye!")
                break
            else:
                print("Oops, not a valid option. Try again.")

    def print_menu(self):
        print("\n--- Pokémon Card Binder Manager ---")
        print("1. Add a Pokémon card")
        print("2. Clear all cards (reset)")
        print("3. Show how many cards you have")
        print("4. Quit")

    def add_card(self):
        try:
            num = int(input(f"Enter a Pokédex number (1-{MAX_POKEDEX}): ").strip())
            if not (1 <= num <= MAX_POKEDEX):
                print(f"Number must be between 1 and {MAX_POKEDEX}.")
                return
            added, page, slot = self.binder.add_card(num)
            if added:
                print(f"Added Pokédex {num} at Page {page}, Slot {slot}.")
            else:
                print(f"Already have Pokédex {num} on Page {page}, Slot {slot}.")
        except ValueError:
            print("Please enter a valid number.")

    def reset_binder(self):
        print("Are you sure? This will delete ALL cards!")
        confirm = input("Type 'CONFIRM' to delete, or anything else to cancel: ").strip().upper()
        if confirm == "CONFIRM":
            self.binder.reset()
            print("Binder cleared. All cards gone.")
        else:
            print("Reset cancelled.")

    def show_status(self):
        count, total, percent = self.binder.get_status()
        print(f"You have {count} cards.")
        print(f"There are {total} possible cards.")
        print(f"That's {percent:.2f}% complete.")

if __name__ == "__main__":
    game4 = BinderManager()
    game4.run()