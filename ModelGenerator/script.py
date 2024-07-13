import sys
sys.path.append("C:/Users/Lenovo/PycharmProjects/modelCreation")

import Langage
import ModelUtilities

class Main:
    def __init__(self):
        pass

    @staticmethod
    def run_test(language):
        ModelUtilities.ModelUtilities.test_language("model/model.joblib", language)
        language_list = language.split(',')
        return Langage.Langage.checkCode(language_list)
