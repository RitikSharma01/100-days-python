'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

Example Input
weight = 80
height = 1.75
Example Output
80 รท (1.75 x 1.75) = 26.122448979591837
26
'''


# ๐จ Don't change the code below ๐
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# ๐จ Don't change the code above ๐

# Write your code below this line ๐
h = float(height)

bmi = float(weight)/(h*h)
print(int(bmi))
