lbs = 350
kg =  lbs/2.205
kg = round(kg,2)
lbs = str(lbs)
kg = str(kg)
print("Weight in Pounds (lbs) = " + lbs)
print("Weight converted to Kilogram (kg) = " + kg)

print("==================================")

mi = 21
km = mi*1.609
km = round(km,2)
mi = str(mi)
km = str(km)
print("Length in Miles (mi) " + mi)
print("Length in Kilometer (km) " + km)

print("==================================")

Fahrenheit = 10000
Celsius = (5/9)*(Fahrenheit - 32)
Fahrenheit = str(Fahrenheit)
Celsius = round(Celsius)
Celsius = str(Celsius)
print("Temperature to Fahrenheit (°F)" + Fahrenheit)
print("Temperature to Celsius (°C)" + Celsius)

print("==================================")

Student1 = 25
Student2 = 27
Student3 = 24
Student4 = 25
Student5 = 23
Student6 = 28
Student7 = 26
Student8 = 28
Student9 = 24
Student10 = 23

total_age = Student1 + Student2 + Student3 + Student4 + Student5 + Student6 + Student7 + Student8 + Student9 + Student10 
Average = int(total_age/10)

print("Age of Student 1: " , Student1)
print("Age of Student 2: " , Student2)
print("Age of Student 3: " , Student3)
print("Age of Student 4: " , Student4)
print("Age of Student 5: " , Student5)
print("Age of Student 6: " , Student6)
print("Age of Student 7: " , Student7)
print("Age of Student 8: " , Student8)
print("Age of Student 9: " , Student9)
print("Age of Student 10: ", Student10)
print(f"The average age of the students is: {Average}")

print("==================================")

names = ["Rimuru", "Zoro", "Julius", "Tryndamere", "Enel", "Luna"]
ability = ["Eagle's eye", "Thunderstrike", "Arcane Scepter", "Oathbreaker", "Skytriders"]
item =  "Enchanted Amulet"
place = "Eldoria"



print("The group of explorers came together as a result of a vision that predicted the coming of " + names[0] + ", an evil sorcerer who sought to utilize the " + item + " to submerge " + place + " in an unending period of darkness."    
""" They traveled through dangerous jungles, across precarious heights, and into the darkest dungeons. They ran into many obstacles and supernatural creatures along the route. They were aided in navigating difficult terrain by """ + names[1] +"'s " + ability[0] + ", " + names[4] + "'s " + ability[1] + ", " + names[2] + "'s " + ability[2] + ", " + names[3] + "'s " + ability[3] + ", and " + names[5] + "'s " + ability[4] + "."
"When they eventually arrived at " + names[0] + """'s lair, a furious struggle broke out. They overcame the evil sorcerer's defenses because to their combined power and special skills. """ + ability[0] + " of " + names[1] + "."
+ " pierced " + names[0] + "'s magical barriers, " + names[4] + "'s " + ability[1] + " shattered his illusions, " + names[0] + "'s " + ability[2] + " weakened his powers, " + names[3] + "'s " + ability[3] + " broke his cursed armor, and " + names[5] + "'s " + ability[4] + " provided the mobility to outmaneuver him."
"In the end, it was " + names[4] + " who delivered the final blow with " + ability[1] +", shattering the " + item + " and defeating " + names[0] + ". The realm of " + place + " was saved from eternal darkness, thanks to the combined effort of " + names[1] + ", " + names[4] + ", " + names[2] + ", " + names[3] + ", and " + names[5] + ".")