# CodaSync

## Local Installation
### Create Postgresql database locally

`CREATE ROLE codabene WITH PASSWORD '1234' LOGIN;`

`CREATE DATABASE codasync OWNER codabene;`

## Design choices
Since the `StockReading` model is expected to be updated by many users at the same time, and there is also a high probability of updating the same product at the same time (Multiple requests to modify the same database row at the same time), this will result in a race condition rendering the database in an inconsistent state.

In order to avoid that, there is usually two approaches, the optimistic approach and the pessimistic approach.

The optimistic doesn't prevent the race condition from happening, as it doesn't lock the db row that is being updated, and it is not suitable for thousands of requests being issued at the same time.

That is why I decided to go for the pessimistic approach which will lock the database row using the Django method `select_for_update`.

## Scaling recommendations
### Database connections
While I tried to increase the maximum age of the DB connections in the settings, however this method has its quirks, The best solution is to implement a connection pooler for the database like `PgBouncer`, This will help set the pool size, the max clients we want to handle at any moment (default_pool_size), and the number of clients that can connect to the DB (max_client_conn). Also to make sure the max_connections param in postgres.conf file is tuned to handle the number of concurrent connections to the PostgreSQL server.

### Caching
Some tables doesn't change much, so we don't need to hit the database to get the data required each time, we can cache them instead and retrieve them from cache later.
Django has a caching framework, `Memcached` is the recommended option for caching.

After setting up the cache framework in Django, `method_decorator` can be used to with other cache decorators to decorate Django rest framework class based views.

Caching can significantly improve performance.

### Web Server optimization
In production, the application will be sitting behind a web server like Apache or Nginx, These servers can be optimized to handle high loads through altering their configurations.

### Infrastructure
Heroku enables scaling the application to run on multiple dynos on the paid plan.

But the best and recommended option is using Kubernetes.
Tools like Docker containers managed by Kubernetes helps orchestrate the containers and allow to scale (up or down) the number of nodes at run time without any down time.

### Load testing
We should load test our environment to make sure it can handle the required load/traffic.
Tools like `Locust` or `JMeter` can be used for such purposes.

### Monitoring
Setting up monitoring systems like Prometheus is good to identify performance bottlenecks.