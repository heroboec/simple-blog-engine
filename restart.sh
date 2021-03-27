#!/bin/bash
git pull 
sudo gunicorn_blog restart
sudo nginx restart