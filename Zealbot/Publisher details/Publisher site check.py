import json
file = open('journal_update_data.json','r')
data1 = json.load(file)
pub = set()
try:
    for i in data1:
        v = i['publisher']
        # print(v)
        pub.add(v.lower())
except KeyError:
   
    pub.add('unknown')

pars = open('publisher.txt','r')
new = []
for g in pars:
    print(g)
    k = g.lower()
    print(k)
    # if k in pub:
    #     print ('already')
    # else:
    #     pass
        # new.append(g)
    
print(new)

# for jj in pub:
#     print(jj)

