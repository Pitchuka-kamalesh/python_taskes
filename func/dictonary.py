# a = 0
# print(f"before the increment the value {a}")
# for i in range(0,12):
#     print(f"before the increment the value in loop  {a}")
#     a += 1
#     print(f"after increment the value {a}")
data_1 = {'one':10,"two":{"three":30,"four":{"five":50,"six":{"seven":70}}}}
out = []
# note method 1
while True:

    # for k_key,k_valu in data_1.items():
    #     out.append(k_valu)
    out.extend(i for i in data_1.values())
    if type(out[-1]) == dict:
        data_1 = out.pop()
    else:
        break
 
print(out)

# note method 2
def fun_1(dat):

    out.extend(i for i in dat.values())
    if type(out[-1]) == dict:
        fun_1(out.pop())
    else:
        print(out)

fun_1(data_1)
