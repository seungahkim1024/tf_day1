from calc.calculator import Calculator


def main():
    calc = Calculator(int(input("첫번째 수"))
                      , int(input("두번째 수")))
    print("{} + {} = {}"
          .format(calc.no1
                  , calc.no2
                  , calc.sum()))

    print("{} - {} = {}"
          .format(calc.no1
                  , calc.no2
                  , calc.sub()))

    print("{} * {} = {}"
          .format(calc.no1
                  , calc.no2
                  , calc.mul()))

    print("{} / {} = {}"
          .format(calc.no1
                  , calc.no2
                  , calc.div()))


if __name__ == '__main__':
        main()