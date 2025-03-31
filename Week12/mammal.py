from heart import Heart
class Mammal:
    def __init__(self, p_age, tick=None):#aggregation through parameter
        print("Constructor: inside the parent class constructor: making the mammal part of the object")
        self.age = p_age
        self.__live_birth = True
        self.heart = Heart()
        self.tick=tick

    @property
    def live_birth(self):
        return self.__live_birth
    @live_birth.setter
    def live_birth(self, p_live_birth):
        self.__live_birth = p_live_birth
    
    def love(self):
        print("Mammal is in love")
    def mammal_checkup(self):
        self.heart.beat()
        if self.tick:
            self.tick.suck_blood()

    def __str__(self):
        tick_status= "attached" if self.tick else "none"
        return f"Mammal(age={self.age}, live_birth={self.__live_birth}, tick={tick_status}, heart_bpm={self.heart.bpm})"
    def __del__(self):
        print("Mammal is destroyed")