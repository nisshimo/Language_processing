"""
Q 04. 元素記号
"""

def minus_one(n):
    return n - 1
def plus_one(n):
    return n + 1


head_index_list = list(map(minus_one, [1, 5, 6, 7, 8, 9, 15, 16, 19]))

w = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()

values = [w[i][:1] if i in head_index_list else w[i][:2] for i in range(len(w))]

keys = list(map(plus_one, [i for i in range(len(values))]))

res_dic =dict(zip(keys, values))

print(res_dic)
