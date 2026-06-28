# 🌾 AgriSathi AI

> AI-powered agriculture platform built with **Next.js**, **FastAPI**, and **Supabase**.

---

## 🚀 Features

- 🌱 Crop Disease Detection
- 🤖 AI Crop Advisory
- 📊 Dashboard
- 📷 Crop Scan
- 📈 Market Insights
- 👤 User Profile
- 🔐 Authentication
- 🌙 Dark / Light Mode
- 📱 Responsive UI
- ⚡ REST API with FastAPI
- 🗄️ Supabase Database Integration

---

## 🛠 Tech Stack

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- Axios

### Backend
- FastAPI
- Python
- Supabase
- Pydantic
- Uvicorn

---

## 📂 Project Structure

```text
AgriSathi-AI/
│
├── frontend/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── schemas/
│   │   ├── middleware/
│   │   ├── config.py
│   │   ├── main.py
│   │   └── supabase_client.py
│   │
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
└── README.md
```

---

## ⚙️ Backend Setup

### Clone Repository

```bash
git clone https://github.com/pantagrima300-spec/AgriSathi-AI.git
cd AgriSathi-AI/backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file.

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

### Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/crops` | Get all crops |
| GET | `/api/crops/{id}` | Get single crop |
| POST | `/api/crops` | Create crop |
| PUT | `/api/crops/{id}` | Update crop |
| DELETE | `/api/crops/{id}` | Delete crop |
| GET | `/api/crops/search?name=` | Search crops |

---

## 🌐 Frontend

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:3000
```

---

## 📦 API Testing

- Postman Collection Included
- CRUD Operations Tested
- JSON Responses
- HTTP Status Codes
- Supabase Integration

---

## 👨‍💻 Developed By

**Agrima Pant**

B.Tech Computer Science Engineering

Graphic Era University

---

## 📄 License

This project is developed for educational and internship purposes.
