f = open("db.sql", "r", encoding="utf-8")

# data = f.readlines()[147827:579225:]

# idxs = []
# dictionary = []

# korean = []

# for i in data:
#     word = ""
#     for j in i:
#         if j == "\t":
#             korean.append(word)
#             break
#         word += j

# for i in korean:
#     if "이세계에서펜션을시작했습니다세계유일의흑마녀입니다만이힘은고객님을위해쓰겠습니다" == i:
#         print(True)

# data = f.readlines()[311:]

# idxs = []
# dictionary = []

# korean = []

# for i in data:
#     if 48 <= ord(i[0]) and ord(i[0]) <= 57:
#         for j in range(0,len(i)):
#             if i[j] == "\t" or i[j] == ",":
#                 word = ""

#                 for k in range(j + 1, len(i)):
#                     if i[k] == ",":
#                         break
#                     if i[k] == "|" or i[k] == "\t" or i[k] == "\n":
#                         korean.append(word)
#                         break
#                     word += i[k]

data = f.readlines()[794:147811:]

english = []

for i in data:
    word = ""
    for j in i:
        if j == "\t":
            english.append(word)
            break
        word += j

a = 0
for i in english:
    if i == "zoisia":
        a += 1

print(a)