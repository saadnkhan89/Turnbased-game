#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random as rd

class item:
    def __init__(self,name,attack_damage,attack_magic,armor,magic_resist):
        self.name=name
        self.attack_damage=attack_damage
        self.attack_magic=attack_magic
        self.armor=armor
        self.magic_resist=magic_resist


sword=item("sword",10,0,0,0)
wand=item("item",0,10,0,0)
shield=item('shield',0,0,0,10)
rune=item('rune',0,0,0,10)

class player:
    def __init__(self):
        self.health=100
    def set_health(self,health):
        self.health=health

def main():
    player1=player()
    player1.health=20
    player2=player()
    player2.health=20
    while player1.health>0 or player2.health>0:
        print('attack move: Select wand or sword')
        a=input()
        if a=='sword':
            damage=sword.attack_damage
        elif a=='wand':
            damage=wand.attack_magic
        r1=rd.randint(0,1)
        if r1==0 and a=='wand':
            player2.health=player2.health-10
        elif r1==1 and a=='sword':
            player2.health=player2.health-10
        print('player 1 health:',player1.health)
        print('player 2 health:',player2.health)
        print('defend move: Select armor or magic resist')
        b=input()
        if b=='shield':
            defence=sheild.armor
        elif b=='rune':
            defence=rune.magic_resist
        r2=rd.randint(0,1)
        if r2==0 and b=='rune':
            player1.health=player1.health-10
        elif r2==1 and b=='armor':
            player1.health=player1.health-10
        print('player 1 health:',player1.health)
        print('player 2 health:',player2.health)
        
if __name__ == "__main__":
    main()        


# In[ ]:




