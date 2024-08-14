from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    visit_count = r.incr('visit_count')
    return f"Visit count: {visit_count}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
