FROM python:3.8.16-slim

# Create .venv in project directory
ENV PIPENV_VENV_IN_PROJECT=true

WORKDIR /app

COPY . .

RUN apt update -y \
    && apt upgrade -y \
    && python -m pip install --upgrade pip \
    && pip install pipenv==2023.3.20 \
    && pipenv sync \
    && apt install -y curl

CMD [ "pipenv", "run", "python", "server.py" ]
