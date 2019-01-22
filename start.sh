#!/usr/bin/env bash
echo 'SEARCH_TEXT='$1 > search.env
sudo docker-compose up --abort-on-container-exit