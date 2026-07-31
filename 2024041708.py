c=int(input("enter the cache capacity)
cache=[]
dit={}
def put(key,value):
    if(len(cache)>c):
         dit.delete(cache[0])
         cache.pop(0)
         cache.append(key)
         dit[key]=value
def get(key):
     if key not in dit:
           return -1
     else:
         return dit[key]
     
         
         
    