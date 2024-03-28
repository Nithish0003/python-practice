import json
import requests

# data1=requests.get("https://api.github.com")
payload1={
  "message": "Not Found",
  "documentation_url": "https://docs.github.com/rest/issues/issues#list-issues-assigned-to-the-authenticated-user"
}
string_payload1=json.dumps(payload1)
print(string_payload1)
data1=requests.get("https://api.github.com/issues")
print(data1)

# payload={
#     "tittle":"BMW Pencil"
# }
# string_payload=json.dumps(payload)
# print(string_payload)
# data=requests.post("https://dummyjson.com/products/add",string_payload)
# print(data.text)

# jason_data=data.json()
# print(jason_data['issues_url'])
# print(jason_data['user_url'])
# for i in jason_data:
#     print(f'{i} : {jason_data[i]}')




# country = {
#     "id" : 1,
#     "country_name" : "India",
#     "code" : "+91",
#     "State" : ["Kerala", "Tamil nadu", "karnataka", "Andhra Pradesh", "Delhi"],
#      "City" : [{
#          "id": 1,
#          "name" : "chennai"
#      },
#      {
#          "id": 2,
#          "name": "Trivandrum"
#      },
#      {
#          "id": 3,
#          "name" : "Bangalore"
#      },{
#          "id": 4,
#          "name" : "Chittod"
#      },{
#          "id": 5,
#          "name" : "Delhi"
#      }]
     
# }

# # convert dict ---> json
# dumper=json.dumps(country)
# # convert json ---> str
# print(json.loads(dumper))
