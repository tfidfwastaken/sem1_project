import json
"""
print("Adding the subject and hours per week\n\n")
my_dict1 = dict()
user_input = input("Enter subject and hours per week separated by commas (,): ")
key, value = user_input.split(",")
my_dict1[key] = int(value)

while True:
    flag=input("Do you want to add more(Y/N): ")
    if flag=='N' or flag=='n':
        break
    user_input = input("Enter subject and hours per week separated by commas (,): ")
    key, value = user_input.split(",")
    my_dict1[key] = int(value)

print(my_dict1)

json = json.dumps(my_dict1)
f = open("dict_subperweek.json","w")
f.write(json)
f.close()
"""
print("Adding the hours per day\n\n")
l=["Monday","Tuesday","Wednesday","Thursday","Friday"]

my_dict2=dict.fromkeys(l)

for key in my_dict2.keys():
    user_input=int(input(f"Specify Number of days in {key}: "))
    my_dict2[key] = user_input

print(my_dict2)

json = json.dumps(my_dict2)
f = open("dict_hoursperday.json","w")
f.write(json)
f.close()
