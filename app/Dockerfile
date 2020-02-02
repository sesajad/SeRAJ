FROM docker.xaas.ir/python
EXPOSE 8000
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD ./ /app/
WORKDIR /app/
RUN python3 manage.py migrate
RUN python3 manage.py createsuperuser
CMD gunicorn -b 0.0.0.0:8000 SeRAJ.wsgi
