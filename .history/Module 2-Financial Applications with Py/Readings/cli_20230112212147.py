import fire 
import random

def clothes_picker():
    shirts_list = ["solid blue t-shirt", "red striped sweatshirt", "purple and green tie dye t-shirt", "black dress shirt"]

    return random.choice(shirts_list)

if __name__ == '__main__':
    fire.Fire(clothes_picker)
    