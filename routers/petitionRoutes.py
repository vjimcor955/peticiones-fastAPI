# Petition router

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from models.Petition import Petition

router = APIRouter()

@router.get("/petition", response_class=HTMLResponse)
@router.post("/petition", response_class=HTMLResponse)
@router.options("/petition", response_class=HTMLResponse)
@router.put("/petition", response_class=HTMLResponse)
@router.patch("/petition", response_class=HTMLResponse)
@router.delete("/petition", response_class=HTMLResponse)
async def handle_petition(request: Request, petition: Petition):
    if request.method in ["POST", "PUT", "PATCH"]:
        if petition is None:
            raise HTTPException(status_code=422, detail="Petition data is required")
        data = petition.dict()
    else:
        data = None

    headers_html = "".join([f"<li>{key}: {value}</li>" for key, value in request.headers.items()])
    query_params_html = "".join([f"<li>{key}: {value}</li>" for key, value in request.query_params.items()])

    return f"""
      <html>
        <head>
            <title>FastAPI Petition</title>
        </head>
        <body>
            <h1>FastAPI Petition</h1>
            <div>
              - METODO: {request.method} <br>
              - HEADERS: <ul>{headers_html}</ul>
              - QUERY PARAMS: <ul>{query_params_html}</ul>
              - BODY: {petition.body}
            </div>
        </body>
      </html>
    """