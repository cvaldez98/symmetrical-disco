# fetch json data and add to markov chain.
import markovgen
import json
class markov(object):
    def __init__(self):
        with open('data.json') as data:
            d = json.load(data)
            # print(d[0]['full_text'])
            self.m = markovgen.Markov()
            for tweet in d:
                try:
                    tweet_text = tweet['full_text']
                except:
                    pass # some tweets might not have full_text attributes
                # print(tweet_text)
                self.m.feed(tweet_text)

    def getText(self):
        return self.m.generate_markov_text(max_size=280, seed=None, backward=False)
