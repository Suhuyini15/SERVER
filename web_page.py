from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_html():
    # Simple HTML content
    html_content = """
    <html>
        <head>
            <title>Simple Page</title>
        </head>
        <body>
            <h1>Hello, FastAPI</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
