"""
list comprehension을 이용해서 list1이 1부터 100 사이의 8의 배수를 가지도록 만들어 보세요.

list1 =


print("list1 : ", list1)
"""

list1 = [i for i in range(1,101) if i%8==0]


print("list1 : ", list1)