import itertools
weapons = {1:(8,4,0), 2:(10,5,0), 3:(25,6,0), 4:(40,7,0),5:(74,8,0)}
armors = {0:(0,0,0),1:(13,0,1),2:(31,0,2),3:(53,0,3),4:(75,0,4),5:(102,0,5)}
rings = {0:(0,0,0),1:(25,1,0),2:(50,2,0),3:(100,3,0),4:(20,0,1),5:(40,0,2),6:(80,0,3)}
enemy = (100,8,2)
player_hp = 100
max_gold = 0

ring_kombis = [0,1,2,3,4,5,6]
kombi = itertools.combinations([1,2,3,4,5,6],2)
for i in kombi: ring_kombis.append(i)

def fight(p_hp,p_dmg,p_arm,e_hp,e_dmg,e_arm):
    turn = 'P'
    while p_hp > 0 and e_hp > 0:
        if turn == 'P':
            player_hit = p_dmg - e_arm
            if player_hit > 1: e_hp -= player_hit
            else: e_hp -= 1
            turn = 'E'
        elif turn == 'E':
            enemy_hit = e_dmg - p_arm
            if enemy_hit > 1: p_hp -= enemy_hit
            else: p_hp -= 1
            turn = 'P'
    if p_hp > 0: return ("WIN")
    elif e_hp > 0: return ("LOOSE")
    else: return ("DRAW")

for w in weapons:
    for a in range(6):
        for r in ring_kombis:
            if isinstance(r,int):
                player_dmg = weapons.get(w)[1] + rings.get(r)[1]
                player_arm = armors.get(a)[2]+ rings.get(r)[2]
                ring_gold = weapons.get(w)[0] + armors.get(a)[0] + rings.get(r)[0]
            else:
                player_dmg = weapons.get(w)[1] + rings.get(r[0])[1] + rings.get(r[1])[1]
                player_arm = armors.get(a)[2] + rings.get(r[0])[2] + rings.get(r[1])[2]
                ring_gold = weapons.get(w)[0] + armors.get(a)[0] + rings.get(r[0])[0] + rings.get(r[1])[0]
            erg = fight(player_hp, player_dmg, player_arm, enemy[0], enemy[1], enemy[2])
            print(w, a, r, player_dmg, player_arm, ring_gold, erg)
            if erg in ["LOOSE","DRAW"] and ring_gold > max_gold: max_gold = ring_gold
print(max_gold)