# symmetrical-disco
I wanted to build a markov chain that was fed trump's tweets and would be able to have a nice GUI. This is what I came up with in a few days, I've come accross some challenges and I have done a lot of reading. There's something fishy about the markov chain since it's repeating a lot about Saudi Arabia. The html needs to get changed to something more aesthetic. 

Update: I'm opening this up to anyone who wants it. 
You'll have to install Flask (pip install flask)
You'll also need markovfy (pip install markovfy)
Then you can run the server using Flask!

I was trying to figure out how to deploy this on the UTCS machines but it looks like they have restrictions that won't allow me to display dynamic content (using AJAX requests, using Flask) (or it's extremely complicated)

Future goals for this project:

- The hardest part was actually trying to get everything into a web gui. I want to deploy it if I get to have my own domain at one point (or maybe figure out how to do it in the UT CS machines). 

- There are still some improvements that can be made to the markov chain (I know trump only tweets from an android so we can easily sort those tweets and ignore the other tweets his staff made) 

- it's UGLY! I really want some CSS to spice it up. 

- !!! There's so much more that can be done. We could make it get passed in a JSON file and have it build another markov chain of whatever data it is given. We could make the font color crayons. There's so much more to do. 


Anyways all help is welcome. Thanks for checking this out. 



