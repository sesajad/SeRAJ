FROM python3
RUN pip3 install django
RUN pip3 install django-crispy-forms
RUN python3 manage.py migrate
RUN python3 manage.py createsuperuser
CMD python3 manage.py runserver
