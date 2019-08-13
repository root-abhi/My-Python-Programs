user_weight = input('What is your weight in punds? ')
weight_in_kg = 2.5 * float(user_weight) ## I have used float here becuase user can input weight in decimel also where int will be failed to run.
print(weight_in_kg)


## Another example for same exercise

weight_lbs = input('What is your weight, Please enter in LBS: ')
weight_calc = int(weight_lbs) * 0.45
print(weight_calc)