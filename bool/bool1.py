"""
다음 코드를 실행해서 어느 경우 if문 안의 코드가 실행되는지 확인해 보세요.

if []:
    print("[]은 True입니다.")

if [1, 2, 3]:
    print("[1,2,3]은/는 True입니다.")

if {}:
    print("{}은 True입니다.")

if {'abc': 1}:
    print("{'abc':1}은 True입니다.")

if 0:
    print("0은/는 True입니다.")

if 1:
    print("1은 True입니다.")
"""

if []: #false
    print("[]은 True입니다.")

if [1, 2, 3]: #true
    print("[1,2,3]은/는 True입니다.")

if {}: #false
    print("{}은 True입니다.")

if {'abc': 1}: #true
    print("{'abc':1}은 True입니다.")

if 0: #false
    print("0은/는 True입니다.")

if 1: #true
    print("1은 True입니다.")