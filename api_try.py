from fastapi import FastAPI, Path, HTTPException,File,UploadFile
from typing import Annotated
import os
from fastapi.responses import JSONResponse
from main import recognize_person
import uvicorn

app = FastAPI()

@app.get("/")


@app.post("/upload_file/")
async def create_upload_file(name: str, file: UploadFile):
    try:
        file_path = os.path.join(r'C:\Users\Beyza\g_teknik\face_recognition\face_dataset', f"{name}")
        
        #the file_path where we save it 
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
    
        # return a message message that the file is upload successfull 
        return JSONResponse(status_code=200, content={"message": "Dosya başariyla yüklendi"})
    
    except Exception as e:
        #and if not return a exception
        return JSONResponse(status_code=500, content={"message": f"Dosya yükleme başarisiz oldu. Hata: {str(e)}"})



@app.post("/recog_persons/")
async def run_recognition():
    try:
        recognize_person()  # recognize_person fonksiyonunu çağırın (parametre gerektirmediği varsayımıyla)
        
        return JSONResponse(status_code=200, content={"message": "Tanıma işlemi başarıyla çalıştırıldı"})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Tanıma işlemi başarısız oldu. Hata: {str(e)}"})
    
if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)


    #python api_try.py
    #uvicorn api_try:app --reload
    #şekilde kullanarak derleme sağlayabilirsin 
    