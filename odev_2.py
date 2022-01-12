lst = [[1, 2], [3, 4], [5, 6, 7]]

def Ters(lst): 
    lst.reverse()
    print(lst[0][::-1],lst[1][::-1],lst[2][::-1])
    return lst


Ters(lst)

      