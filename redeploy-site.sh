#!/bin/bash

cd amber-web
git fetch && git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

# source python3-virtualenv/bin/activate
# pip install -r requirements.txt
# systemctl daemon-reload
# systemctl restart myportfolio
