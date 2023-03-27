# Flask with crontab

This project is the Proof of Concept that web service having crontab feature.  
The process is a server that listens for HTTP requests, but is also a worker that periodically performs tasks.  
By implementing this worker instead of using the OS crontab, you get a crontab that has the same life cycle as the web service.  
It may be easier to operate on monolithic servers.

- The web service and worker are running in the separate thread
- Cron expressions are evaluated every second and `CronTask` is started in a new process when the condition is met
- The configs of `CronTask` are written in [settings/settings.json](./settings/settings.json) as `CronTaskOptions` property

# How to run it

## Docker (or Docker Compose)

The quickest and easiest way is to use Docker.  
You can check whether `CronTask` has worked by watching logs.  
Also, the web service is listening, open http://localhost:5000 in browser.

The following is a reference procedure.

```bash
# Build and Run
docker build -t flask-with-cron-worker:latest .
docker run --name flask_with_cron_worker -d -p 5000:5000 flask-with-cron-worker:latest

# Watch logs
docker logs -f flask_with_cron_worker

# Clean
docker stop flask_with_cron_worker && docker rm flask_with_cron_worker
```

or

```bash
# Build and Run
docker-compose up -d --build

# Watch logs
docker-compose logs -f flask_with_cron_worker

# Clean
docker-compose down
```

## Python 3.8 and pipenv

If Python version is 3.8.x, you can also easily do this with `pipenv`.

```bash
# Execute this if pipenv does not installed
pip install pipenv

# Download required packages using pipenv
bash setup.sh

# Run
pipenv run python server.py
```

## Others

Create .venv/ and install packages by manual.  
Required packages are written in [Pipfile](./Pipfile) as [packages].

```bash
# Create and load virtualenv
python -m venv .venv/
source .venv/bin/activate

# Install packages
python -m pip install --upgrade pip
pip install flask==2.2.3 crontab==1.0.0

# Run
python server.py
```
