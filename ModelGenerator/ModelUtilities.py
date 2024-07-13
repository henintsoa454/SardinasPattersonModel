import joblib
import pandas as pd
import joblib as jb
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

import DataCreation


class ModelUtilities:
    def __init__(self):
        pass

    @staticmethod
    def create_model_from_csv(filename):
        data = pd.read_csv(filename)

        X = data[['avg_word_length', 'unique_words', 'entropy', 'occurance0', 'occurance1', 'ecartType', 'variation']]
        y = data['classe']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }

        # Create the RandomForest model
        rf = RandomForestClassifier()

        # Setup GridSearchCV
        grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)

        # Train the model with GridSearchCV
        grid_search.fit(X_train, y_train)

        # Get the best model
        best_rf = grid_search.best_estimator_

        # Evaluate the model on the test set
        test_accuracy = accuracy_score(y_test, best_rf.predict(X_test))

        print("Best hyperparameters:", grid_search.best_params_)
        print("Testing Accuracy:", test_accuracy)

        # Save the best model
        jb.dump(best_rf, "model/model.joblib")

    @staticmethod
    def load_model_from_joblib(joblib_file):
        model = joblib.load(joblib_file)
        return model

    @staticmethod
    def test_language(model_file, language):
        words = language.split(',')
        language_properties = DataCreation.DataCreation.get_language_properties(words)
        language_df = pd.DataFrame([language_properties]).drop(['classe'], axis=1)
        model = joblib.load(model_file)
        prediction = model.predict(language_df)
        if prediction[0] == 1:
            print("Language is decodable")
        else:
            print("Language is not decodable")