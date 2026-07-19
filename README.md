# Full-Stack Web Application (FastAPI & React) - UTS Pemrograman Sisi Server

Tugas Ujian Tengah Semester (UTS) Semester 6 untuk mata kuliah Pemrograman Sisi Server. Proyek ini merupakan aplikasi full-stack yang mengintegrasikan backend berbasis Python (FastAPI) dengan frontend berbasis TypeScript (React).

## 🛠️ Tech Stack & Arsitektur

### 1. Backend (Sisi Server)
* **Framework:** FastAPI (Python)
* **Database ORM:** SQLModel & SQLAlchemy
* **Database Migrations:** Alembic
* **Authentication:** OAuth2 dengan JWT Token
* **Validasi Data:** Pydantic v2

### 2. Frontend (Sisi Klien)
* **Library:** React dengan TypeScript
* **Build Tool:** Vite
* **UI Components:** Chakra UI / Tailwind CSS
* **State Management:** TanStack Router & TanStack Query

### 3. Database
* **Engine:** PostgreSQL

---

## 🚀 Cara Menjalankan Proyek secara Lokal

### 1. Prasyarat (Prerequisites)
* Python 3.10+ sudah terinstal
* Node.js & npm sudah terinstal
* PostgreSQL Server sudah aktif di komputer

### 2. Konfigurasi Backend
1. Masuk ke folder backend:
   ```bash
   cd backend
   ```
2. Instal semua dependensi:
   ```bash
   pip install "fastapi[standard]" python-dotenv
   pip install .
   ```
3. Jalankan migrasi database untuk membuat tabel:
   ```bash
   alembic upgrade head
   ```
4. Jalankan server FastAPI:
   ```bash
   fastapi dev app/main.py
   ```
   *Backend akan berjalan di:* `http://127.0.0.1:8000`
   *Dokumentasi API Swagger:* `http://127.0.0`

### 3. Konfigurasi Frontend
1. Buka terminal baru dan masuk ke folder frontend:
   ```bash
   cd frontend
   ```
2. Instal dependensi dan jalankan server Vite:
   ```bash
   npm install
   npx vite
   ```
   *Frontend akan berjalan di:* `http://localhost:5173`

---

## 🔐 Akun Akses Default (Development)
Sesuai dengan konfigurasi pada file `.env`:
* **Email Administrasi:** `admin@gmail.com`
* **Kata Sandi:** `admin123`
