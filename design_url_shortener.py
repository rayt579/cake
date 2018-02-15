'''
Design a URL shortener.

Like bit.ly


1) What is the URL shortener?
    - Think of it as a service that provides users with a shortened web app.

2) What are the features?
    - Full web app, with a web interface?
    - If API, do we need authentication or user accounts or developer keys?
    - Can people modify or delete links?
    - If people can't delete links, do they persist forever? Should we have a retention policy?
    - Should be people be able to choose their shortlinks?
    - Should we support market analytics, on everyone that clicks on the link?

3) What are the design goals?
    - We should be able to support a lot of links => scale
    - We need the shortlinks to be as short as possible
    - Following a shortlink should be fast
    - The shortlink follower should be resilient to load spikes. It might be the top story on reddit.

4) Building the data model.
    - We need a link, which maps a short_link on our site to a long_link, where we redirect people who visit short_link

    Link
    - short_link
    - long_link

    to maek things more readable,

    ShortLink
    - slug
    - destination

'''



