"""
product_list에는 상품의 목록이 들어 있고, price_list에는 각 상품의 가격이 순서대로 들어있습니다. 딕셔너리 컴프리헨션을 이용해서 product_dict를 상품의 이름을 키로 가지고, 가격을 값으로 가지는 딕셔너리로 만들어보세요.

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict =


print(product_dict)
"""

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {product:price for product,price in zip(product_list,price_list)}


print(product_dict)