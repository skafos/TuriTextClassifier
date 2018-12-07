import turicreate as tc
import save_models as sm
from skafossdk import *

ska = Skafos() # initialize skafos

# Load data
ska.log("Loading the data", labels = ['text_classifier'])
data = tc.SFrame('https://static.turi.com/datasets/regression/yelp-data.csv')

# Create a model
ska.log("Building the model", labels = ['text_classifier'])
model = tc.text_classifier.create(data, 'stars', features=['text'])

# export to coreml
ska.log("Saving the model", labels = ['text_classifier'])
coreml_model_name = "text_classifier.mlmodel"
res = model.export_coreml(coreml_model_name)

# compress the model
compressed_model_name, compressed_model = sm.compress_model(coreml_model_name)

# save to Skafos
sm.skafos_save_model(skafos = ska, model_name = compressed_model_name,
								compressed_model = compressed_model,
								permissions = 'public')