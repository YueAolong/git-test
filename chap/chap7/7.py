s="hello‘world"
print(s)
s="hello\" world"
print(s)
s="hello\nworld"
print(s)
s=r"hello\nworld"
print(s)
s="""
早发白帝城
白帝彩云间
啊啊啊啊啊"""
print(s)
s="早发白帝城 白帝彩云间 啊啊啊啊啊"
print(s)

s=int("80")
print(s)
s=float("80.0")
print(s)
s=int("AB",16)
print(s)
s=str(123)
print(s)
money = 5834.5678

print(money)


i = 32
s = "i * i = " + str(i * i)
print(s)
s = "i * i = {}".format(i * i)
print(s)
s = "{0} * {0} = {1}".format(i, i * i)
print(s)
s = "{p1} * {p2} = {p3}".format(p1 = i, p2 = i, p3 = i * i)
print(s)

# money = 5834.5678
# name = "toney"
# print("{0:s}年龄{1:d}, 工资是{2:f}元".format(name, 20, money))
# print("{0}的工资是{1}".format(name, money))
# s_str = "hello world"
# print(s_str.find("e"))
# print(s_str.find("h",2, 6))

text = "AB CD EF GH"
print(text.replace(" ", "!", 1))
print(text.split(" ", maxsplit=1))
wordstring = """it was the best of times it was the worst of times.
it was the age of wisdom it was the age of foolishness."""
wordstring = wordstring.replace(".", "")
wordlist = wordstring.split()
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
d = dict(zip(wordlist,wordfreq))
print(d)