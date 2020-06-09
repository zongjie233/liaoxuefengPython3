#python内置的enumerate函数 
# for i, value in enumerate("abc"):
#     print(i,value)

#ex

def findMaxandMin(l):
    if len(l) == 0:
        print("请输入一个列表")
    else:
        min = max = None
        min = max = l[0]
        for i in l:
            if i > max :
                max = i
            if i < min:
                min = i
    t1 = (min,max)
    return t1            


l1 = [1,2,3]
print(findMaxandMin(l1))
            
