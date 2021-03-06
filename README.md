# Turi Text Classifier

**DEPRECATION WARNING**

This code example was intended for use by the legacy Skafos platform and is no longer being maintained. On 05/29/2019, a new version of [Skafos](https://skafos.ai) was released, streamlining model delivery to the edge.

[Sign-up](https://dashboard.skafos.ai/sign-up) for an account, [join](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI) our Slack community, and explore some [example models](https://github.com/skafos/colab-example-models) to get started.

---

The following repo contains code for training a text classifier model on Skafos using the [Turi Create framework](https://apple.github.io/turicreate/docs/userguide/text_classifier/). The example model is based on user reviews from Yelp, and given a new sentence, will predict the user's sentiment (negative or positve on a scale from 1-5).

## What is here?
The components of this repo are:
-  `text_classifier.ipynb` - a Python notebook that trains and saves a sentiment classifier model to use in your app. Start here.
-  `utilities/` - a directory that contains helper functions used by `text_classifier.ipynb`.
-  `advanced_usage/` - a directory that contains additional information about this text classification model, how to incorporate your own data, advanced usage, and additional example models.
-  `requirements.txt` - a file describing all required Python dependencies.

## About the model
-  The text classifier is trained on [Yelp review data](https://static.turi.com/datasets/regression/yelp-data.csv).
-  Once trained, you can give the model a snippet of text, and it will predict a sentiment score between 1-5.
    -  A score of 1 means that the text is *negative* in nature.
    -  A score of 5 means that the text is *positive* in nature.  
-  The model takes about 15 minutes to train in the JupyterLab session on CPUs. To decrease this run time, you can deploy as a job and ask Skafos for more resources. To read more about this, check out [Skafos Jobs documentation](https://docs.metismachine.io/docs/jobs-1).

## Going beyond the example
- If you wish to incorporate your own data or try another type of text classification model, check out the `advanced_usage/` section.
- Turi Create has built-in model evaluation and prediction techniques. We use some of the functions  in the `advanced_usage/` section, but for a more detailed description, refer to Turi Create's [documentation](https://apple.github.io/turicreate/docs/api/turicreate.toolkits.evaluation.html).


## Need Help?
Please contact us with questions or feedback! Here are two ways:


-  [**Signup for our Slack Channel**](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos) 

Also checkout Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/text_classifier/) on text classification basics.
