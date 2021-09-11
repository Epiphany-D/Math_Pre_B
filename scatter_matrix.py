import numpy as np
import pandas as pd

# df = pd.read_csv('file01.csv')

df = pd.DataFrame(np.random.randn(100, 4), columns=['a', 'b', 'c', 'd'])
pd.scatter_matrix(df, figsize=(10, 6),
                  marker='o',
                  diagonal='kde',
                  alpha=0.5,
                  range_padding=0.1)
