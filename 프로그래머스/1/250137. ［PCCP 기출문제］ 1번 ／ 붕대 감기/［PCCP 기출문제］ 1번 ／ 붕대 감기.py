def solution(bandage, health, attacks):
    current_health = health
    max_health = health
    last_attack_time = 0
    
    for attack_time, damage in attacks:
        time_diff = attack_time - last_attack_time - 1
        
        if time_diff > 0:
            current_health += time_diff * bandage[1]
            bonus_heal_count = time_diff // bandage[0]
            current_health += bonus_heal_count * bandage[2]
        
            if current_health > max_health:
                current_health = max_health
        
        current_health -= damage
        
        if current_health <= 0:
            return -1
        
        last_attack_time = attack_time
    
    return current_health