import collections
import random
import csv
import math
import Langage


class DataCreation:
    def __init__(self):
        pass

    @staticmethod
    def generation_random_word():
        word_length = random.randint(1, 7)
        word = ""
        for i in range(word_length):
            word += str(random.randint(0,1))
        return word

    @staticmethod
    def generation_random_language():
        language_length = random.randint(1, 10)
        language = []
        for i in range(language_length):
            language.append(DataCreation.generation_random_word())
        return language

    def is_de_bruijn_sequence_present(language, order):
        if len(language) < 2 ** order:
            return 0
        substrings = set()
        for i in range(len(language) - order + 1):
            substring = language[i:i + order]
            substring_str = "".join(substring)
            if substring_str in substrings:
                return 0
            substrings.add(substring_str)
        return 1

    def calculate_entropy(language):
        char_counts = collections.Counter("".join(language))
        total_chars = sum(char_counts.values())

        probabilities = {char: count / total_chars for char, count in char_counts.items()}

        entropy = 0
        for char, probability in probabilities.items():
            if probability > 0:
                entropy += probability * math.log2(probability)

        if(entropy < 0):
            return entropy*(-1)
        else:
            return entropy

    def getVariation(language,avg_word_length):
        result = 0
        for i in language:
            result += (len(i) - avg_word_length) ** 2

        return result / len(language)

    def ecartType(language,avg_word_length):
        return math.sqrt(DataCreation.getVariation(language,avg_word_length))

    @staticmethod
    def get_language_properties(language):
        word_lengths = [len(word) for word in language]
        language_properties = {
            "avg_word_length": sum(word_lengths) / len(language),
            "unique_words": len(set(language)),
            "entropy": DataCreation.calculate_entropy(language),
            "occurance0":sum(sum(1 - int(bit) for bit in word) for word in language)/len(language),
            "occurance1": sum(sum(int(bit) for bit in word) for word in language) / len(language),
            "ecartType": DataCreation.ecartType(language,sum(word_lengths) / len(language)),
            "variation": DataCreation.getVariation(language,sum(word_lengths) / len(language)),
            "classe": None,
        }
        return language_properties

    @staticmethod
    def create_data(number_of_lines, filename):
        data_x = []
        data_y = []
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["avg_word_length", "unique_words", "entropy", "occurance0", "occurance1","ecartType","variation", "classe"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            num_decodable = number_of_lines // 2
            num_non_decodable = number_of_lines // 2

            for _ in range(num_decodable):
                language = DataCreation.generation_random_language()
                while Langage.Langage.checkCode(set(language)) is True:
                    language = DataCreation.generation_random_language()
                language_properties = DataCreation.get_language_properties(language)
                classe = 0
                language_properties["classe"] = classe
                data_x.append(language_properties)
                data_y.append(classe)
                writer.writerow(language_properties)

            for _ in range(num_non_decodable):
                language = DataCreation.generation_random_language()
                while Langage.Langage.checkCode(set(language)) is False:
                    language = DataCreation.generation_random_language()
                language_properties = DataCreation.get_language_properties(language)
                classe = 1
                language_properties["classe"] = classe
                data_x.append(language_properties)
                data_y.append(classe)
                writer.writerow(language_properties)

        print(f"Fichier CSV créé : {filename}")

