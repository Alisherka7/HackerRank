nums = input().split()
a = int(nums[0])
b = int(nums[1])
d = '-'
m = 1
f = a - 2
for i in range(a//2):
    c = '.|.' * m
    print(c.center(b,d))
    m += 2
print('WELCOME'.center(b, d))
for i in range(a//2):
    c = '.|.' * f
    print(c.center(b,d))
    f-=2

print()

# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))