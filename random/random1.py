"""
https://docs.python.org/3.5/library/random.html#random.choice 에서 random.choice의 활용법을 확인하고, 3번째 줄에 코드를 추가해서 random_element가 list의 element중 하나를 가지도록 만들어 보세요.

import random
list = ["빨","주","노","초","파","남","보"]
random_element = 


print(random_element)
"""

import random
list = ["빨","주","노","초","파","남","보"]
random_element = random.choice(list)


print(random_element)