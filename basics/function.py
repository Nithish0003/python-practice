from fun_to_dict import function_to_dict as dict

name="Nithish"
email="nits000333@gmail.com"
ph_no="4779878498"
# def insert_to_db(name,ph,email,gender="Any",address="N/A"):
#     print(name,ph,email,gender,address)

# insert_to_db(name,ph_no,email)

# def function_to_dict(name,ph_no,email):
#     key={
#         "key1":name,
#         "key2":ph_no,
#         "key3":email
#     }
#     return key


def print_function():
    ret1=dict("name1","ph_no1","email1")
    ret2=dict("name2","ph_no2","email2")
    ret3=dict("name3","ph_no3","email3")
    ret4=dict("name4","ph_no4","email4")
    ls=[ret1["key3"],ret2["key2"],ret3["key1"],ret4["key3"]]
    print(ls)
# print_function()