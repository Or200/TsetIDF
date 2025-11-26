

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
            
        
        