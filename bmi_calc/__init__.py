from bmi_calc.bmi import Bmi


def main():
    bmi = Bmi((input("이름 "))
              , int(input("키 "))
              , int(input("몸무게 ")))
    print("{}님의 BMI는 {}"
          .format(bmi.name
                  , bmi.bmi()))


if __name__ == '__main__':
    main()
