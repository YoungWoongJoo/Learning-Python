"""
튜플도 리스트와 마찬가지로 index로 값을 읽어올 수 있습니다. 현재 코드를 실행하면 0,1,2가 차례로 한 줄 씩 출력되지요. 코드의 3번째 줄 print문을 수정해서 tuple1의 값이 각각 한 줄 씩 출력되도록 만들어 보세요.

tuple1 = (11, 22, 33)
for i in range( len( tuple1) ):
    print( i )
"""

tuple1 = (11, 22, 33)
for i in range( len( tuple1) ):
    print( tuple[i] )