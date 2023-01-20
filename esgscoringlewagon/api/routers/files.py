from fastapi import APIRouter
from utils.AppRequests import cloneManarEcheanciers, cloneManarTitres

router = APIRouter()

@router.get("/fichiers/Titres")
def get_Files_From_Excel():
    cloneManarTitres()

@router.get("/fichiers/Echeanciers")
def get_Files_From_Excel():
    cloneManarEcheanciers()
