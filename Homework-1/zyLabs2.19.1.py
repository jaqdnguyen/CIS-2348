"""Joseph Nguyen PSID: 1779987"""
# zyLabs 2.19.1 #
# servings = (cups_lemon + cups_water + cups_agave)/3.416 #

cups_lemon = float(input("Enter amount of lemon juice (in cups):\n"))
cups_water = float(input("Enter amount of water (in cups):\n"))
cups_agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(cups_lemon), "cup(s) lemon juice")
print('{:.2f}'.format(cups_water), "cup(s) water")
print('{:.2f}'.format(cups_agave), "cup(s) agave nectar\n")

desired_servings = float(input("How many servings would you like to make?\n"))
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings), "servings")
print('{:.2f}'.format(desired_servings/3), "cup(s) lemon juice")
print('{:.2f}'.format(desired_servings*2.666666666666667), "cup(s) water")
print('{:.2f}'.format(desired_servings*0.4166666666666667), "cup(s) agave nectar\n")

print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings), "servings")
print('{:.2f}'.format((desired_servings/3)/16), "gallon(s) lemon juice")
print('{:.2f}'.format((desired_servings*2.666666666666667)/16), "gallon(s) water")
print('{:.2f}'.format((desired_servings*0.4166666666666667)/16), "gallon(s) agave nectar")
