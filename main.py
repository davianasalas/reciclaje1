import email
from msilib.schema import Error
from multiprocessing import connection
from sqlite3 import Cursor
from fastapi import *
from fastapi.templating import*
from fastapi.staticfiles import*
import mysql.connector
import uvicorn 
from funcion_insertar import *
templates = Jinja2Templates(directory="D:\servidoradri\ServidorWeb\static")
app=APIRouter()#Crear una instancia de fastapi
#configurar la instancia de fastapi con el director
app.mount("/static", StaticFiles(directory=r"D:/servidoradri/ServidorWeb/static"),name="static")

@app.get("/")#RUTA O ENDPOINT
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/registrar")
def form_post(request: Request, fn: str = Form(...), ap: str = Form (...),  em: str = Form (...), pas: str = Form (...)):
    print(fn)
    print(ap)     
    print(em)
    print(pas)
    print("esta es la ruta registro")
    insertar_variables_registro(fn,ap,em,pas)
    return templates.TemplateResponse("index.html",{"request":request})


if __name__=='__main__':
    print("Método Principal aqui inicia la ejecución")
    uvicorn.run(app, host="localhost", port=1111)
