# CICD-2 FastAPI Lab Template

This repository contains a FastAPI lab for the CICD-2 module.  
Use this `README.md` as the standard structure for future labs.

---

## Lab 5

To launch the app service run the following command in a codespace terminal. The service will then be available on port 8000

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

To launch the product serivce use the following command in a codespace terminal. The serivce will be available on port 8001

python -m uvicorn product_service.main:app --host 0.0.0.0 --port 8001

PRODUCT_SERVICE_URL provides the location of the product service.
```