import requests, zipfile, io


def load_spam_dataset():
    spam_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'
    _request_and_unzip(spam_url, 'spam/')
    with open("datasets/spam/SMSSpamCollection", "r", encoding="utf-8") as infile:
        d = infile.readlines()
    return d

def _request_and_unzip(url, folder):
    r = requests.get(url)
    if r.ok:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(f'datasets/{folder}')
