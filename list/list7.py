"""
safe_index함수는 mylist와 value를 매개변수로 받아, mylist에서 value의 인덱스를 return하는 함수입니다. safe_index함수를 완성해 보세요. 단, value가 my_list안에 없으면 None을 리턴해야 합니다.

def safe_index(my_list, value):
    # 함수를 완성하세요
    if 
:
        return 

    else:
        return 



print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))
"""

def safe_index(my_list, value):
    # 함수를 완성하세요
    if : value in my_list
        return my_list.index(value)

    else:
        return None



print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))