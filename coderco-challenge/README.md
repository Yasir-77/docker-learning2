# CoderCo Containers Challenge Solution — Multi-Container Flask + Redis App

A simple multi-container application that serves a Flask web app fronted by Nginx and backed by Redis.
The app renders a welcome page (/) and a counter page (/count) that increments a visit counter stored in Redis.

## 🧩 What’s inside

- Flask (web) — Python app with two routes:
  - / → Welcome page
  - /count → Increments & displays a visit counter (Redis key: visits)
- Redis (redis) — Key-value store that persists the visit count
- Nginx (nginx) — Reverse proxy exposing the app on localhost:5002
- Docker Compose — Orchestrates the services & wiring

## ⚒️ Breakdown of whats inside each file 

### [app.py](https://github.com/Yasir-77/docker-learning2/blob/main/coderco-challenge/app.py)

#### Flask (`web`)
- Python Flask application.
- Has two routes:
  - `/` → displays a welcome page.
  - `/count` → increments and shows a counter stored in Redis.
- Connects to Redis using environment variables (`REDIS_HOST`, `REDIS_PORT`).
- Runs on port **5002** inside the container.



#### Redis (`redis`)
- In-memory key-value database.
- Stores the visit count under the key `visits`.
- Data is persisted using a Docker volume (`redis-data`).
- Exposed on port **6379**.



#### Nginx (`nginx`)
- Acts as a reverse proxy for the Flask app.
- Listens on host port **5002** (`localhost:5002`).
- Forwards requests to the Flask container (`web:5002`).
- Makes it possible to scale multiple Flask instances and load balance traffic.

---

### [Dockerfile](https://github.com/Yasir-77/docker-learning2/blob/main/coderco-challenge/Dockerfile)
- Defines how the Flask image is built:
  - Starts from a lightweight Python 3.8 base image.
  - Sets working directory to `/app`.
  - Copies project files into the container.
  - Installs Flask and Redis Python libraries.
  - Exposes port 5002.
  - Runs the app with `python app.py`.

---

### [docker-compose.yml](https://github.com/Yasir-77/docker-learning2/blob/main/coderco-challenge/docker-compose.yml)
- Orchestrates all services together.
- **Web service (Flask)**:
  - Built from the Dockerfile.
  - Depends on Redis.
  - Reads Redis host/port from environment variables.
- **Redis service**:
  - Uses the official Redis image.
  - Persists data with a volume (`redis-data:/data`).
- **Nginx service**:
  - Uses the official Nginx image.
  - Mounts a custom `nginx.conf`.
  - Exposes the app on host port 5002.

---

### [nginx.conf](https://github.com/Yasir-77/docker-learning2/blob/main/coderco-challenge/nginx.conf)
- Defines proxy rules for Nginx.
- Creates an upstream called `flask_app` pointing to `web:5002`.
- Listens on port 5002.
- Proxies all requests (`/`) to the Flask app.

---

### [Templates (`welcome-page.html` & `count.html`)](https://github.com/Yasir-77/docker-learning2/tree/main/coderco-challenge/templates)
- **welcome-page.html**:
  - Displays a welcome message.
  - Provides a button to check the visit counter.
- **count.html**:
  - Shows the current number of visits.
  - Provides a button to return to the home page.
