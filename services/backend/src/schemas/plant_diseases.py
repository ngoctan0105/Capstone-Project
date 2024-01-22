from pydantic import BaseModel
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Plant_Diseases

PlantDiseaseInSchema = pydantic_model_creator(
    Plant_Diseases, name="PlantDiseaseIn", include=["id", "name", "plant", "disease", "symptoms", "causes", "measures"], exclude_readonly=False
)

PlantDiseaseOutSchema = pydantic_model_creator(
    Plant_Diseases, name="PlantDisease", include=["id", "name", "plant", "disease", "symptoms", "causes", "measures"]
)

class UpdatePlantDisease(BaseModel):
    name: Optional[str]
    plant: Optional[str]
    disease: Optional[str]
    symptoms: Optional[list]
    causes: Optional[list]
    measures: Optional[list]
