import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the data

# try:
#     # newlist = [x for x in data if x['Delegator']['delegator_public_key'] == "0203a5c03d9f7d6885276d0faa25d412ecc1369f6573856c321d99cafc0dac2a8c12"]
#     for x in data(1,10):
#         print(x)
#     # print(newlist)
# except Exception as err:
#     print(err)

newlist = []
amount = 0
newamount = []
for x in data:
    try:
        # print(x['Delegator']['delegator_public_key'])
        if x['Delegator']['delegator_public_key'] == '0203a5c03d9f7d6885276d0faa25d412ecc1369f6573856c321d99cafc0dac2a8c12':
            # print(x)
            newlist = newlist + [x['Delegator']]
            amount = amount+int(x['Delegator']['amount'])
            newamount = newamount + [int(x['Delegator']['amount'])]
        # new_list = [expression for item in list if condition]
    except Exception as err:
        # print(err)
        pass

print(newlist, len(newlist))
print("amount:", amount)
print("newamount", newamount)
