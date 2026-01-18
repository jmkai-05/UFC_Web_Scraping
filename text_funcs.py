ASCII_OFFSET = 96

def get_first_name(first_name):
    return first_name.text.strip()

def get_last_name(last_name):
    return last_name.text.strip()

def get_nickname(nickname):
    nickname = nickname.text.strip()

    if nickname == '':
        nickname = None
    
    return nickname

def get_height(height):
    height = height.text.strip()

    if height == '--':
        height = None
    else:
        feet = int(height[0])

        if(height[3] == '"'):
            inch = int(height[2])
        else:
            inch = 10 + int(height[3])
        
        height = feet * 30.48 + inch * 2.54

    return height

def get_weight(weight):
    weight = weight.text.strip()

    if(weight == "--"):
        weight = None
    else:
        weight = weight[0:3]
    
    return weight

def get_reach(reach):
    reach = reach.text.strip()

    if(reach == '--'):
        reach = None
    else:
        reach = float(reach[0:4])
    
    return reach

def get_stance(stance):
    stance = stance.text.strip()
    
    if(stance == ''):
        stance = None

    return stance

def get_wins(wins):
    wins = int(wins.text.strip())

    return wins

def get_losses(losses):
    losses = int(losses.text.strip())

    return losses

def get_draws(draws):
    draws = int(draws.text.strip())

    return draws