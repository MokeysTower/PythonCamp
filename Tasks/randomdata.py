import datetime
from math import e
import random 
try:
    x = datetime.date(random.randint(1,2021),random.randint(1,12),random.randint(1,31))
except:
    try:
        x = datetime.date(random.randint(1,2021),random.randint(1,12),random.randint(1,30))
    except:
        try:
            x = datetime.date(random.randint(1,2021),random.randint(1,12),random.randint(1,29))
        except:
            try:
                x = datetime.date(random.randint(1,2021),random.randint(1,12),random.randint(1,28))
            except:
                print("Sorry you are looser")
print(x)