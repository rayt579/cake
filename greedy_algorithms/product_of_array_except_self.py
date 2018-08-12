'''
Write a function get_products_of_all_ints_except_at_index()
that takes a list of integers and returns a list of the products

Takeaways:
    1) O(n) solutions require caching (products at left and right of index)
    2) Save space by performing operations in a single array...
        this goes beyond just appending correct solutions to it.

BONUS:
1) What if you could use division? Careful—watch out for zeroes!
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

# Solution
  def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    # We make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in xrange(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in xrange(len(int_list) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

    return products_of_all_ints_except_at_index