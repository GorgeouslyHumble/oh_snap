oh_snap
=======

A small project that consumes Snapguide's API.

It will, initially, be a simple web application that displays a leaderboard of what supplies are popular with recent guides.

Stack:
=======
Flask as the web framework.
RQ (Redis Queue) will handle queueing.
Requests and Simplejson for talking to the API.
Redis and Redisco handles the storing and retrieving of API responses.
Will use Pyyco when the application reaches v1.0.0 and I've proof-read my documentation.

Done:
======
1. Write a module to communicate with Snapguide's API.
2. Write a data storage layer to take store the API responses.
3. Get Flask set up so that it renders pages.
4. Begin work on an API.

To-Do:
======
1. Find a good testing framework and write unit tests for my code / move into a TDD kind of work flow.
2. Write documentation on how the service works. Particularly around Redisco.
3. Write the front-end.
4. Write the logic for sorting supplies based on popularity.
5. Document the API.
6. Better implement SemVer into my development work flow.

In Progress:
======
1. Testing the data storage layer to see how well it works.
2. Reading documentation on how to do TDD with Python and Flask and do it well.
3. Evaluating whether or not it will be better to use Couchbase for storage rather than Redis.
4. Implementing queueing for API requests/storage so things aren't so darn slow.
5. Making my service web scale!!!!one1one!!

