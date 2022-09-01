""""
takes dataframe and column names. Returns dataframe concat dummied columns.
You can specify drop_first and drop_orig for more.
"""


from typing import Sequence
import pandas as pd

def get_dummies(df:pd.DataFrame, cols:Sequence):
    pass

def test():
    df = pd.DataFrame({'a':['z','x','y'], 'b':[4,5,6], 'c':[7,8,9]})
    df2 = pd.DataFrame({'a2':['z','x','y'], 'b2':[4,5,6], 'c2':[7,8,9]})
    print(pd.concat(df, df2, axis=1))
test()