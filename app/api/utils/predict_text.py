import tensorflow as tf
import pandas as pd

from os import path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.utils import pad_sequences
from num2words import num2words
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# nltk.download('punkt')
# nltk.download('stopwords')

factory = StemmerFactory()
stemmer = factory.create_stemmer()
stop_words = set(stopwords.words("indonesian"))


def load_model():
    return tf.keras.models.load_model(path.abspath("app/keras_model/model_nlp.h5"))


def preprocess_text(text):
    text = word_tokenize(text.lower())
    text = [t for t in text if t not in stop_words]
    text = [stemmer.stem(t) for t in text]
    text = [t if not t.isdigit() else num2words(int(t)) for t in text]
    text = " ".join(text)
    return text


# Text for testing predict_list_text
list_text_test = [
    "Saya sangat senang hari ini",
    # "Saya ingin bunuh diri",
    # "Saya menyesal",
    # """Hari ini, tanggal 1 Mei 2023, saya sangat sulit untuk bangun dari tempat tidur. Saya merasa sangat lelah dan sedih, dan tidak ingin melakukan apa pun. Saya merasa seperti tidak ada yang peduli dengan saya dan tidak punya tempat yang benar-benar merasa seperti rumah.
    #     Saya merasa seperti saya tidak memiliki nilai apa pun dan seperti tidak ada yang akan merasa kehilangan jika saya pergi. Saya merasa sangat kesepian dan tidak tahu apa yang harus saya lakukan untuk merasa lebih baik.
    #     Saya berusaha untuk melakukan beberapa tugas rumah, tetapi rasanya sangat berat dan sulit untuk fokus. Saya merasa sangat sedih dan hampa, dan tidak tahu bagaimana cara keluar dari perasaan ini. Rasanya seperti saya terjebak dalam perasaan sedih dan putus asa.
    #     Saya mencoba untuk berbicara dengan beberapa teman, tetapi rasanya seperti mereka tidak benar-benar memahami apa yang saya alami. Saya merasa sangat kesepian dan terisolasi. Saya tidak tahu bagaimana cara mengatasi perasaan ini dan merasa sangat putus asa.
    #     Sekarang, saya hanya ingin tidur dan berharap bahwa besok akan menjadi hari yang lebih baik. Saya tahu bahwa saya harus mencari bantuan, tetapi rasanya sangat sulit untuk memulai. Saya harap saya dapat menemukan cara untuk merasa lebih baik dan menemukan harapan lagi.
    #     """
]


def predict_list_text(list_text):
    model = load_model()
    data = pd.DataFrame(list_text, columns=["text"])
    data["nlp_text"] = data["text"].apply(lambda x: preprocess_text(x))
    one_hot_representation = [one_hot(words, 14233) for words in data["nlp_text"]]
    embedded_docs = pad_sequences(
        one_hot_representation, padding="post", truncating="post", maxlen=1366
    )

    result = model.predict(embedded_docs)

    # result = (result >= 0.5).astype("int")
    return result


def predict_depression(text):
    list_text = [text]

    confidence_score = predict_list_text(list_text)[0][0]
    depression = confidence_score >= 0.5

    result = {
        "depression": depression,
        "confidence_score": confidence_score,
    }

    return result


# Text for testing check_depression
# text = "Saya sangat senang hari ini"
# print(predict_depression(text))
