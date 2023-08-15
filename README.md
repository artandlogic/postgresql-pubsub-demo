# postgresql-pubsub-demo

This repo holds code to be used in conjunction with the A+L blog post,
[Using PostgreSQL for Pub/Sub](https://artandlogic.com/blog/), a
tutorial on PostgreSQL's little known pub/sub feature.  It
demonstrates how, if you're already using PostgreSQL, you have a
pub/sub engine which you can use in your asynchronous applications.

In this repo:

* `demo.sql` - database schema with initial data inserted.  The
  tutorial describes how to launch a PostgreSQL docker container that
  loads this schema.

* `demo.py` - A simple python asynchronous application which
  establishes a connection to the running postgres datbase and listens
  for publications.  The tutorial describes how to install the
  necessary virtualenv and run the application.


Check out the [A+L blog](https://artandlogic.com/blog/) for posts on a
wide array of topics!
