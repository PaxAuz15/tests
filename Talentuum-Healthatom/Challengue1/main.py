import json
from urllib.request import urlopen

LAST_DAY:int = 364
urlOnline:str = "https://hrcdn.net/s3_pub/istreet-assets/kCl8fwL94C5PNGFzbD4jXQ/last_year.json"
urlLocal:str = "/home/paxauz/dev/test/Talentuum-Healthatom/Challengue1/last_year.json"

dictionary_titans:dict = {}

def januaryDont(day:int):
    if day >= 0 and day < 31:
        return 0
    elif day > LAST_DAY and day < (LAST_DAY+31):
        return 0
    else:
        return 1

def decemberDont(day:int):
    if day > (LAST_DAY-31):
        return 0
    else:
        return 1

with urlopen(urlOnline) as file:
    data = json.load(file)

    for register in data:
        dayFirst = register[0]
        dayLast = register[1]
        counter = 0
        validateSum = 0
        while validateSum < dayLast:
            validateSum = dayFirst + counter
            january = januaryDont(validateSum)
            december = decemberDont(validateSum)
            if january == 0 or december == 0:
                counter += 1
                continue
            else: 
                try:
                    dictionary_titans[str(validateSum)] += 1
                    counter += 1
                except Exception as e:
                    dictionary_titans[str(validateSum)] = 1
                    counter += 1



# with open(urlLocal) as file:
#     data = json.load(file)
    

#     for register in data:
#         dayFirst = register[0]
#         dayLast = register[1]
#         counter = 0
#         validateSum = 0
#         while validateSum < dayLast:
#             validateSum = dayFirst + counter
#             january = januaryDont(validateSum)
#             december = decemberDont(validateSum)
#             if january == 0 or december == 0:
#                 counter += 1
#                 continue
#             else: 
#                 try:
#                     dictionary[str(validateSum)] += 1
#                     counter += 1
#                 except Exception as e:
#                     dictionary[str(validateSum)] = 1
#                     counter += 1

    
resultDay = min(dictionary_titans.keys(), key=lambda k: dictionary_titans[k])
# print(resultDay)
print(f"En el día {int(resultDay)+1} se observó la menor cantidad de titanes. Un total de {dictionary_titans[resultDay]}")
