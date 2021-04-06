"""
for in문을 이용해서 days_in_month의 이름표(key)를 한줄씩 출력해 보세요.

days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}
"""

days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

for key in days_in_month.keys():
	print(key)