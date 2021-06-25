dic = {"nombre":"Juan", "apellido":"Perez"}

def opcion1(valor):
    for key in dic:
        if(dic[key] == valor):
            print(key)

def opcion2(valor):
    for key,value in dic.items():
        if(value == valor):
            print(key)