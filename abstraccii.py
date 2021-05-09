#list абстракции:
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

#абстракции списков заменяют создание нового простого списка при помощи цикла for и append:
squared = [x**2 for x in range(10)]
print(squared)

#dict абстракции:
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase_frequency)

#set абстракции:
squared = {x**2 for x in [1, 1, 2]}
print(squared)


# Абстракции генераторов:
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)


for x in multiples_gen:
    print(x)
    