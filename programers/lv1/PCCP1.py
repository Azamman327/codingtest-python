#기술의 시전 시간, 1초당 회복량, 추가 회복량 / 공격시간, 피해량
def healing(health, maxHealth, bandage, count):
    if (health < maxHealth):
        health += bandage
        if (health > maxHealth):
            health = maxHealth
    return health, count + 1

def bonusHealing(health, maxHealth, bonus):
    health += bonus
    if (health > maxHealth):
        health = maxHealth
    return health, 0

def solution(bandage, health, attacks):
    answer = 0
    count = 0
    maxHealth = health
    
    second = 0
    count = 0
    while attacks:
        second += 1
        
        if (second == attacks[0][0]):
            health, count = health - attacks[0][1], 0
            attacks.pop(0)
        
        else:
            health, count = healing(health, maxHealth, bandage[1], count)
            
            if count == bandage[0]:
                health, count = bonusHealing(health, maxHealth, bandage[2])
                
        if health <= 0:
            return -1
                
    return health
