import random
rock = '''
    _______
---'   ____)    
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

class RPSGame:
    def __init__(self):
        self.player_lives = 3
        self.computer_lives = 3
        self.game_images = [rock,paper,scissors]

    def choice_user(self):
        while True: 
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            while user_choice not in [0,1,2]:
                user_choice = int(input("pls give me the number again"))
            return user_choice

    def choice_computer(self):
        computer_choice = random.randint(0,2)
        return computer_choice

    def whos_the_winner(self,user_choice,computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == 0 and computer_choice == 2)
            or (user_choice == 1 and computer_choice == 0)
            or (user_choice == 2 and computer_choice == 1 )
        ):
            return "You win!"
    
        else:
            return "Computer wins! \n"
    
    def main(self):
        while self.player_lives > 0 and self.computer_lives > 0 :
            user_choice =  self.choice_user()
            computer_choice = self.choice_computer()
            print(f"user choice {self.game_images[user_choice]}")
            print(f"computer choice {self.game_images[computer_choice]}")

            result = self.whos_the_winner(user_choice,computer_choice)
            print(result)
    

            if result == "You win!":
                self.computer_lives = self.computer_lives - 1
                print(f"the lives of the computer are {self.computer_lives} ---- and for you are {self.player_lives}")

            if result == "Computer wins!":
                self.player_lives = self.player_lives - 1
                print(f"the lives of the computer are {self.computer_lives} and for you are {self.player_lives}")
    
            if self.player_lives == 0 or self.computer_lives == 0:
                break
       
        if self.player_lives  == 0:
            print("Game over! computer wins")
        else:
            print("Game over! player wins")


if __name__ == "__main__":
    game = RPSGame()
    game.main()
