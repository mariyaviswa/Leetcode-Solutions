password = input()
all_conditions = []
for i in range(0, len(password)):
    if password[i].isupper():
        if "upper" not in all_conditions:
            all_conditions.append("upper")
    elif password[i].islower():
        if "lower" not in all_conditions:
            all_conditions.append("lower")
    elif password[i].isdigit():
        if "digit" not in all_conditions:
            all_conditions.append("digit")
    else:
        if "special" not in all_conditions:
            all_conditions.append("special")
print(all_conditions)
if len(all_conditions) == 4:
    print("Valid")
else:
    print("Invalid")