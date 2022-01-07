from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import accuracy_score
from catboost import CatBoostClassifier
from xgboost import XGBClassifier

class SobrietyClassifier(object):

    def __init__(self) -> None:
        
        self.X = None
        self.y = None
    
    def fit(self, X_train, y_train):
        
        self.X = X_train
        self.y = y_train

    def predict(self, X_test):

        clf1 = RandomForestClassifier()
        clf2 = XGBClassifier(use_label_encoder = False)
        clf3 = CatBoostClassifier()

        model = VotingClassifier(estimators = [('rf', clf1), ('xgb', clf2), ('cat', clf3)], voting = 'hard')
        model.fit(self.X, self.y)
        prediction_values = model.predict(X_test)
        return prediction_values
    
