"""
다음 코드는 발생하는 예외를 try/except문으로 처리하고 있습니다. 5번째 줄에서는 어떤 에러가 발생하는지 출력할 수 있도록 빈칸을 채우고, 6번째 줄은 예외를 출력할 수 있도록 format의 빈칸을 작성하세요.

try:
    a = 5
    b = 0
    c = a / b
except 
:
    print('다음과 같은 에러가 발생했습니다: {}'.format( 
 ))
"""

try:
    a = 5
    b = 0
    c = a / b
except Exception as ex: #발생된 에러의 이름을 ex로 받아옴
    print('다음과 같은 에러가 발생했습니다: {}'.format( 
		 ))
		 """

		 try:
		     a = 5
				     b = 0
						     c = a / b
								 except Exception as ex: #발생된 에러의 이름을 ex로 받아옴
								 
    print('다음과 같은 에러가 발생했습니다: {}'.format(ex))