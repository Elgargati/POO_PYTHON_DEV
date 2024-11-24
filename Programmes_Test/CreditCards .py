from faker import Faker
f = Faker()
# # for i in range(10):
# #     pro = f.simple_profile()
# #     for key in pro:
# #         print(f"{key} : {pro[key]}")
# #     print("_________________________")

# # print(f"adresse : {f.address()}")
# # print(f"country : {f.country()}")
# # print(f"current_country : {f.current_country()}")
# # print(f"city : {f.city()}")
# # print(f"street_name : {f.street_name()}")
# # print(f"building number : {f.building_number()}")
# # print(f"post code : {f.postcode()}")

# print(f"company name : {f.company()}")
# print(f"company slogen : {f.bs()}")
# print(f"job  : {f.job()}")

# credit cards 
print(f"credit card provider : {f.credit_card_provider()}")
print(f"credit card name : {f.name()}")
print(f"credit card expire : {f.credit_card_expire()}")
print(f"credit card number : {f.credit_card_number()}")
print(f"credit card number visa  : {f.credit_card_number(card_type='visa')}")
print(f"credit card CVC  : {f.credit_card_security_code()}")
