class Bird:
    def fly(self):
        return "bird is flying"
    
class Airplane:
    def fly(self):
        return "plane is flying"
    
def duck(obj):
    return obj.fly()

print(duck(Bird()))