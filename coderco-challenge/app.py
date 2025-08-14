from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Redis connection settings
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def welcome():
    # Show welcome page
    return render_template("welcome-page.html")

@app.route("/count")
def count():
    # Increment the visit counter in Redis
    visits = r.incr("visits")
    return render_template("count.html", count=visits)

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5002)
