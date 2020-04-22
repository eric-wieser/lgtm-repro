class HasA:
    def method(self):
        return 'a'
        
class HasB:
    def method(self):
        return 'b'
        
class HasAB(HasA, HasB):
    def method(self):
        return 'ab'
        
class CustomA(HasA):
    def new_method(self):
        pass
    
class CustomAB(CustomA, HasAB):
    pass
