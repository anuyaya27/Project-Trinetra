from fastapi import APIRouter
from models.killer_profile import generate_killer_response
from models.clue_decoder import decode_clue
from models.astrology_model import get_astrological_insight

router = APIRouter()

@router.post("/generate_killer_response")
def killer_response(prompt: str):
    return generate_killer_response(prompt)

@router.post("/analyze_clue")
def analyze_clue(clue: str):
    return decode_clue(clue)

@router.post("/get_astrology_insight")
def astrology_insight(birth_data: dict):
    return get_astrological_insight(birth_data)