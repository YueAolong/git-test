# a = "Hello"
# print(a[0:5])
# print(a[0:3:3])
# print("E"  in a)
#
# [20, 10, 50, 30]
#
#
# list = [20, 30, 50]
# list.append(80)
# print(list)
# t = [15, 28, 20]
# list +=t
# print(list)
# list.insert(3,60)
# print(list)
# list[1] =80
# print(list)
# list.remove(80)
# print(list)
# (21, 32, 43, 45, )
# print(tuple("hello"))
#
# s_id, s_name = (102, "张三")
# print(s_id)
# print(s_name)
#
# print(set("hello"))
#
# s_set = {"张三", "lisi", "wangwu"}
# s_set.add("dongliu")
# print(s_set)
# s_set.remove("dongliu")
# print(s_set)
# s_set.clear()
# print(s_set)

dict1 = {102: "zhangsan", 105:"lisi", 109:"wangwu"}
#print(dict1[102])
dict1[110] = "dongliu"
#print(dict1)
dict1[109] = "zhangsan"
#print(dict1)
dict1.pop(105)
#print(dict1)
print(dict1.items())
print(list(dict1.items()))

print(dict1.keys())
print(dict1.values())