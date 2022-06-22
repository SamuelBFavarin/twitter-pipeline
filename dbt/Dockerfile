FROM fishtownanalytics/dbt:0.19.2
FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . ./ 

RUN chmod 777 script.sh
RUN chmod 777 script2.sh

CMD ["uvicorn", "invoke:app", "--host", "0.0.0.0", "--port", "8080"]
