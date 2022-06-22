
from subprocess import check_output
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    stdout = check_output(['./script.sh']).decode('utf-8')
    return stdout

@app.get("/checksecrets")
def read_root():
    stdout = check_output(['./script2.sh']).decode('utf-8')
    return stdout
