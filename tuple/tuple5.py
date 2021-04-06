"""
products의 상품명과 값을 한 줄씩 출력하도록 코드의 4번째줄의 빈칸을 채워 보세요.

products = {"풀" : 800, "색종이": 1000}

for product_detail in products.items():
    print("{}의 가격: {}원".format( 
 ))
"""

products = {"풀" : 800, "색종이": 1000}

for product_detail in products.items():
    print("{}의 가격: {}원".format(*product_detail))