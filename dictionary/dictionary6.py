"""
days_in_month의 각 이름표와 값을 다음과 같은 형식으로 출력해 보세요.

1월은 31일이 있습니다.
2월은 28일이 있습니다.
...
정확한 출력 형식은 작성되어 있는 print함수를 참고하세요.

days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

#출력 형식은 아래 print함수를 참고하세요
print("{}은 {}일이 있습니다.".format(        ) )
"""

days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

for key,value in days_in_month.items():
#출력 형식은 아래 print함수를 참고하세요
	print("{}은 {}일이 있습니다.".format(key,value))