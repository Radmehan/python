# for i in range(87):
#     print(i)

def gen(n):
    for i in range(n):
        yield i
        # return i


# g=gen(354545454545454545454)
# print(g)

g=gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

h="Harry"
# h=2342552
# for i in h:
#     print(i)
c=iter(h)
print(c.__next__())
print(c.__next__())

