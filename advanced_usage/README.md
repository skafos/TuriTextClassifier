# Text Classifier Advanced Usage
The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building Text Classification Models.

## Tips And "Gotchas"

-  **Training Data**: The training data used for the sentiment classifier consists of raw text from user reviews on Yelp, paired with a sentiment score (1-5). Don't expect the model to predict the topic of text out of the box unless you change the underlying training data.
    -  **Key Point:** When you train a model, the nature of the training data directly influences the model's ability to make predictions and the types predictions it generates.
 -  **Common Text Classification Tasks**:
     -  ***Sentiment Classification***: How positive or negative is a piece of text? Typically trained with text data representing user reviews and respective ratings on a scale 1-5. The starter model in this repo contains a basic sentiment classifier trained on yelp reviews.
    -  ***Spam Classification***: How likely is it that a piece of text is "spam" or 100% valid? Typically trained with text data paired with the appropriate label (spam or ham). 
    -  ***Topic Identification***: What is the topic or subject matter of a piece of text? Typically trained with text data paired with related categories.
- **Wrangling Text w/ Turi Create**: Text comes in a host of different formats. Fortunately, the Turi Create text classifier handles all cleaning, [tokenization](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html), and text feature engineering, and cleaning of your text data automatically.

## Resources

-  `text_in_turicreate.ipynb`: Gives some tips on adapting your text classifier to a **NEW** set of data, detailing proper formatting and several helper functions.
-  `spam_classifier.ipynb`: Ready to try something other than sentiment classification? Try out spam classification and wrangle a new external data source. By the end, you will have trained a different text classifier and evaluated the model's performance on a holdout test set.

## Need Help?
Didn't find something you need? Confused by something? Need more guidance?

Please contact us with questions or feedback! Here are two ways:

-  [**Signup for our Slack Channel**](https://metismachine-skafos.slack.com/join/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos)

Also checkout Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/text_classifier/) on text classification basics.
