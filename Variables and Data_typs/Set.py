a = {1, 2, 3}
print(a)

nums = {1, 2, 2, 3}
print(nums)

s = set([4, 5, 6])
print(s)

data = {10, 20, 30}
print(len(data))

items = {"apple", "banana"}
items.add("mango")
print(items)

values = {1, 2, 3}
values.remove(2)
print(values)

nums = {5, 10, 15}
nums.discard(20)
print(nums)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

x = {1, 2, 3}
y = {2, 3, 4}
print(x.intersection(y))

m = {1, 2, 3}
n = {2, 3, 4}
print(m.difference(n))

p = {1, 2, 3}
q = {2, 3, 4}
print(p.symmetric_difference(q))

nums = {10, 20, 30}
print(20 in nums)

letters = {"a", "b", "c"}
print("d" not in letters)

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))


data = {10, 20, 30, 40}
data.add(50)
data.remove(20)
data.discard(100)
print(len(data))
print(30 in data)


x = {1, 2, 3}
y = {1, 2}
print(x.issuperset(y))

s = {1, 2, 3}
s.pop()
print(s)

data = {5, 6, 7}
data.clear()
print(data)



unique = set("python")
print(unique)

