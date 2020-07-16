# Objective
We have a python backend service that does vector similarity search. To understand its performance, I created this minimal demo.

# Test Code
Vector similarity search is a CPU consuming task. To simulate that case, I created a brute-force fib function.
```python
def fib(x : int) -> int:
    if x == 0:
        return 1
    if x == 1:
        return 2
    return fib(x - 1) + fib(x - 2)
```
Then created an API endpoint to calculate fib(n).

# Test Environment
Macbook 13, 2017. It takes ~10s to calculate fib(37).

# Tests
1. Debug Server
```sh
./manage.py runserver
```
Then query 4 times with:
```sh
curl -o /dev/null http://127.0.0.1:8000/fib\?n\=37\&format\=json
```
All the requests finished in about 40s
  
2. Daphne
```sh
	daphne tutorial.asgi:application
```
Then query 4 times with:

```sh
curl -o /dev/null http://127.0.0.1:8000/fib\?n\=37\&format\=json
```

All the requests finished in about 40s

3. Gunicorn
```sh
gunicorn -w 4 -k uvicorn.workers.UvicornWorker tutorial.asgi:application
```
Then query 4 times with:
```sh
curl -o /dev/null http://127.0.0.1:8000/fib\?n\=37\&format\=json
```

Although we specified workers = 4, nothing actually changed. All the requests finished in about 40s.

4. Uvicorn
```sh
uvicorn tutorial.asgi:application --workers 4
```
Then query 4 times with:
```sh
curl -o /dev/null http://127.0.0.1:8000/fib\?n\=37\&format\=json
```

Although we specified workers = 4, nothing actually changed. All the requests finished in about 40s.

5. Start two servers
```sh
daphne tutorial.asgi:application -p 8000 && daphne tutorial.asgi:application -p 8001
```
Then query 4 times with
```sh
curl -o /dev/null http://127.0.0.1:8000/fib\?n\=37\&format\=json
curl -o /dev/null http://127.0.0.1:8000/fib\?n\=37\&format\=json
curl -o /dev/null http://127.0.0.1:8001/fib\?n\=37\&format\=json
curl -o /dev/null http://127.0.0.1:8001/fib\?n\=37\&format\=json
```
4 queries ends together around 20s.
