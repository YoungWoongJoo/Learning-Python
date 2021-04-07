"""
taxi는 Car클래스의 인스턴스로 "택시"라는 이름을 가지고 있습니다.taxi.run()을 호출할 수 있도록 Car클래스 밖에 정의되어 있는 run함수를 클래스 안으로 가져오세요. 가져온 다음에는 run의 매개변수인 car를 self로 변경하세요.

class Car():
    '''자동차'''


def run(car):
    print("{}가 달립니다.".format(car.name))

taxi = Car()
taxi.name = "택시"
taxi.run()
"""

class Car():
    '''자동차'''

	def run(self):
    print("{}가 달립니다.".format(self.name))

taxi = Car()
taxi.name = "택시"
taxi.run()