print("Vnesi svojo težo v kilogramih:")
mass=int(input())
print(mass)

print("Vnesi svojo višino v centimetrih:")
height=int(input())
print(height)

def calc_BMI(height,mass):
	BMI=mass/((height/100)**2)
	return BMI

print(f"Tvoj BMI je: {calc_BMI(height,mass):.2f}")

print("Press enter to continue.")
input()
