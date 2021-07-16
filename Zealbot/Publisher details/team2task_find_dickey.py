import json

file = open('/home/mahendrann/Downloads/marlin/small_number/complementarity.txt','r')
data1 = json.load(file) 

print(type(data1))

print(data1.keys())    
# print(data1.values())
# print(data1['hits'])

print(data1['hits'][0])
