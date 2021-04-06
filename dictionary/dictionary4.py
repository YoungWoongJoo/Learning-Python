"""
days_in_month에는 엉뚱하게도 -1월이라는 이름표와 값이 있는데요. 이 값을 지워보세요. (단, 첫번째 줄은 수정하지 마세요)

days_in_month = {"1월":31, "2월":28, "3월":31,"-1월":97889789}


print(days_in_month)
"""

days_in_month = {"1월":31, "2월":28, "3월":31,"-1월":97889789}
del(days_in_month["-1월"])

print(days_in_month)