class calculator:
  def __init__(self, a, b):
    #self에는 calculator의 객체 calc가 자동으로 전달
    self.first = a
    self.second = b

  # def setdata(self, a, b):
  #   self.first = a
  #   self.second = b

  def add(self):
    return self.first + self.second

  def sub(self):
    return self.first - self.second

  def multi(self):
    return self.first * self.second

  def divid(self):
    return self.first/self.second

class newCalculator(calculator):
  def pow(self):
    return self.first ** self.second

class safeFourCal(calculator):
  def divid(self):
    if self.second == 0:
      return 0
    else:
      return self.first / self.second

fix = 2

if __name__ == "__main__":
  calc = calculator(4, 2)
  # print(calc)
  # calc.setdata(4, 2)
  # print(calc.add())
  # print(calc.sub())
  # print(calc.multi())
  # print(calc.divid())

  print('-------------')

  newCalc = newCalculator(10, 5)
  print(newCalc.pow())

  print('-------------')

  safeCalc = safeFourCal(6, 0)
  print(safeCalc.divid())

