#!/usr/bin/idle-python3.5
class animals:
  name = None

  weight = None #масса
  produce_a_product = None #производимый продукт
  growth_factor = None #Коэффициент роста

  def __init__(self, weight, produce_a_product, growth_factor):
    self.weight = weight
    self.produce_a_product = produce_a_product
    self.growth_factor = growth_factor
    print("экземпляр класс создан")

  def graze(self,value): #фунция пастись value дней
    print("Животное отправили пастись и наращивать массу")
    self.weight += value*self.growth_factor
    print("Масса: {} кг".format(self.weight))

  def description_animals(self):
    print("Животное {} массой {} кг., дает продукт {} с коэффициентом роста {} кг в день".format(self.name, self.weight, self.produce_a_product, self.growth_factor))

#Класс парнокопытнах для Коровы, козы, овцы, свиньи
class artiodactyl(animals):
  def graze(self,value):
    self.growth_factor += 2 #Для парнокопытных коэффициент роста +2
    print("Удар копытом")
    super().graze(value)

#класс коровы на основе класса парнокопытных
class cow(artiodactyl):
  name = "Корова"
  def graze(self,value):
    print("Муууу")
    super().graze(value)

#класс козы на основе класса парнокопытных
class goat(artiodactyl):
  name = "Коза"
  def graze(self,value):
    print("Бееееееее")
    super().graze(value)

#класс овцы на основе класса парнокопытных
class sheep(artiodactyl):
  name = "Овца"
  def graze(self,value):
    print("Меееее")
    super().graze(value)

#класс свиньи на основе класса парнокопытных
class pig(artiodactyl):
  name = "Свинья"
  def graze(self,value):
    self.growth_factor += 10 #Для свиней коэффициент роста +10
    print("Хрюююю")
    super().graze(value)

#Класс птиц для Утки, куры, гуси
class birds(animals):
  def graze(self,value):
    print("Взмах крылом")
    super().graze(value)

  def fly(self, value):
    print("Полет на расстояние:{} метров".format(value))

class duck(birds):
  name = "Утка"
  def graze(self,value):
    print("Кряяя Кряяя")
    super().graze(value)

class chicken(birds):
  name = "Курица"
  def graze(self,value):
    print("Кукареку")
    super().graze(value)

class goose(birds):
  name = "Гусь"
  def graze(self,value):
    print("Гагагага")
    super().graze(value)

pig1 = pig(300, "мясо", 3)
pig1.description_animals()
pig1.graze(3)
pig1.description_animals()

cow1 = cow(500, "Молоко", 2)
cow1.description_animals()
cow1.graze(3)
cow1.description_animals()

goat1 = goat(46, "Молоко", 1)
goat1.description_animals()
goat1.graze(3)
goat1.description_animals()

sheep1 = sheep(33, "Молоко", 1)
sheep1.description_animals()
sheep1.graze(3)
sheep1.description_animals()

duck1 = duck(10, "Мясо", 1)
duck1.description_animals()
duck1.graze(3)
duck1.description_animals()

chicken1 = chicken(7, "Яйцо", 1)
chicken1.description_animals()
chicken1.graze(3)
chicken1.description_animals()

goose1 = goose(15, "Мясо", 1)
goose1.description_animals()
goose1.graze(3)
goose1.description_animals()
