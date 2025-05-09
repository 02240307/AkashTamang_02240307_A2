import random

class GuessingNumbers:
    def __init__(self):
        self.target = random.randint(1, 20)
        self.total_guesses = 0

x = GuessingNumbers()

def game1():
    print("Guess a number between 1 and 20!")
    while True:
        guess = input("Your guess: ")
        x.total_guesses += 1
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 20:
                if guess < x.target:
                    print("Guess is too low. Guess higher!")
                elif guess > x.target:
                    print("Guess is too high. Guess lower!")
                else:
                    print("Congratulations! Your guess is correct.")
                    break
            else:
                print("Please enter a number between 1 and 20.")
        else:
            print("Invalid input. Please enter a  number between 1 and 20.")
    score = 20 - x.total_guesses
    print("You have scored", score, 'out of 20')
    return score

class rockpaperscissors:
    def __init__(self):
        self.options = ('rock','paper','scissors')
        self.user_score = 0
        self.computer_score = 0

y = rockpaperscissors()

def game2():
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit') ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in y.options:
            print('Invalid option. Choose a valid option')
            continue
        computer_choice = random.choice(y.options)
        print("Computer chose:", computer_choice)
        if user_choice == computer_choice:
            print('draw')
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            y.user_score += 1
            print("You win")
        else:
            y.computer_score += 1
            print("You lose")
    print("Final Scores - You:", y.user_score, '||| Computer:', y.computer_score)
    return y.user_score

def game3():
    questions = (
        'What is the basic unit of life?',
        'Which gas do plants absorb from the air to make food?',
        'What is the hardest natural substance on Earth?',
        'What is the plural of "child"?',
        'What part of speech describes a noun?',
        'Which word is spelled correctly?',
        'Who was the first President of the United States?',
        'Which ancient civilization built the Great Wall?',
        'Who was the first to land on moon?',
        'How many colours are there in visible light'
    )
    options = (
        ('a) Atom', 'b) Cell', 'c) Molecule', 'd) Tissue'),
        ('a) Oxygen', 'b) Carbon dioxide', 'c) Nitrogen', 'd) Hydrogen'),
        ('a) Gold', 'b) Iron', 'c) Diamond', 'd) Quartz'),
        ('a) Childs', 'b) Childes', 'c) Children', 'd) Child’s'),
        ('a) Verb', 'b) Adjective', 'c) Noun', 'd) Adverb'),
        ('a) Recieve', 'b) Believe', 'c) Decieve', 'd) Recieve'),
        ('a) Thomas Jefferson', 'b) Abraham Lincoln', 'c) George Washington', 'd) John Adams'),
        ('a) Rome', 'b) Greece', 'c) China', 'd) Egypt'),
        ('a) Buzz Aldrin', 'b) Yuri Gagarin', 'c) Neil Armstrong', 'd) Michael Collins'),
        ('a) 7', 'b) 5', 'c) 10', 'd) 15')
    )
    answers = ('b', 'b', 'c', 'c', 'b', 'b', 'c', 'c', 'c','a')
    score = 0
    Q_no = 0
    for question in questions:
        print(question)
        for option in options[Q_no]:
            print(option)
        guess = input("Enter (a, b, c, d): ").lower()
        if guess == answers[Q_no]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print('The correct answer is', answers[Q_no])
        Q_no += 1
    print(f"Your score is: {score} out of {len(questions)}")
    return score

def play():#function to store and call all the games
    overall_score = 0
    while True:
        print("Select a game(1-6):")
        print("1. Guess Number game")
        print("2. Rock paper scissors game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check your Current Overall score")
        print("6. Stop playing game")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":                                         #Calling all the games according to user choice
            overall_score += game1()
        elif choice == "2":
            overall_score += game2()
        elif choice == "3":
            overall_score += game3()
        elif choice == "4":
            from AkashTamang_02240307_A2_PB import BinderManager   # Importing pokemon binder manager from A2 part B
            game4 = BinderManager()
            game4.run()
        elif choice == "5":
            print("Your overall score till now is:", overall_score)
        elif choice == "6":
            print("Thank you for your time!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

play()  #Calling the game function to work