def main():
    COLOR_NAMES = {"AliceBlue": "#f0f8ff",
                   "AntiqueWhite": "#faebd7",
                   "AquaMarine": "#8b8378",
                   "Beige": "#f5f5dc",
                   "Black": "#000000"}

    display_palette(COLOR_NAMES)
    user_input = input("Choose a color: ")
    while user_input != "":
        if user_input in COLOR_NAMES:
            print("The color code for {} is: {}".format(user_input, get_color_code(COLOR_NAMES, user_input)))
        else:
            print("Invalid color name. Look at the palette!")
        user_input = input("Choose a color: ")

def display_palette(COLOR_NAMES):
    for color in COLOR_NAMES:
        print(color)

def get_color_code(COLOR_NAMES, user_input):
    return COLOR_NAMES[user_input]

main()
