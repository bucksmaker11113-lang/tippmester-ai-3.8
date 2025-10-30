[README.md](https://github.com/user-attachments/files/23230793/README.md)
Tippmester AI 3.8 — Gold Edition

Ez egy minimalista, mobil-fókuszú PWA prototípus (Flask backend + statikus frontend).
Kövesd az alábbi lépéseket a GitHub feltöltéshez és Renderre deploy-hoz.

1) Git init, commit, push to GitHub
   git init
   git add .
   git commit -m "Tippmester 3.8 Gold"
   git branch -M main
   git remote add origin https://github.com/<your-username>/Tippmester-3.8-Gold.git
   git push -u origin main

2) Render.com — Create -> Web Service -> Connect GitHub repo
   Render felismeri a render.yaml fájlt és beállítja az appot.
   Start command: gunicorn backend.app:app

3) Mobil telepítés (PWA)
   Nyisd meg a Render URL-t mobilon, és válaszd: Add to Home Screen.

Megjegyzés: Ez egy demo prototípus. Éles odds-feed és pénzügyi API-k integrációja külön fejlesztést igényel.
