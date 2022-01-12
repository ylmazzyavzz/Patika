def flatten(lst):
    return eval('[' + str(lst).replace('[', '').replace(']', '') + ']')

L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(L))

