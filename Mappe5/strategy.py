import numpy as np
import blotto


# her forandrer eg strategi sånn at eg sånn ca vinner hver gang med 2 poeng, har ikkje tapt endå men du vet aldrig 
def player_strategy(n_battalions,n_fields):
    #defining the array:
    battalions=np.zeros(n_fields,dtype=int)
    
    #assigning 25 battalions to the first four battle fields:
    battalions[0]=10
    battalions[1]=20
    battalions[2]=20
    battalions[3]=20
    battalions[4]=20
    battalions[5]=10
    
    
    
    #asserting that all and no more than all battalions are used:
    battalions=battalions[np.random.rand(n_fields).argsort()]
    assert sum(battalions)==n_battalions
    
    return battalions

def computer_strategy(n_battalions,n_fields):
    battalions=np.zeros(n_fields,dtype=int)
    battalions[0:1]=8
    battalions[1:4]=30
    battalions[4:]=1
    assert sum(battalions)==n_battalions
    return battalions

blotto.run(6,100,player_strategy)
