print("Insert M for male and F for female:")
sex = input().upper()
if sex not in ["M", "F"]:
    print("You can insert only M for male or F for female.")
    exit()
print(sex)

print("Insert your age in years:")
age = int(input())
print(age)

print("Insert your height in cm")
height = int(input())
print(height)

print("Insert your body mass in kg:")
mass = int(input())
print(mass)


def calc_BMR(age, mass, height, sex):
    sex_constant = 5 if sex == "M" else -161
    BMR = ((10*mass)+(6.25*height)-(5*-age)+sex_constant)
    return (BMR)


print(f"Your BMR is: {calc_BMR(age, mass, height, sex)}")

print("Press enter to continue.")
input()

# kar je za # je komentar
