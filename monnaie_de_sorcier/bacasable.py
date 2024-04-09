a = "12344"

b = [*a]

c = set(b)

print(b)

print(c)
print(f"Type de c : {type(c)}")


for item in c:
    print(item)
    print(type(item))
