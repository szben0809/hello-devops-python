# Hello DevOps Python app

Egyszerű Python + Flask alkalmazás, amely HTTP-n elérhető, és egy szöveget ad vissza a `http://localhost:8080` címen.

## Követelmények

- Python 3.10 vagy újabb
- Git (opcionális, verziókövetéshez)
- Docker (konténer futtatásához, opcionális)

---

## Projekt indítása fejlesztői környezetben

### 1. Virtuális környezet létrehozása és aktiválása

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Függőségek telepítése (BUILD)

```bash
pip install -r requirements.txt
```

---

### 3. Alkalmazás futtatása

```bash
python Proba.py
```

Ezután az alkalmazás elérhető:

http://localhost:8080

---

## 4. Docker használata

### 4.1. Image buildelése

```bash
docker build -t hello-devops-python:v1 .
```

### 4.2. Konténer futtatása

```bash
docker run -p 8080:8080 hello-devops-python:v1
```

Az alkalmazás a konténerből is elérhető itt:

http://localhost:8080

---

## 5. CI pipeline és container registry

A GitHub Actions pipeline automatikusan:

- ellenőrzi a repót,
- buildeli az alkalmazást,
- Docker image-et készít,
- a képet pusholja a GitHub Container Registry-be (GHCR).

### 5.1. Image lehúzása a registryből

```bash
docker pull ghcr.io/<GitHub-felhasználóneved>/hello-devops-python:latest
```

### 5.2. Image futtatása

```bash
docker run -p 8080:8080 ghcr.io/<GitHub-felhasználóneved>/hello-devops-python:latest
```
