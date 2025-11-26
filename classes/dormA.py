from .dorm import Dorm

class DormA(Dorm):
    
    def __init__(self):
        super().__init__()

    def add_to_room(self, soldier):
        return super().add_to_room(soldier)
    
    def is_full(self):
        return super().is_full()
    
    def print_rooms(self):
        return super().print_rooms()
    
    def deployment_soldier_rooms(self, soldiers):
        return super().deployment_soldier_rooms(soldiers)
    
    