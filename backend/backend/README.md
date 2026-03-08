# Trading Scanner

Simple trading signal scanner.

Run backend:

cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

Run frontend:

cd frontend
python -m http.server 5500
