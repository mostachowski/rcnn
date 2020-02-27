import cv2
from selective_search import get_candidates, add_offset
from generate_model import get_model_for_numbers

image = cv2.imread("sample-data/num_sample2.png")
candidates = get_candidates(image)

model = get_model_for_numbers("model_numbers.json","model_numbers.h5")
t = 0
for candidate in candidates:
    candidate = add_offset(candidate)
    candidate.resize((60,60,1))
    t+=1
    name = "test" + str(t) + ".jpg"
    cv2.imwrite(name,candidate)
    print(candidate.shape)




