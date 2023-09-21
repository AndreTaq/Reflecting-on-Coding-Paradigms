### Functional Prompt

# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
def flatten_and_sort(array):
  arr = []
  for item in array:
    for i in item:
      arr.append(i)

  return sorted(arr)

print(flatten_and_sort("12946aefsd78556"))

# How does this solution ensure data immutability? in two sentances
# It creates a new array with the same values as the original array and flattened and sorted data, leavine the original array unchanged.

# Is this solution a pure function? Why or why not?
# Yes, it is a pure function because it does not have any class variables and it does not mutate the original array

# Is this solution a higher order function? Why or why not?
# No, it is not because a higher-order function is one that either takes one or more functions as arguments or returns a function as its result.

# Would it have been easier to solve this problem using a different programming style?
# Yes

# Why in particular is functional programming a helpful paradigm when solving this problem?
# It makes the code easier to read



###### Object Oriented Prompt

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

# Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"

pod = Podracer("", "great condition", "")
print(pod.repair())
print(pod.condition)

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def boost(self):
    self.max_speed *=2 

new_pod = AnakinsPod("2", "", "")
print(new_pod.boost())
print(new_pod.max_speed)

# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self):
    self.condition = "trashed"

third_pod = SebulbasPod("", "Very Good", "")
print(third_pod.flame_jet())
print(third_pod.condition)


# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)


# Encapsulation:
# The classes (Podracer, AnakinsPod, and SebulbasPod) encapsulate attributes (e.g., max_speed, condition, price) and methods (e.g., repair, boost, flame_jet) that operate on those attributes.
# The attributes are encapsulated within each class, and access to them is controlled through methods, promoting data integrity and encapsulation.

# Inheritance:
# The classes AnakinsPod and SebulbasPod inherit from the Podracer class using the super() function. Inheritance represents an "is-a" relationship, where AnakinsPod and SebulbasPod are specialized versions of Podracer. This allows code reuse and the ability to extend or override behavior as needed.

# Polymorphism:
# Polymorphism is the ability of different classes to be treated as instances of their parent class. In this solution, AnakinsPod and SebulbasPod are treated as instances of the Podracer class. However, true polymorphism would involve overriding methods to provide different implementations. While not explicitly demonstrated in this code, it is implied that you can use boost and flame_jet methods on instances of AnakinsPod and SebulbasPod, respectively, which could be seen as a form of polymorphism.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# No, OOP style used in this solution is appropriate and effective for modeling Podracers and their associated attributes and behaviors. OOP provides a natural way to encapsulate data and methods related to objects, making it well-suited for this problem.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# OOP assists in solving this problem by allowing the modeling of Podracers as objects with encapsulated attributes (e.g., max_speed, condition, price) and behaviors (e.g., repair, boost, flame_jet), making the code more organized, reusable, and easier to manage.

