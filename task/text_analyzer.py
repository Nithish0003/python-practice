import text_processing as tp
import re

try:
    while True :
        str1=input("Enter the string: ")
        print(type(str1))
        if re.findall("\d",str1) :
            print("Please Enter a valid string....")
            continue
        # else:
        #     pass
        oper=input("Enter the operation you want to do:\n 1) calculate the number of words in the text \n 2) calculate the number of characters in the text \n 3) reverse the text \n 4) capitalize the text => ")
        if oper=="1":
            result=tp.count_words(str1)
            print(result)
        elif oper=="2":
            result=tp.count_char(str1)
            print(result)
        elif oper=="3":
            result=tp.reverse_char(str1)
            print(result)
        elif oper=="4":
            result=tp.capitalize_words(str1)
            print(result)
        else:
            print("Enter a valid input..")
        cont=input("Do you want to do another operation? YES/NO: ")
        if cont.lower()=="yes" or cont.lower()=="y":
            continue
        else:
            break
except Exception as e:
    print(e)