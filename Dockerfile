# 
FROM python:3.10
# 
RUN pip install pipenv
# 
WORKDIR /code

# 
# COPY ./requirements.txt /code/requirements.txt
COPY ./app/Pipfile ./app/Pipfile.lock /code/
# 
RUN  pipenv install --system --deploy

# 
COPY /app /code/app

# 
CMD ["python", "./app/main.py" ]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]