""""
takes dataframe and column names. Returns dataframe concat dummied columns.
You can specify drop_first and drop_orig for more.
"""


from typing import Sequence
import pandas as pd

def uni_encoder(df:pd.DataFrame,
                cols_for_label:Sequence = None,
                cols_for_onehot:Sequence = None,
                cols_for_delete:Sequence = None,
                labels_kwargs:dict = None,
                ohe_kwargs:dict = None) -> pd.DataFrame:

    def _label(kwargs):
        from sklearn.preprocessing import LabelEncoder

        for col_name in cols_for_label:
            if kwargs:
                df[col_name] = LabelEncoder(**kwargs).fit_transform(df[col_name])
            else:
                df[col_name] = LabelEncoder().fit_transform(df[col_name])

    def _ohe(kwargs):
        from sklearn.preprocessing import OneHotEncoder
        nonlocal df
        for col_name in cols_for_onehot:
            columns=[f"{df[col_name]}_{i}" for i in range(df[col_name].nunique())]
            if kwargs:
                df = pd.concat(df, pd.DataFrame(OneHotEncoder(**kwargs).fit_transform(df[[col_name]]), columns = columns), axis = 1)
            else:
                df = pd.concat(df, pd.DataFrame(OneHotEncoder().fit_transform(df[[col_name]]), columns = columns), axis = 1)

    if not (cols_for_label or cols_for_onehot or cols_for_delete):
        raise Exception("Function takes at least one argument")
    if cols_for_label:
        _label(labels_kwargs)
    if cols_for_onehot:
        _ohe(ohe_kwargs)

    return df


df1 = pd.DataFrame({'a':[1,2,3], 'b': [4,5,6], 'c':[7,8,9]})
df2 = pd.DataFrame({'d':[10,11,12], 'e': [14,15,16], 'f':[17,18,19]})
lb = pd.DataFrame({'names': ['alan', 'dalan', 'kalan'], 'surname':['alanson', 'dalanson', 'kalanson']})
print(uni_encoder(lb, cols_for_onehot = ['names', 'surname']))
