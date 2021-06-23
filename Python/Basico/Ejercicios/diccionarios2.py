dic = {"nombre":"Juan", "apellido":"Perez"}

items2 = dic.items()

def opcion1(valor):
    for key in dic:
        if(dic[key] == valor):
            print(key)

def opcion2(valor):
    for key,value in dic.items():
        if(value == valor):
            print(key)

print(items2[0])