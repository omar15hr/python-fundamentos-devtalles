class CoffeeMaker: 

  def make_coffee(self):
    self.__boil_water()
    self.__mix()
    print("PI PI")
    print("Tu cafe esta listo")

  def __boil_water(self):
    print("Hirviendo agua")

  def __mix(self):
    print("Combinando cafe y agua")

coffee_maker = CoffeeMaker()
coffee_maker.make_coffee()

# La abstraccion se enfoca en lo que hace y no en como lo hace