import sys

import DataCreation
import Langage
import ModelUtilities

class Main:
    def __init__(self):
        pass

    language = sys.argv[1]
    #DataCreation.DataCreation.create_data(5000,"data.csv")
    #ModelUtilities.ModelUtilities.create_model_from_csv("data.csv")
    ModelUtilities.ModelUtilities.test_language("C:/Users/Lenovo/PycharmProjects/modelCreation/model/model.joblib", language)
    language = language.split(',')
    print(',')
    print(Langage.Langage.checkCode(language))


