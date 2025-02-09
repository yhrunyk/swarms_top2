import random

def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself at a crossroads. Do you go left or right?")
    choice1 = input("Type 'left' or 'right': ").lower()
    
    if choice1 == "left":
        print("You walk into a dark forest and hear a noise. Do you investigate or run away?")
        choice2 = input("Type 'investigate' or 'run': ").lower()
        
        if choice2 == "investigate":
            print("You find a hidden treasure! But there's a guard. Do you fight or sneak away?")
            choice3 = input("Type 'fight' or 'sneak': ").lower()
            
            if choice3 == "fight":
                if random.randint(1, 2) == 1:
                    print("You defeated the guard and take the treasure! You win!")
                else:
                    print("The guard defeats you. Game over!")
            elif choice3 == "sneak":
                print("You successfully sneak away with some gold. You win!")
            else:
                print("Invalid choice. The game ends.")
        elif choice2 == "run":
            print("You trip and fall. A wild animal catches you. Game over!")
        else:
            print("Invalid choice. The game ends.")
    
    elif choice1 == "right":
        print("You reach a river. Do you swim across or look for a bridge?")
        choice2 = input("Type 'swim' or 'bridge': ").lower()
        
        if choice2 == "swim":
            print("You get swept away by the current. Game over!")
        elif choice2 == "bridge":
            print("You safely cross the river and find a village. Do you explore or rest?")
            choice3 = input("Type 'explore' or 'rest': ").lower()
            
            if choice3 == "explore":
                print("You discover an ancient temple filled with gold! You win!")
            elif choice3 == "rest":
                print("You wake up to find the village abandoned. You decide to keep moving. You win!")
            else:
                print("Invalid choice. The game ends.")
        else:
            print("Invalid choice. The game ends.")
    
    else:
        print("Invalid choice. The game ends.")

if __name__ == "__main__":
    adventure_game()
