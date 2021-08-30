class Fish():
  def __init__(self):
    print("鱼都生活在水里。")
  def weight(self,weight):
    print("鱼的重量:{}".format(weight))
class caoyu(Fish):
   def __init__(self):
    print("鱼类都有鳃。但不会得腮腺炎。")

xiaoli = caoyu()
xiaoli.weight(100)