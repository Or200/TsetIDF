from classes.soldier import Soldier
from classes.dormA import DormA

if __name__ == "__main__":
    dorm1 = DormA()
    Soldier.add_soldier()
    soldiers = Soldier.list_of_soldiers
    dorm1.deployment_soldier_rooms(soldiers)

    