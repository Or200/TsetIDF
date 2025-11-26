from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import csv, codecs
from db.load_csv import load_csv_into_db
import os


app = FastAPI()

CSV_FOLDER = "csv"

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("./favicon.ico")

# @app.post("/assignWithCsv")
# def upload(file: UploadFile = File(...)):
#     csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
#     data = {}
#     for rows in csvReader:             
#         key = rows['id']
#         data[key] = rows  
#     file.file.close()
    
@app.post("//initializeScheme")
def get_net_image_evaluate_local(file: UploadFile = File(...)):
    file_path = os.path.join(CSV_FOLDER, file.filename)
    load_csv_into_db(file_path)


    