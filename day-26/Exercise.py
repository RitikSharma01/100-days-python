# number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# //////////////////////
# Squared Numbers
# squared_numbebrs = [num*num for num in number]
# print(squared_numbebrs)

# //////////////////////
# # even number
# even_number = [even for even in number if even % 2 == 0]
# print(even_number)
# //////////////////////

# exercise4
# sentence = 'What is the Airspeed velocity of an Unnladen Swallow?'
# # list = [value for value in sentence.split(' ')]
# dict = {key: len(key) for key in sentence.split(' ')}
# print(dict)

# exercise 5
weather = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thrusday': 14,
    'Friday': 21,
    'Saturday': 22,
    'sunday': 24,
}
weather_f = {key: (value*9/5)+32 for (key, value) in weather.items()}
print(weather_f)
