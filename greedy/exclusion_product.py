'''
Write a function get_products_of_all_ints_except_at_index()
that takes a list of integers and returns a list of the products

Takeaways:
    1) O(n) solutions require caching (products at left and right of index)
    2) Save space by performing operations in a single array...
        this goes beyond just appending correct solutions to it.
'''

def get_products_of_all_ints_except_at_index_bf(integers):
    products = []
    for i in range(len(integers)):
        product = 1
        for j in range(len(integers)):
            if i != j:
                product *= integers[j]
        products.append(product)
    return products

print('Brute force Happy path input...')
a = [1, 7, 3, 4]
print(get_products_of_all_ints_except_at_index_bf(a))

print('Brute force Zeroes in input...')
a = [1, 7, 0, 3, 4, 0]
print(get_products_of_all_ints_except_at_index_bf(a))

# O(n) time, O(n) space
def get_products_of_all_ints_except_at_index(integers):
    if len(integers) <= 1:
        raise Exception('Need to provide >= 1 integers')
    products = [None] * len(integers)
    before_product = 1
    for i in range(len(integers)):
        products[i] = before_product
        before_product *= integers[i]

    after_product = 1
    i = len(integers) - 1
    while i >= 0:
        products[i] *= after_product
        after_product *= integers[i]
        i -= 1

    return products

print('Linear Happy path input...')
a = [1, 7, 3, 4]
print(get_products_of_all_ints_except_at_index(a))

print('Linear Zeroes in input...')
a = [1, 7, 0, 3, 4, 0]
print(get_products_of_all_ints_except_at_index(a))
