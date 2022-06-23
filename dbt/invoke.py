
from subprocess import check_output
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse 


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    stdout = check_output(['./script_run.sh']).decode('utf-8')
    return f"""<html>
                <h3>DBT Run response</h3>
                <pre>{stdout}</pre>
            </html>"""

@app.get("/dbtdoc")
def read_root():
    stdout = check_output(['./script_doc.sh']).decode('utf-8')
    
    if stdout:        
        search_str = 'o=[i("manifest","manifest.json"+t),i("catalog","catalog.json"+t)]'

        with open('twitter_dbt/target/index.html', 'r') as f:
            content_index = f.read()
            
        with open('twitter_dbt/target/manifest.json', 'r') as f:
            json_manifest = json.loads(f.read())

        with open('twitter_dbt/target/catalog.json', 'r') as f:
            json_catalog = json.loads(f.read())
            
        with open('twitter_dbt/target/index2.html', 'w') as f:
            new_str = "o=[{label: 'manifest', data: "+json.dumps(json_manifest)+"},{label: 'catalog', data: "+json.dumps(json_catalog)+"}]"
            new_content = content_index.replace(search_str, new_str)
            f.write(new_content)
        
        return FileResponse('twitter_dbt/target/index2.html') 
    
    return "<html>Ops, something wrong happens</html>" 
