import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

model = None

class CNNCatDogClassification():

    def __init__(self):       
        pass
    
    def load_saved_model(self):
        global model
        filepath = os.path.join("artifacts", "cnn_model.keras")
        if model is None:
            print("Model is loading")
            model = load_model(filepath)
        return model

    def predict_cateory(self, image_path):
        self.load_saved_model()
        image_size = (224,224)
        img = image.load_img(image_path, target_size=image_size)
        image_array = image.img_to_array(img)/255
        test_array = image_array.reshape((1,)+image_array.shape)
        predict_prob = model.predict(test_array)
        print("Predicted Prob :",predict_prob)
        predicted_class = "Dog" if predict_prob >= 0.5 else "Cat"
        print("Predicted Class is :",predicted_class)
        return predicted_class