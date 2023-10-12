favorite_team:str = "Manchester City" 
year = 2020
#accessing a single charactor 
print(favorite_team[0])

#accessing a charactor from the end
print(favorite_team[-1])

#sliceing a string to gitting a part of a string , fist position incloud last position non-incloud
print(favorite_team[0:2])
print(favorite_team[:4])  #without start
print(favorite_team[1:])  #without end
print(favorite_team[:])
print(favorite_team[-3:-1]) 

#skip the number in postion 2 , step size
print(favorite_team[0:6:2]) 

print(favorite_team.lower())
print(favorite_team.upper())
print(favorite_team.count("M"))

#chek if this string start with this letter
print(favorite_team.startswith("M"))
print(favorite_team.lower().startswith("man"))

#string concatination
output = "My favorate team is" + favorite_team + "in the premier " + str(year)

print(output)

#string interplation / formating
output = "My favorate team is {} in the permir".format(favorite_team)

#shorthand for string formating
output = "My favorate team is {favorite_team} in the premier {year}" 
