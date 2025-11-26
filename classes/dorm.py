import sqlite3

class Dorm:

    def __init__(self):
        self.rooms = [

            {"name" : "room1",
             "amount" : 0,
             "soldiers" : []
            },

            {"name" : "room2",
             "amount" : 0,
             "soldiers" : []
            },

            {"name" : "room3",
             "amount" : 0,
             "soldiers" : []
            },

            {"name" : "room4",
             "amount" : 0,
             "soldiers" : []
            },

            {"name" : "room5",
             "amount" : 0,
             "soldiers" : []
            },

            {"name" : "room6",
             "amount" : 0,
             "soldiers" : []
            },

            {"name" : "room7",
             "amount" : 0,
             "soldiers" : []
            },

            {"name" : "room8",
             "amount" : 0,
             "soldiers" : []
            },
    
            {"name" : "room9",
             "amount" : 0,
             "soldiers" : []
            },

            {"name" : "room10",
             "amount" : 0,
             "soldiers" : []
            }
        ]

    def add_to_room(self, soldier : object) -> None:
        added = False
        for room in self.rooms:
            if room["amount"] < 8:
                room["soldiers"].append(soldier)
                room["amount"] += 1
                print(f"Soldiers added to {room["name"]}")
                added = True
        if not added:
            print("Rooms are full - the soldier was not added.")

    def is_full(self):
        count = 0
        for i in self.rooms:
            count += i["amount"]
        return count == 80

    def print_rooms(self):
        for i in self.rooms:
            print(i)

   
    def deployment_soldier_rooms(self, soldiers):

        soldiers = sorted(soldiers, key=lambda x: x.distance_from_base, reverse=True)

        conn = sqlite3.connect("db/rooms.db")
        my_cursor = conn.cursor()
        
        for room in self.rooms:
            for soldier in soldiers:
                if room["amount"] < 10:
                    soldier.assignment_status = "assigned"
                    room["soldiers"].append(soldier)
                    room["amount"] += 1
                    command = f"INSERT INTO room(id, assignment_status, dorm, room_num) VALUES('{soldier.id}', 'assigned', '{self.__class__.__name__}', '{room["name"]}')"
                    print(command)
                    my_cursor.execute(command)
        conn.commit()
        
                    
                    


            

            
        
        