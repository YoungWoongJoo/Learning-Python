"""
days에는 1월부터 12월까지 그 달에 포함딘 날짜수가 정리되어 있습니다. for in문과 range 또는 enumerate를 이용해서 다음과 같이 출력되도록 만들어 보세요.

1월의 날짜수는 31일 입니다.
2월의 날짜수는 29일 입니다.
...
위와 같은 형식으로 12월까지 출력하세요. 출력 형식은 코드의 print문을 활용해서 format()의 괄호 안을 채워 넣으면 됩니다.

days = [31,29,31,30,31,30,31,31,30,31,30,31]



print('{}월의 날짜수는 {}일 입니다.'.format(  ,  ))
"""

days = [31,29,31,30,31,30,31,31,30,31,30,31]

for month,day in enumerate(days) :
	print('{}월의 날짜수는 {}일 입니다.'.format(month+1,day))