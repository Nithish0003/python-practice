country = {
    "id" : 1,
    "country_name" : "India",
    "code" : "+91",
    "State" : ["Kerala", "Tamil nadu", "karnataka", "Andhra Pradesh", "Delhi"],
     "City" : [{
         "id": 1,
         "name" : "chennai"
     },
     {
         "id": 2,
         "name": "Trivandrum"
     },
     {
         "id": 3,
         "name" : "Bangalore"
     },{
         "id": 4,
         "name" : "Chittod"
     },{
         "id": 5,
         "name" : "Delhi"
     }]
     
}

name="Nithish"
number=6382544302
city=country["City"][0]["name"]
state=country["State"][1]
country_name=country["country_name"]
code=country["code"]


print("My name is",name,"and I'm from",country["City"][0]["name"],",",country["State"][1],",",country["country_name"],"and my mobile number is",country["code"],number)
print("My name is"+" "+name+" and I'm from "+country["City"][0]["name"].capitalize()+", "+country["State"][1]+", "+country["country_name"]+" and my mobile number is "+country["code"]+" "+str(number))
print(f"My name is {name} and I'm from {city}, {state}, {country_name} and my mobile number is {code} {number}")