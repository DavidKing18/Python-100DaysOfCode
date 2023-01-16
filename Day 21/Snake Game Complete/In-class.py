class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
print("\n\n")


# How to slice lists and tuples in python

piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
piano_tuples = ('do', 're', 'mi', 'fa', 'so', 'la', 'ti')

print(piano_keys[2:5])
print(piano_keys[2:5:2])
print(piano_keys[::2])
print(piano_keys[::-1])
print()

print(piano_tuples[2:5])
print(piano_tuples[2:5:2])
print(piano_tuples[::2])
print(piano_tuples[::-1])
