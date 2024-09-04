# указываем какой начальный образ будет использован - в данном случае образ python 3.9
FROM python:3.9-slim

# переходим в каталог /usr/src/app (нужные пути сами создадутся)
WORKDIR /usr/src/app

# копируем файл из данной папки в контейнер
COPY app.py .

# устанавливаем пакет psycopg2-binary, который используется для связи с postgres
RUN pip install psycopg2-binary

# выполняем запуск файла при старте контейнера
CMD ["python", "app.py"]