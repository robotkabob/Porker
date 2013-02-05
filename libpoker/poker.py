from card import qCard
from deck import qDeck
import math

def chenFormula(a,b):
    """Returns the Chen Starting Hand Formula value for cards a,b."""
    #pick high card
    if a.getValue() >= b.getValue():
        highCard = a
        lowCard = b
    else:
        highCard = b
        lowCard = a
    
    #assign initial value to high card    
    value = {  14:10, 13:8, 12:7, 11:6, 10:5, 9:4.5, 8:4, 7:3.5, 6:3, 5:2.5, 4:2, 3:1.5, 2:1   }[highCard.getValue()]
    
    #double pair score
    if highCard.getValue() == lowCard.getValue():
        value = value * 2
    
    #add two points for suited
    if highCard.getSuit() == lowCard.getSuit():
        value = value + 2
        
    #add 1 for connectors (EG KQ)
    #if highCard.getValue() - 1 == lowCard.getValue():
    #    value = value + 1
        
    #subtract for gaps
    gap = highCard.getValue() - lowCard.getValue() - 1
    if gap == 1:
        value = value - 1
    elif gap == 2:
        value = value - 2
    elif gap == 3:
        value = value - 3
    elif gap >= 4:
        value = value - 5
    
    #add 1 if both cards <Q
    if (gap == 0) or (gap == 1):
        if highCard.getValue() < 12:
            if highCard.getValue() != lowCard.getValue():
                value = value + 1
    
    
    
    return int(math.ceil(value))