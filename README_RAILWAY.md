# MZ/X 4.2 Fusion Intelligence Engine

## Telepítés (helyben)
pip install -r requirements.txt
uvicorn app.main:app --reload

## Railway deploy
1. Csatold a GitHub repót a Railwayhez.
2. Állítsd be a `Procfile`-t és a `requirements.txt`-t.
3. Deploy → A web app automatikusan indul.
