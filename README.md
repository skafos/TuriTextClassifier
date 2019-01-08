# Turi Text Classifier

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training a text classifier model on Skafos using the Turi Create framework. As much as possible, the code in this repo mimicks Turi Create's text classifier example which can be found [here](https://apple.github.io/turicreate/docs/userguide/text_classifier/). 

## What is here?

The main components of this repo are:
- `text_classifier.ipynb` - a python notebook that trains and saves a sentiment classifier model
- `metis.config.yml` - a file telling Skafos how to execute the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `utilities/` - a helper module with functions to load data and save the core ml model to Skafos
- `userguide/` - a module that contains more examples, tips, and documentation


## Further notes:
- The data for this example is Yelp review data that comes from Turi Create's own static data sets and can be found [here](https://static.turi.com/datasets/regression/yelp-data.csv)
- Note this job takes about 15 minutes to run locally using CPU. To decrease this run time, you can ask Skafos for more resources if you deploy this job to Skafos. To read more about this, check out [Metis Machine's documentation](https://docs.metismachine.io/docs/jobs-1)

## Going beyond the example:
- If you wish to incorporate your own data, check out `userguide/
text_in_turicreate.ipynb`
- If you wish to try another type of text classificaiton model, check out `userguide/spam_classification.ipynb`
- Turi Create has built-in model evaluation and prediction techniques. We've included some of the functions below but for more detailed description, refer to Turi Create's [documentation](https://apple.github.io/turicreate/docs/userguide/image_similarity/).

#### Predicting New Text
In `text_in_turicreate.ipynb`, we've included some code to show you how to make predictions once you've trained a text classification model.  

```python
# predict a bad review, returns 2
model.predict(tc.SFrame({'review' : ['This product didnt meet expectations']}))

# predict a good review, returns 5
model.predict(tc.SFrame({'review' : ['This product far exceeded my expectations']}))
```