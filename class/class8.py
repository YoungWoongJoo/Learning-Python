"""
Truck클래스는 Car클래스의 자식클래스입니다. Car클래스에 정의된 run을 Truck클래스에서 오버라이드해서 run을 실행하면 "트럭이 달립니다."라고 출력되도록 만들어 보세요.

class Car():
    
    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    
    def load(self):
        print("짐을 실었습니다.")
    # 이 아래에서 run 메소드를 오버라이드 하세요.
    
    
truck = Truck()
truck.run()
"""

class Car():
    
    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    
    def load(self):
        print("짐을 실었습니다.")
    # 이 아래에서 run 메소드를 오버라이드 하세요.

		def run(self):
			print("트럭이 달립니다.")
    
    
truck = Truck()
truck.run()