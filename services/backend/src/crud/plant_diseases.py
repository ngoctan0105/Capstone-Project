from ultralytics import YOLO
import os
from typing import List
from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist
from src.database.models import Plant_Diseases
from src.schemas.plant_diseases import PlantDiseaseOutSchema
from src.schemas.token import Status

model = YOLO(os.listdir()[-1] + '/best.pt')
# model = YOLO(os.listdir()[-1] + '/best_dropout.pt')
# model = YOLO(os.listdir()[-1] + '/best-7.pt')

# segmentation_model = YOLO(os.listdir()[-1] + '/best_grape_seg.pt')

async def get_plant_diseases() ->List[PlantDiseaseOutSchema]:
    # await Plant_Diseases.all().delete()
    # return []
    return await PlantDiseaseOutSchema.from_queryset(Plant_Diseases.all())

async def get_plant_disease(plant_disease_name) -> PlantDiseaseOutSchema:
    return await PlantDiseaseOutSchema.from_queryset_single(Plant_Diseases.get(name=plant_disease_name))

async def create_plant_disease(plant_disease) -> PlantDiseaseOutSchema:
    plant_disease_dict = plant_disease.dict(exclude_unset=False)
    plant_disease_obj = await Plant_Diseases.create(**plant_disease_dict)
    return await PlantDiseaseOutSchema.from_tortoise_orm(plant_disease_obj)

async def delete_plant_disease(plant_disease_id):
    try:
        db_plant_disease = await PlantDiseaseOutSchema.from_queryset_single(Plant_Diseases.get(id=plant_disease_id))
        print("db_plant_disease: ", db_plant_disease)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Plant Disease {plant_disease_id} not found")

    deleted_count = await Plant_Diseases.filter(id=plant_disease_id).delete()
    print("deleted_count: ", deleted_count)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Plant Disease {plant_disease_id} not found")
    return Status(message="Deleted plant disease " + str(plant_disease_id))

async def update_plant_disease(plant_disease_id, plant_disease) -> PlantDiseaseOutSchema:
    try:
        db_plant_disease = await PlantDiseaseOutSchema.from_queryset_single(Plant_Diseases.get(id=plant_disease_id))
        print("db_plant_disease: ", db_plant_disease)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Plant disease {plant_disease_id} not found")

    await Plant_Diseases.filter(id=plant_disease_id).update(**plant_disease.dict(exclude_unset=True))
    return await PlantDiseaseOutSchema.from_queryset_single(Plant_Diseases.get(id=plant_disease_id))
