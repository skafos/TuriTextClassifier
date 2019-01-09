# Turi Text Classifier

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training a text classifier model on Skafos using the [Turi Create framework](https://apple.github.io/turicreate/docs/userguide/text_classifier/). 

## What is here?
The main components of this repo are:
-  `sentiment_classifier.ipynb` - a python notebook that trains and saves a sentiment classifier model, START HERE!
-  `utilities/` - a helper module with functions to load data and save the core ml model to Skafos
-  `advanced_usage/` - a module that contains more examples, tips, and documentation
-  `requirements.txt` - a file describing all required python dependencies

## About the model
-  The sentiment classifier is trained on [Yelp review data](https://static.turi.com/datasets/regression/yelp-data.csv).
-  Once trained, you can feed the model a snippet of text, and it will predict a sentiment score between 1-5.
    -  A score of 1 means that the text is *negative* in nature.
    -  A score of 5 means that the text is *positive* in nature.  
-  The model takes about 15 minutes to train in the JupyterLab session on CPUs. To decrease this run time, you can deploy as a job and ask Skafos for more resources. To read more about this, check out [Skafos Jobs documentation](https://docs.metismachine.io/docs/jobs-1)

### Predicting new text
In `advanced_usage/text_in_turicreate.ipynb`, we've included some code to show you how to make predictions once you've trained a sentiment classification model by simply calling the `.predict()` method.

```python
# predict a bad review, returns 2
model.predict(tc.SFrame({'review' : ['This product didnt meet expectations']})) 

# predict a good review, returns 5
model.predict(tc.SFrame({'review' : ['This product far exceeded my expectations']}))
```

## Going beyond the example
- If you wish to incorporate your own data or try another type of text classification model, check out the `advanced_usage/` section.
- Turi Create has built-in model evaluation and prediction techniques. We use some of the functions  int he `advanced_usage/` section, but for more detailed description, refer to Turi Create's [documentation](https://apple.github.io/turicreate/docs/userguide/image_similarity/)


## Need Help?
Please contact us with questions or feedback! Here are two ways:


-  [**Signup for our Slack Channel**](https://metismachine-skafos.slack.com/join/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos) 

Also checkout Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/text_classifier/) on text classification basics.