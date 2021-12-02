
from abc import abstractclassmethod


class Band():

    instances = []
    def __init__(self, name="unkown", members=[]):
        self.name = name
        self.members = members
        Band.instances.append(self)
    
    @classmethod
    def to_list(cls):
        return cls.instances
    
   
    def play_solos(self):
       solos = []
       for member in self.members:
           solos.append(member.play_solo())
       return solos

    pass

class Musician:
    def __str__(self):
        return "My name is " + str(self.name) + " and I play " + str(self.instrument) 
    
    def __repr__(self):
        if self.instrument == 'guitar':
            musician_type = 'Guitarist'
        elif self.instrument == 'bass':
            musician_type = 'Bassist'
        elif self.instrument == 'drums':
            musician_type = 'Drummer'
        rep = f"{musician_type} instance. Name = " + self.name
        return rep
    
    def get_instrument(self):
        return self.instrument
    pass

class Guitarist(Musician):
    def __init__(self, name="unknown"):
        self.name = name
        self.instrument = 'guitar'
    
    def play_solo(self):
        return "face melting guitar solo"
    pass
    
    
class Bassist(Musician):
    def __init__(self, name="unknown"):
        self.name = name
        self.instrument = 'bass'
    
    def play_solo(self):
        return "bom bom buh bom"
    pass


class Drummer(Musician):
    def __init__(self, name="unknown"):
        self.name = name
        self.instrument = 'drums'
    
    def play_solo(self):
        return "rattle boom crash"
    pass


