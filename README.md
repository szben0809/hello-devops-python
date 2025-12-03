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


```
## Dev Container használata (Választható feladatrész – 3.1)

A projekt tartalmaz egy `.devcontainer` mappát, amely VS Code Dev Containers környezetet biztosít
a fejlesztéshez. A Dev Container lehetővé teszi, hogy a projekt egy elkülönített, előre
konfigurált Linux-alapú fejlesztői konténerben fusson – ugyanazokkal a verziókkal és függőségekkel,
függetlenül attól, hogy a fejlesztő gépén mi van telepítve.

### 🔧 Dev Container indítása

1. Nyisd meg a projektet VS Code-ban.
2. Telepítsd a következő kiegészítőt (ha még nincs):
   - **Dev Containers** (Microsoft)
3. A bal alsó sarokban kattints a zöld ikonra.
4. Válaszd ki:
   **"Reopen in Container"**
5. A VS Code automatikusan:
   - felépíti a konténert a `.devcontainer/Dockerfile` alapján,
   - létrehozza a környezetet,
   - telepíti a `requirements.txt` függőségeit.

### ▶️ Futás DevContaineren belül

A konténerben megnyíló beépített terminálban futtasd:

```bash
python Proba.py
