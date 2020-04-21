import cv2
from selective_search import get_candidates, add_offset
from generate_model import get_model_for_numbers
import numpy as np

class number_recognizer:

    def __init__(self):
        self.model = get_model_for_numbers("model_numbers.json","model_numbers.h5") # "model_numbers.json","model_numbers.h5

    def convertPredictionsToNumber(self, predictions):
        result = ""
        for prediction in predictions:
            if prediction < 10:
                result = result + str(prediction)
            if prediction == 11:
                result = result + "."
        if len(result)>0:
            if result.replace('.','',1).isdigit():
                return float(result)
        return None

    def getNumber(self, image):

        candidates = get_candidates(image)
        t = 0
        predictions = list()
        for candidate in candidates:

            newCandidate = candidate.reshape(1,candidate.shape[0], candidate.shape[1], 1)
            result = self.model.predict(newCandidate)
            t+=1
            prediction = np.argmax(result)
            if float(result[0][prediction])<0.8:
                continue
            name = "test" + str(t) + ".jpg"
            cv2.imwrite(name,candidate)
            predictions.append(prediction)
            np.set_printoptions(formatter={'float_kind':'{:f}'.format})
        result = self.convertPredictionsToNumber(predictions = predictions)
        return result

# nr = number_recognizer()
# image = cv2.imread("sample-data/num_sample3.png") ##sample-data/num_sample2_2.png
# print (nr.getNumber(image))



