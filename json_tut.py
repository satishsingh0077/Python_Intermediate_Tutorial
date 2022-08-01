#JSON: java script object notataion. Used for data exchange
# JSON encodings
#    Python             JSON
#   dict                object
#   list, tuple         array
#   atr                 string
#   int, long, float    number
#   True, False         true, false
#   None                null

# converitng pythonn dictionary to json is called serialization or encoding


from asyncore import read
import json
my_dict = {"name":"Satish","city":"magdeburg","is_student":True,"age":28,"work":["kpit","bosch","luxoft"]}
my_dict1 = {"name":"kumar","city":"magdeburg","is_student":True,"age":28,"work":["zequenses","gi","tempton"]}

#make a json string document
my_json = json.dumps(my_dict)
print(my_json)
# format the json
my_json1 = json.dumps(my_dict, indent = 4,separators=('; ', '= '), sort_keys=True)# indent make in format properly. seperators replaces default seperators i.e : and ,  Sort_keys arranges them in alphabetical order
print(my_json1)

# write to a file
with open('mydata.json','w') as file:
    json.dump(my_dict, file, indent = 4)

with open('mydata.json','a') as file:
    json.dump(my_dict1, file, indent = 4)

# converting data from json object to pyhton dictionary is called deserialization or decoding
person = json.loads(my_json)
print(person)

print("**************************************************************************************************************************")
# reading from a file
with open('mydata.json','r') as file:
    back_data = json.load(file)
    print(back_data)
