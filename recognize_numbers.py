import cv2
from selective_search import get_candidates, add_offset
from generate_model import get_model_for_numbers
import numpy as np

image = cv2.imread("sample-data/num_sample1.png") ##sample-data/num_sample2_2.png
candidates = get_candidates(image)

model = get_model_for_numbers("model_numbers.json","model_numbers.h5") # "model_numbers.json","model_numbers.h5"
t = 0
for candidate in candidates:

    newCandidate = candidate.reshape(1,candidate.shape[0], candidate.shape[1], 1)
    result = model.predict(newCandidate)
    t+=1
    name = "test" + str(t) + ".jpg"
    cv2.imwrite(name,candidate)
    print("candidate ", t, ": ",np.argmax(result))
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    # print(result)




