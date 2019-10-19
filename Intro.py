# def div(a, b):
#     return (a + b) ** 2
#
#
# assert div(3, 6) == 81, 'FAIL'
# print('PASS')
# assert div(2, -6) == 16, 'FAIL'
# print('PASS')
# assert div(0, 7) == 49, 'FAIL'
# print('PASS')


def factorial(n):
    fact_list = 1
    for i in range(1, n+1):
        fact_list *= i
    return fact_list


n = int(input())
result = factorial(n)
print(result)

assert factorial(4) == 24, 'failed'
print('test 1 passed')
assert factorial(0) == 0, 'test 2 failed'
print('test 2 passed')
