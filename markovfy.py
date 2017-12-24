# fetch json data and add to markov chain.
import markovgen
import json

with open('data.json') as data:
    d = json.load(data)
    # print(d[0]['full_text'])
    m = markovgen.Markov()
    for tweet in d:
        try:
            tweet_text = tweet['full_text']
        except:
            break
        # print(tweet_text)
        m.feed(tweet_text)
    print(m.generate_markov_text(max_size=280, seed=None, backward=False))
# init markov chain
