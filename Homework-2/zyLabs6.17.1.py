"""Joseph Nguyen PSID: 1779987"""
# zyLabs 6.17.1 #

user_input = input()

user_input = user_input.replace('i', '!')
user_input = user_input.replace('a', '@')
user_input = user_input.replace('m', 'M')
user_input = user_input.replace('B', '8')
user_input = user_input.replace('o', '.')
user_input = user_input + "q*s"

print(user_input)
