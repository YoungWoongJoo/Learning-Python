"""
days_in_month에는 2월이 28일까지 있다고 만들어져 있는데요. 알고보니 2016년에는 2월이 29일까지 있습니다. "2월"이라는 이름표가 가지는 값을 29로 수정해 보세요. (단, 첫번째 줄은 수정하지 마세요)

days_in_month = {"1월":31, "2월":28, "3월":31}


print(days_in_month)
"""

days_in_month = {"1월":31, "2월":28, "3월":31}
days_in_month["2월"]=29

print(days_in_month)