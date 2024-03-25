shopping_cart={
    "mobile_phone" : "1",
    "ear_phone" : "3",
    "case_cover" : "1",
    "accessories" : "6"
}

price={
    "mobile_phone" : "19000",
    "ear_phone" : "3500",
    "case_cover" : "350",
    "accessories" : "220"
}

total=0
for i in shopping_cart:
    for j in price:
        total+=int(shopping_cart[i])*int(price[j])
print(total)