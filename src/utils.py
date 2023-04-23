import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score as r2
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(x_train,y_train,x_test,y_test,model):
     report ={}
     for i in model:
         model_n = model[i]
         model_n.fit(x_train,y_train)
         y_train_pred = model_n.predict(x_train)
         y_test_pred = model_n.predict(x_test)
         train_model_score = r2(y_train,y_train_pred)
         test_model_score = r2(y_test,y_test_pred)
         
         report[i] = test_model_score

     return report










         

