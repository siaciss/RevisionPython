# Révisions python
# Avec python 2.7

age = input("Quel est votr age ? ")
is_adult = age >= 18
age_int = int(age)
#rep = "Vous avez "+ str(age_int) + " ans."
#rep = f"Vous avez {age_int} ans."   #Version 3.6 et sup
rep = "vous avez {} ans.".format(age_int)
rep = "vous avez %d ans." % age_int
rep2 = "Vous etes majeur." if is_adult else "Vous etes mineur."
print(rep + " " + rep2)
#print(f"{rep} {rep2}")