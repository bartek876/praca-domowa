def edit(lst:list,id:int,key:str,val):
    for elem in lst:
        if elem ["id"] == id:
            elem[key] = val