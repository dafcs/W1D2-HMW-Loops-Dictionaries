users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [{
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return a list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary

print(users["Jonathan"]["twitter"]) #1
print(users["Erik"]["home_town"]) #2
print(list(users["Erik"]["lottery_numbers"])) #3
print(users["Avril"]["pets"][0]["name"]) #4
print(min(users["Erik"]["lottery_numbers"])) #5

AvLo = users["Avril"]["lottery_numbers"] #6
EvList = []
for ev in AvLo:
    if ev % 2 == 0:
      EvList.append(ev)
users["Erik"]["lottery_numbers"].append(7) #7
print(users["Erik"]["lottery_numbers"])
print(EvList)

# KeyList = users.keys()

users["Erik"]["home_town"] = "Edinburgh" #8

new_pet = {"name":"Fluffy","species":"dog"}
users["Erik"]["pets"].append(new_pet) #9
print(users["Erik"])

users["Daniel"] = {
   "twitter":"danf",
   "lottery_numbers":[1,2,3,4,5,6],
   "home_town":"Edinburgh",
   "pets":[
    {
      "name":"Pantera",
      "species":"cat",
    }]
}

print(users)