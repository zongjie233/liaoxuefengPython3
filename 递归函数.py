#汉诺塔图解递归算法

def move(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        move(n-1,a, c, b)#将A柱子上的n-1个盘子放到B柱子上
        # print("这是a,c,b排列的abc值：",a,b,c)
        print(a, '--->', c)
        move(n - 1, b, a, c)#将B柱子上的n-1个放到C柱子上
        # print("这是b,a,c排列的abc值",a,b,c)
move(3, 'A', 'B', 'C')  