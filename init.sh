sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/django.conf /etc/gunicorn.d/test
sudo /home/box/web sudo gunicorn -b 0.0.0.0:8000 ask.wsgi