# **Kwargs - gathers remaining arguments as a dictionary

def fav_color(ram, **Kwargs):
    print(ram)
    print(Kwargs)

    for person, color in Kwargs.items():
        print(f"{person}'s fav color is {color}")

fav_color("red",aman = "white",tod = "green")