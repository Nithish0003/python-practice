import requests

def getFunction(searchTxt):
    url=f"https://api.github.com/search/users?q={searchTxt}"
    data=requests.get(url)
    response=data.json()
    print(data.json())
    print("Total records found: ",response["total_count"])
    for i in response["items"]:
        print("Persons login name is :",i["login"])
        print("Persons Github ID is :",i["url"])
    return data.json()
getFunction("Nithish")