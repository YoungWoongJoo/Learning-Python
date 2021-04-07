"""
다음 코드는 list1과 list2가 모두 list클래스의 인스턴스인지를 검사합니다. 코드의 빈칸을 채워넣어 정상 동작하도록 만들어 보세요.

list1 = list(range(10))
list2 = [1, 2, 3]

if isinstance(  , list) and isinstance(  , list):
    print("list1과 list2는 둘 다 list클래스 입니다.")
"""

list1 = list(range(10))
list2 = [1, 2, 3]

if isinstance(list1, list) and isinstance(list2, list):
    print("list1과 list2는 둘 다 list클래스 입니다.")