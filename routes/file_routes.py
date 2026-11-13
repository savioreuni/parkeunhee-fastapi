from fastapi import APIRouter, HTTPException, status,UploadFile
from fastapi.responses import FileResponse
import os

file_router = APIRouter(tags=["file"])

file_folder = "static/files"

# ==================== 1. 파일 업로드 ======================

@file_router.post("/uploadfile",summary="단일 파일 업로드", status_code=status.HTTP_201_CREATED)
async def upload_file(file:UploadFile):
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="파일을 선택해주세요"
        )
    os.makedirs(file_folder,exist_ok=True)
    save_path = f"{file_folder}/{file.filename}"
    content = await file.read()
    with open(save_path,"wb") as f:
        f.write(content)

    return{"msg":"파일 업로드 및 저장 성공","filename":file.filename}

# ==================== 2. 파일 다운로드  ======================

@file_router.get("/download/{filename}", summary="파일 다운로드")
async def download_file(filename:str):
    path = f"{file_folder}/{filename}"
    if not os.path.isfile(path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="찾을 수 없는 파일 입니다."
        )
    return FileResponse(path=path,filename=filename)
    # return {"msg":f"{filename}다운로드 성공"}

# ==================== 3. 전체 파일 목록 ======================

@file_router.get("/filelist",summary="전체 파일 목록")
async def get_file_list():
    os.makedirs(file_folder,exist_ok=True)
    files= os.listdir(file_folder)
    file_list = []
    for i, name in enumerate(files):
        file_list.append({"idx":i,"filename":name})
    if not file_list:
        msg = "파일 없음"
    else:
        msg= "조회 성공"

    return {"msg":msg, "files":file_list }