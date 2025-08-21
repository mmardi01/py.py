from S1E9 import Character
class Baratheon(Character):
    """Representing the Baratheon family."""
    family_name = ""
    eyes = ""
    hairs = ""
    def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __getattribute__(self, name):
        if name == "__str__":
            return f"<bound method Baratheon.__str__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"
        if name == "__repr__":
            return f"<bound method Baratheon.__repr__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"
        return object.__getattribute__(self, name)
#your code here
class Lannister(Character):
    """Lannister the Baratheon family."""
    family_name = ""
    eyes = ""
    hairs = ""
    def __init__(self, first_name, is_alive=True, family_name="Lannister", eyes="blue", hairs="light"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __getattribute__(self, name):
        if name == "__str__":
            return f"<bound method Lannister.__str__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"
        if name == "__repr__":
            return f"<bound method Lannister.__repr__ of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')>"
        return object.__getattribute__(self, name)
    @classmethod
    def create_lannister(cls, name, is_alive=True):
            print(cls)
            return cls(name, is_alive)
  
