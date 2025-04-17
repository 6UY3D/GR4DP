import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from gr4dp.ui.chat_manager import ChatManager

app = FastAPI()
templates = Jinja2Templates(directory="gr4dp/ui/templates")

chat_manager = ChatManager()

@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
def chat_endpoint(message: str = Form(...)):
    response = chat_manager.process_user_message(message)
    return {"response": response}

def start_ui(host="0.0.0.0", port=8000):
    uvicorn.run(app, host=host, port=port)
