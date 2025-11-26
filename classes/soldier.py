

class Soldier:

    def __init__(self, id: int, f_name : str, l_name : str, gender : str, city : str, distance_from_base : int, assignment_status : str = "waiting"):

        try:
            if isinstance(id, int) and str(id)[0] == "8":
                self.id = id
            else:
                print("Error - A number that starts with 8 and contains only numbers.")
                raise Exception
                

            self.f_name = f_name
            self.l_name = l_name

            if gender in ["male", "femail"]:
                self.gender = gender
            else:
                print("Error - gender can be 'male' or 'female'.")
                raise Exception

            self.city = city
            self.distance_from_base = distance_from_base

            if assignment_status in ["assigned", "waiting"]:
                self.assignment_status = assignment_status
            else:
                print("Error - assignment status can be 'assigned' or 'waiting'.")
                raise Exception

            print(f"Soldier {f_name} {l_name} added successfully")
        except:
            print(f"Fail -  {f_name} {l_name} NOT!! added", )







        