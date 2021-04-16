# given data is "1- bla bla.\n2- this is text.\n5- i dont need this text."
# import re
# a = "1 - bla bla.\n2 - this is text.\n5 - i dont need this text."
# d = list(a.split("\n"))
# c = re.split("\n", a)
# for i in re.split("\n", a):
#     print(i)
# print(d)


# def digit(num):
#     count = 0
#     while num > 0:
#         num = num // 10
#         count += 1
#     return count
#
#
# print(digit(num = int(input("Enter the number : "))))

# def count_num(num1,num2):
#     strs = " "
#     if num1<num2:
#         strs = "counting up: "
#         strs += ",".join(map(str, list(range(num1, num2+1))))
#     elif num2 < num1:
#         strs = "counting down: "
#         strs += ",".join(map(str, list(range(num1,num2-1,-1))))
#     elif num1 == num2:
#         strs = f"Counting up, {num1}"
#
#     return strs
#
#
# print(count_num(10,1))
# a = "kamalesh"
# for data in set(a):
#     print(f"{data} --> {a.count(data)}")
# data = list(data for data in set(a))

# list = [10,50,60]
# dts = list[::-1]
# print(dts)
# import array as arr
# import sys
# d = ["kamal"]
# b = arr.array('i',["kamal"])
# print(sys.getsizeof(d))
# print(sys.getsizeof(b))
# # # prin
# data = "kamal"
# print(data)
def capital_indexes(datas):
    output = []
    for i, data in enumerate(datas):
        if data.isupper():
            output.append(i)

    return output
