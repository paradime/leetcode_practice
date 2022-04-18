class Animal:
  # instance method
  def name(self):
    return 'animal'

  # static method
  def nameStatic():
    return 'static animal'

class Being:
  def name(self):
    return 'being'

class Dog(Animal, Being):
  def name(self):
    return 'dog'

  def superName(self):
    return super().name()

  def __getattr__(self, name):
    def _missing(*args, **kwargs):
      print("A missing method was called.")
      print("The object was %r, the method was %r. " % (self, name))
      print("It was called with %r and %r as arguments" % (args, kwargs))
    return _missing

# decorator function to convert to lowercase
def lowercase_decorator(function):
  def wrapper(*args):
    func = function(*args)
    string_lowercase = func.lower()
    return string_lowercase
  return wrapper

@lowercase_decorator # this is executed first
def helloWorld(name):
  return f'Hello World {name}!'