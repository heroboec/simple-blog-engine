#!/bin/bash
git pull 
sudo service gunicorn_blog restart
sudo service nginx restart