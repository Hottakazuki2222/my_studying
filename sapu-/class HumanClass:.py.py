class HumanClass:
    #def defend(self):
        #print('防御しました！')
    def __init__(self): 
        print('HumanClassのinit')
        self.hp = 100


class WizardClass:
    def __init__(self):
        #super().__init__()
        self.mp = 50
        #print('WizardClassのinit')
    def cast_spell(self):
        print('呪文を唱える')

    #def output_info(self):
        #print(f'現在のHPは{self.hp}で、'
              #f'MPは{self.mp}です。')
        
class SwprdFighterClass:
    def __init__(self):
        print('SwordFighterClassのinit')
    def attack_with_sword(self):
        print("剣で攻撃する")

class MagicSwordFighterClass(WizardClass,SwprdFighterClass):
    pass


msf = MagicSwordFighterClass()
msf.cast_spell()
msf.attack_with_sword()

#wizard = WizardClass()
#print(wizard.mp)
#wizard.output_info()
