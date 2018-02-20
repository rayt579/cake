'''
Design a URL shortener.

Like bit.ly


1) What is the URL shortener?
    - Think of it as a service that provides users with a shortened web app.

2) What are the features? (get clarification from interviewer)
    - Full web app, with a web interface?
    - If API, do we need authentication or user accounts or developer keys?
    - Can people modify or delete links?
    - If people can't delete links, do they persist forever? Should we have a retention policy?
    - Should be people be able to choose their shortlinks?
    - Should we support market analytics, on everyone that clicks on the link?

3) What are the design goals (What are we optimizing for)?
    - We should be able to support a lot of links for all of our users => scale
    - We need the shortlinks to be as short as possible
    - Following a shortlink should be fast
    - The shortlink follower should be resilient to load spikes. It might be the top story on reddit.

4) Building the data model.
    - We need a link, which maps a short_link on our site to a long_link, where we redirect people who visit short_link

    Link
    - short_link
    - long_link

    to make things more readable,

    ShortLink
    - slug
    - destination

5) Views/Pages/Endpoints (skeleton code)
    - First's let's make a way to create a ShortLink
    - Let's make a REST-style API.
        We'll define a creation endpoint:
            ca.ke/api/v1/shortlink

        The response will contain the newly-created ShortLink, with its slug and destination.

        To create a new ShortLink, we'll issue a POST request there. Our POST request will include one required
        argument: the destination where our ShortLink will point. It'll also take optional slug argument, and
        generate if not provided.

        ex. curl --data '{"destionation": "interviewcake.com"}' https://ca.ke/api/v1/shortlink
        {
            "slug":"ae8uFt"
            "destination": "interviewcake.com"
        }


        We'll reject non-POST requests with error 501 for now.
        Our endpoint will look like this:

            def shortlink(request):
                if request['method'] is not 'POST':
                    return Response(501)

                destination = request['data']['destination']

                # if they included a slug, use that
                if 'slug' in request['data']:
                    slug = request['data']['slug']
                else:
                    slug = generate_random_slug()

                DB.insert({'slug':slug, 'destination':destination})

                response_body = {'slug':slug, 'destination':destination}
                return Response(200, json.dumps(response_body))


        Keep in mind that the method to generate_random_slug() is tricky:
            - What characters can we use in randomly generated slugs. What characters are allowed in URLs?
            - How do we ensure a randomly generated slug hasn't already been used? If there is collision,
                how to handle it?

    - Let's make a way to follow a ShortLink
        We will give our short link this format: ca.ke/$slug
        You could make it a redirect endpoint by using a format like ca.ke/r/$slug, but adds 2 char of length
        to the shortlink.

        - One thing to keep in mind: when we build the webapp for our service, we want to differentiate our page
          from other shortlinks (no slug with /about). We could reserve a set of shortlinks for pages, or
          prefix our pages: ca.ke/w/about

        def redirect(request):
            destination = DB.get({'slug':request['path']})['destination']
            return Response(302, destination)


6) Greater Detail: How to handle slug generation? Slug length, allowed characters, and how to handle slug collisions.
    - What are we optimizing for?
    1) We should be able to store a lot of links
    2) Our shortlinks should be as short as possible

    How many links do we need??

    - If we allow c different characters, for n-character slugs we have c^n distinct possibilities.

    - If we are trying to accomodate as many slugs as possible, we should allow as many characters as we can.
        1) Figure out the max set of characters we can allow in random shortlinks
        2) Figure out how many distinct shortlinks we want to accommodate
        3) Figure out how long our shortlinks must be to accommodate that many distinct possibilities

    What are the constraints on c?
    1) We should only use characters that are allowed in URLs
    2) We should only pick chacracters that are easy to type on a keyboard (use case where people enter from keyboard)

    How to address #1? -> Google Search, Request for Comments.
        - Domains are not case-sensitive, but the path portion of a URL is. So you need to treat lowercase separate from
          uppercase.

    Decision: The set of allowed characters is A-Z, a - z, 0-9. Let's not use special characters like "$-_.+!*()." for
    the sake of addressing easy to type.

    26 + 26 + 10 = 62 possible characters

    Note: In the user experience, you will have to accomodate for fonts (ambiguity between lowercase l and 1)


    How many distinct slugs do we need?
    How many slugs per minute? Let's say 100,000 new slugs generated per min.
    100000 * 60 * 24 => 145 million new slugs per day. 52.5 billion per year. For 100 years, that's 5.2 trillion slugs.
    Let's say we need 5.2 trillion distinct slugs.


    How short can we make our slugs while still getting enough distinct possibilities?
        Solve for 62 ^ n = 5 trillion. n = 7.09

    We'll use 7-length slugs.

    How about support for slugs that are less than 7-length?
        62 ^ 6 + 62 ^ 5 + 62 ^ 4 + 62 ^ 3 + 62 ^ 2 + 62 = 57 billion.

        For now let's just keep random slugs at 7 length. Note how 57 billion to 5 trillion going from 62 ^ 6 to 62 ^ 7.

7) Even more detail: How do we generate a random slug?

    We could just make a random choice for each character

    def generate_random_slug():
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        num_char = 7
        return ''.join([random.choice(alphabet) for _ in xrange(num_char)])

    How to ensure that slugs are unique?
    1) Reroll (retry) when we hit an already-used slug
    2) Adjust the slug generation strategy to only ever give us unclaimed slugs

    As you get more slugs in your database, you will find more collisions. At capacity 3/4, you can expect to reroll 4 times.
    Come up with a strategy to use for option 2.


    Use base conversion to generate random slugs.
    - Think of each of our possible "random" slugs as a unique number, expressed in base 62.

    def generate_random_slug():
        global current_random_slug_id
        slug = base_conversion(current_random_slug_id, base_62_alphabet)
        current_random_slug_id += 1
        return slug

    We can store the current_random_slug_id in our webserver, and make it persistent even if the webserver crashes.
    ex. Convert 125 to base-62
        62 ^ 1 * 2 + 62 ^ 0 = 125
        so 21 is base-62 of 125

    One potential issue: slugs may have an id shorter than 7 digits in base-62.
        a) Pad the slugs with 0s to be exactly 7 digits
        b) Function converts slugs back to numbers doesn't choke when the slug is less than 7 characters

    Another issue: User can select a slug that matches the URL. When this happens, you should just iterate
    the global_current_random_slug_id.

    def generate_random_slug():
        global current_random_slug_id
        while True:
            slug = base_conversion(current_random_slug_id, base62_alphabet)
            existing = DB.get({'slug':slug})
            if not existing:
                return slug

    You've tacked 1) and 2) of the design goals. Two left! Latency, and load balancing?
    1) We should be able to store a lot of links
    2) Our shortlinks should be as short as possible
    3) Following a shortlink should be fast
    4) The shortlink follower should be resilient to laod spikes.

7) How do we scale our link follower to be fast for read/writes.
- DB to be read to get the destination for the given slug is going to be the first bottleneck.
    - In general databse operations usually bottleneck before business logic.

- What kind of database should we use to store the shortlinks? -> SQL, NOSQL.
    - SQL: good for performing complex queries using joins, good if planning to look at releationships between things
    - NoSQL: faster for writes and simple key-value reads.

    We probably don't need to do relational queries, so let's go with a NoSQL DB
    * Also consider adding an abstraction layer to decouple the DB from the model

- How to unbottleneck database reads?
    You must make sure that you are indexing the right way

    Your should make the key for each row in the ShortLink table be the slug.
        * Note: If you used RDBMS, you could use the global current_random_slug_id as the auto-incrementing index, but you
        would need to handle the user generated slugs.

- How else to speed up reads?
    Implement as much data in-memory as possible to avoid disc seeks. This becomes very important if one of the links
    get a heavy load of requests (front page of Reddit). Have the redirect link (destination) in memory to process quickly.
        Depending on the database we use, it might already have an in-memory cache system.

    We could additionally add our own cacheing layer, using memcached.
        This adds complexity, as you have to maintain two sources of truth the DB and the cache layer.
        You need to push edits to both the database and the cache, it could slow down reads if you get a lot of cache misses.

        1) Cache eviction strategy: What to do once our cache is full? LRU (least recently used)
        2) Sharding strategy: sharding the cache lets you store more things in memory, because you can horizontally scale.
            You can decide what goes into which shard using a hash and mod strategy.
            But how do you add or remove a shard without causing an unmanageable spike in cache misses?

    It might be a better idea to shard the DB instead of, or in addition to caching. If the database has a built-in
    memory cache, sharding the DB would allow to keep more data in working memory without additional cacheing layer.

    Adding and removing database/cache shards can be painful, because you will have to migrate your schema without downtime.

    Cassandra offers sharding systems built in.

8) How to be resilient to load spikes?
- Have multiple webserver workers, and put them behind a load balancer.that distributes incoming requests among the workers.
    More web servers will add more complexity to the database and caching layers
    you will need to handle multiple connections to the webservers.


There are a bunch more directions to go with this:
    1) Split creation endpoint across multiple workers. How do you stay in sync about what current_random_slug_id?
    2) Uptime and (Single Point of Failure) SPOF are common concerns. How to make sure that a single machine won't bring
    down the whole system.
    3) Analytics. What if you want to provide users with information of the links they've created. What analytics would
    you show, and where can you store and display them.
    4) Editing and deleting. How would you add edit and delete features?
    5) Optimizing for implementation time. You built a machine for scale, but how would you get an MVP off the ground.
'''
