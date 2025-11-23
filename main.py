import zipfile; z = zipfile.ZipFile('steam_games.zip'); 

print('\n'.join(z.namelist()[:10]))

import zipfile
import os

if not os.path.exists('data/'):
    os.makedirs('data/')

try:
    with zipfile.ZipFile('steam_games.zip', 'r') as zip_ref:
        zip_ref.extractall('data/')
except FileNotFoundError:
    pass
except Exception:
    pass



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

