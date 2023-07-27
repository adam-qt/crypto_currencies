FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#ENV PATH "/usr/local/bin:$PATH"

WORKDIR /crypto
COPY . .

RUN pip install --upgrade pip
RUN pip install -r ./req.txt
RUN chmod +x /crypto/start_app.sh
EXPOSE 8000

CMD ["sh","/crypto/start_app.sh"]
