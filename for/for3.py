"""
range를 이용해서 무지개의 순서와 색을 출력하도록 빈칸을 채워보세요. 단, rainbow에 새로운 값이 추가되더라도 그 값을 모두 출력할 수 있도록 len을 이용해야 합니다.

rainbow=["빨","주","노","초","파","남","보"]
for i in 
 :
    color = rainbow[i]
    print('{}번째 색은 {}'.format(i+1,color))
"""

rainbow=["빨","주","노","초","파","남","보"]
for i in range(len(rainbow)):
  color = rainbow[i]
  print('{}번째 색은 {}'.format(i+1,color))