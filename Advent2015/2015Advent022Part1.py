import itertools
kombi=[]
iter_kombi = itertools.product([1,2,3,4,5],repeat=9)
for i in iter_kombi: kombi.append(i)

enemy = (100,9)
player_hp = 50
player_mana = 500

# kombi = [(4,1)]
# enemy = (13,8)
# player_hp = 10
# player_mana = 250

# kombi = [(5,3,2,4,1)]
# enemy = (13,8)
# player_hp = 10
# player_mana = 250

def fight(combi, p_hp, p_mana, e_hp, e_dmg):
    turn = 'P'
    idx_combi = 0
    idx_shield = 0
    idx_poison = 0
    idx_recharge = 0
    mana_spend = 0
    while p_hp > 0 and e_hp > 0 and idx_combi < len(combi):
        temp_idx = combi[idx_combi]
        if idx_shield == 0: p_arm = 0
        if idx_shield > 0: idx_shield -= 1
        if idx_poison > 0:
            e_hp -= 3
            idx_poison -= 1
        if idx_recharge > 0:
            p_mana += 101
            idx_recharge -= 1
        if turn == 'P':
            if temp_idx == 5:
                if idx_recharge == 0:
                    p_mana -= 229
                    mana_spend += 229
                    idx_recharge = 5
                else:
                    if e_hp <= 4: temp_idx = 1
                    if p_hp <= 20: temp_idx = 2
                    else: temp_idx = 4
            if temp_idx == 4:
                if idx_poison == 0:
                    p_mana -= 173
                    mana_spend += 173
                    idx_poison = 6
                else:
                    if e_hp <= 4: temp_idx = 1
                    if p_hp <= 20: temp_idx = 2
                    else: temp_idx = 3
            if temp_idx == 3:
                if idx_shield == 0:
                    p_mana -= 113
                    mana_spend += 113
                    idx_shield = 6
                    p_arm = 7
                else:
                    if e_hp <= 4 or p_hp > 20: temp_idx = 1
                    if p_hp <= 20: temp_idx = 2
            if temp_idx == 1:
                p_mana -= 53
                mana_spend += 53
                e_hp -= 4
            if temp_idx == 2:
                p_mana -= 73
                mana_spend += 73
                e_hp -= 2
                p_hp += 2
            idx_combi += 1
            print(combi, turn, p_hp, p_mana, e_hp, e_dmg)
            turn = 'E'
        elif turn == 'E':
            damage = e_dmg-p_arm
            p_hp -= damage
            print(combi, turn, p_hp, p_mana, e_hp, e_dmg)
            turn = 'P'
    if p_hp > 0: return (mana_spend)
    elif e_hp > 0: return (0)
    elif p_mana < 0: return (-1)

erg_mana = 9999999

for i in kombi:
    erg = fight(i, player_hp, player_mana, enemy[0], enemy[1])
    if erg > 0 and erg < erg_mana: erg_mana = erg
print(erg_mana)