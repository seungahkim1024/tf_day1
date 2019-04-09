class Bmi:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        re = self.weight/(self.height*self.height)*10000

        if re > 40:
            return "고도비만"
        elif re >= 35:
            return "중등도비만"
        elif re >= 30:
            return "경도비만"
        elif re >= 35:
            return "과체중"
        elif re >= 18.5:
            return "정상"
        elif re < 18.5:
            return "저체중"
