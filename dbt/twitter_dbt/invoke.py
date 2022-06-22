
from subprocess import check_output
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    stdout = check_output(['./script.sh']).decode('utf-8')
    return stdout

@app.get("/ls")
def read_root():
    stdout = check_output(['ls']).decode('utf-8')
    return stdout

@app.get("/secrets")
def read_root():
    stdout = check_output(['ls secrets/']).decode('utf-8')
    return stdout
