from functools import reduce 

def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print('L1:',L1)
print('L2:', L2)

def mutiply(x,y):
    return x*y
def prod(L):
    return reduce(mutiply, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功！')
else:
    print('测试失败！')

def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    s = s.split('.') #分切字符串
    def f1(x, y):
        return x * 10 + y
    def f2(x, y):
        return x/10+y
    def char2num(s):
        return digits[s]
    #[::-1]翻转list
    return reduce(f1,map(char2num,s[0]))+reduce(f2,list(map(char2num,s[1]))[::-1])/10

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

