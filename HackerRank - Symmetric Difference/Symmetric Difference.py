def symetric_difference(num1,num2):
    num1 = set(list(map(int, num1)))
    num2 = set(list(map(int, num2)))
    num = sorted(num1.symmetric_difference(num2), key=int, reverse=True)
    for i in num[::-1]:
        print(i)

nums1 = input()
nums2 = input().split()
nums3 = input()
nums4 = input().split()
symetric_difference(nums2,nums4)