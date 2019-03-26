class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    
    @property
    def is_alive(self):
        return (self.health > 0)


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7
        
class Army:
    def __init__(self):
        self._unit_list = []
    
    def add_units(self, UnitClass, num):
        for _ in range(num):
            self._unit_list.append(UnitClass())
            
    @property
    def units(self):
        return self._unit_list
        
    @units.setter
    def units(self, value):
        self._unit_list = value
        
            
class Battle:
    def __init__(self):
        pass
    
    def fight(self, f_army, s_army):
        for unit in f_army.units:            
            while self._fight(unit, s_army.units[0]):
                s_army.units = s_army.units[1:]
                
                if len(s_army.units) == 0:
                    return True
        
        return False
            
    def _fight(self, unit_1, unit_2):
        while unit_1.health > 0 and unit_2.health > 0:
            unit_2.health -= unit_1.attack
        
            if unit_2.health <= 0:
                break
            
            unit_1.health -= unit_2.attack
        
        return unit_1.health >= unit_2.health

def fight(unit_1, unit_2):
        while unit_1.health > 0 and unit_2.health > 0:
            unit_2.health -= unit_1.attack
        
            if unit_2.health <= 0:
                break
            
            unit_1.health -= unit_2.attack
        
        return unit_1.health >= unit_2.health



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
