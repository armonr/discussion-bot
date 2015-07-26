Discussion Fact Bot
====================

A conversation simulating bot tailored for Wikia discussion.

Provided a Wikia discussion post data, discussion bot aims to provide a relevant fact as a post reply.


Usage
======

1. `python run.py`
2. POST to localhost:5500/dis_reply with JSON data

    ```{"text":"THE POST CONTENT TO REPLY TO",
    "siteId":"THE ID OF THE SITE (WIKIA)",
    "threadId":12345678,
    "userId":1234}```
