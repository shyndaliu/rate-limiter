# Flower API rate limiting

Microservice is written on FastAPI, has rate limitter in middleware level which allows service block requests

## Approach:
✅ ability to block too much requests form certain user by IP
👎 doesn't consider spike of requests in general
👎 can take too much memory
👎 no shared memory in case of distributed system 
❓ possible solution: change config, doesn't save bucket by unique id, instead just save bucket, add some caching like Redis

## Algorithm:
token bucket rate limiting

## Configuration:
- capacity: 3 tokens
- refilling: 1 token/s

## How to run:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
