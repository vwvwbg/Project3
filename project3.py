import os
import linecache  


def LFU():
    
    print('replace By LFU')
    for i in line:
        if i != ' ':
            print(i)
            if cache.__contains__(i):               #if hit counter++
                cache[i] = cache[i] + 1
            elif  int(cache_size)>len(cache):           #if not full 
                cache[i] = 1
            else:
                del cache[min(cache, key=cache.get)]        #if need to replace select the one which is smallest 
                cache[i] = 1
            print(cache)
    cache.clear()



def LRU():
    print('replace by LRU')
    for i in line:
        if i != ' ':
            print(i)
            if cache.__contains__(i):           #if hit set this page to 1 another ++ 
                for k in cache:
                    if k == i:
                        cache[i] = 1
                        pass
                    else:
                        cache[k] = cache[k] + 1 
            elif  int(cache_size)>len(cache):   #if not full 
                for k in cache:
                    cache[k] = cache[k] + 1 
                cache[i] = 1
            else:
                del cache[max(cache, key=cache.get)]    #if need to replace select the one which is biggest 
                cache[i] = 0
                for k in cache:
                    if k == i:
                        pass
                    else:
                        cache[k] = cache[k] + 1 
            print(cache)
    cache.clear()

script_dir = os.path.dirname(__file__) 
print('Your input filie name:')
file_name = input()
rel_path = file_name                               
abs_file_path = os.path.join(script_dir, rel_path)      #trans local file path to system path
line  =  open(abs_file_path).readline()
cache = {}
print('Cache size = ')
cache_size = input()


while 1:
    print('Select which algorithm you want to use.\n1 = LFU\n2 = LRU')
    select = input()
    select = int(select)    
    if select == 1:
        LFU()
    elif select == 2:
        LRU()
    else:
        pass


