# Turi Text Classifier

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com._

The following repo contains code for training an text classifier model on Skafos using the Turi Create framework. As much as possible, the code in this repo mimicks Turi Create's text classifier example which can be found [here](https://apple.github.io/turicreate/docs/userguide/text_classifier/). 

## What is here?

The two main components to this repo are:
- `text_classifier.py` - a Skafos job that trains a text classifier model and saves a core ml model
- `text_classifier.ipynb` - a python notebook with the same code as the above `text_classifier.py` job.

Additionallly, there exist:
- `metis.config.yml` - a file telling Skafos how the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `save_models.py` - a helper module to save the core ml model to Skafos

## Further notes:
- The data for this example is Yelp review data that comes from Turi Create's own static data sets and can be found [here](https://static.turi.com/datasets/regression/yelp-data.csv)
- Note this model can take a while to run depending on the dataset you are training with. For the example data, this takes about 15 minutes to run. This model does not leverage GPU's but runtime can be decreased by increasing requested resources on Skafos. To see how this is done, check out our [documentation](https://docs.metismachine.io/docs/jobs-1).
