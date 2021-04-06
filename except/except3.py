"""
다음 코드는 문구점 3곳을 검사하면서 풀이 있으면 문구점의 이름과 가격을 출력합니다.
실행 버튼을 눌러서 출력 결과를 확인해 보세요.

풀을 파는 가게를 발견하면 for문 전체를 즉시 종료하고 싶습니다. for 문을 try/except로 감싸고 print문 다음에 raise StopIteration을 추가해서 풀을 파는 가게를 하나만 출력하도록 만들어 보세요. except문에서는 StopIteration을 지정해 주어야 합니다.

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

for shop, products in shops.items():
    for product, price in products.items():
        if product =='풀':
            print("{}: {}원".format(shop, price))
"""

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

try:
	for shop, products in shops.items():
			for product, price in products.items():
					if product =='풀':
						raise StopIteration #raise를 통해 원하는 예외 발생
except StopIteration:
	print("{}: {}원".format(shop, price))