"""
Truck클래스는 Car클래스의 상속을 받는 자식클래스입니다. Truck클래스의 __init__에서 name, capacity(몇톤트럭인지)를 입력받아 인스턴스의 값으로 저장하세요. (단, Truck클래스의 __init__에서 name을 설정하는 부분은 super()를 이용해서 처리하도록 만드세요.)

class Car():
    
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    # 이 아래에서 __init__ 메소드를 오버라이드 하세요.
    
    def load(self):
        print("짐을 실었습니다.")
"""

class Car():
    
    def __init__(self, name):
      self.name = name
    
    def run(self):
      print("차가 달립니다.")


class Truck(Car):
    # 이 아래에서 __init__ 메소드를 오버라이드 하세요.
		def __init__(self,name,capacity):
			super().__init__(name)
			self.capacity=capacity
    
    def load(self):
        print("짐을 실었습니다.")