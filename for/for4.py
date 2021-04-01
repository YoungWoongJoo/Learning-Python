"""
enumerate를 이용해서 무지개의 순서와 색을 출력하도록 빈칸을 채워보세요.

rainbow=["빨","주","노","초","파","남","보"]
for i,color in 
 :
    print('{}번째 색은 {}'.format(i+1,color))
"""

rainbow=["빨","주","노","초","파","남","보"]
for i,color in enumerate(rainbow):
  print('{}번째 색은 {}'.format(i+1,color))