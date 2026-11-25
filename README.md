# 🐍 Snake Game

Một trò chơi **Snake săn mồi** được xây dựng bằng **Python**, **FastAPI**, **HTML**, **CSS** và **JavaScript**.
## Yêu cầu
- Python 3.10 trở lên
- FastAPI
- Uvicorn

## Cài đặt

### 1. Tạo môi trường ảo (khuyến nghị)
**Windows**
```cmd
python -m venv venv
venv\Scripts\activate
cd venv
```
### 2. Clone dự án
```cmd
git clone https://github.com/Dqquan2079/SnakeSanMoi.git
cd SnakeSanMoi
```
### 3. Cài đặt thư viện

```cmd
pip install -r requirements.txt
```

## Chạy trò chơi
Khởi động máy chủ FastAPI:
```cmd
uvicorn app:app --reload
```
Sau đó mở trình duyệt và truy cập:

```
http://127.0.0.1:8000
```

## Điều khiển
↑ Di chuyển lên
← Di chuyển sang trái
↓ Di chuyển xuống
→ Di chuyển sang phải