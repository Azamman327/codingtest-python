#달리기 경주
def solution(players, callings):
    dictionary = {player: i for i, player in enumerate(players)}
    
    for who in callings:
        idx = dictionary[who]
        dictionary[who] -= 1
        dictionary[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    
    return players