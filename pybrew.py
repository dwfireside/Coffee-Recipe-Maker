from brew import *

def get_user_input():
    print()
    serving = input("How much coffee (ml) - [default:230]: ").strip() or 230

    try: 
        return int(serving)
    except:
        return None
    

serving_size = get_user_input()
brew = BrewFactory.create_brew(BrewMethod.FRENCH_PRESS, serving_size, BrewStrength.STANDARD)

print(brew)

print("Water temp: 195-205°F (90-96°C)")
print(f"Brew ratio: 1:{brew.brew_ratio}")
print(f"Brew length: 5 minutes")
print("-------------------------------\n")

