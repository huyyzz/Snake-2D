@ECHO OFF
D:
cd "D:\Snake\venv\SnakeSanMoi"
call "D:\Snake\venv\Scripts\activate.bat"
uvicorn app:app --reload
PAUSE
