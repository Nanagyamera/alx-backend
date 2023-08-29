Redis and Kue Examples

This repository contains a series of example scripts that demonstrate various concepts related to Redis, Kue, and Express.js. These examples cover tasks such as connecting to a Redis server, managing job queues, implementing job processing, and building a seat reservation system.

Contents

The repository includes the following files:

0-redis_client.js: Connects to a Redis server and logs connection status.

1-redis_op.js: Demonstrates setting and displaying values using callbacks.

2-redis_op_async.js: Converts the display function to use async/await with promisify.

4-redis_advanced_op.js: Stores a hash value using Redis hset and displays it using hgetall.

5-subscriber.js: Subscribes to a Redis channel and logs received messages.

5-publisher.js: Publishes messages to a Redis channel.

6-job_creator.js: Demonstrates creating and managing jobs using Kue queue.

6-job_processor.js: Implements job processing using the Kue queue.

7-job_creator.js: Creates jobs for a job queue and tests the job creation function.

8-job.js: Contains functions for job creation and reservation management.

9-stock.js: Implements an Express server for product listing and reservation with Redis and Kue.
