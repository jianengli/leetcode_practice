numbers = [6,3,2,0,2,5,0]   
hashmap={}
hashmap[(2,3)]=4
hashmap[(1,2)]=3

print(list(sorted(hashmap.items(), key=lambda item:item[1])[0][0]))
