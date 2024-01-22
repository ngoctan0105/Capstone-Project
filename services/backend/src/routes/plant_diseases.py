from ultralytics import YOLO
from fastapi import File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import io
import numpy as np
import cv2
from src.crud.plant_diseases import model
# from src.crud.plant_diseases import segmentation_model

from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.plant_diseases as crud
from src.schemas.plant_diseases import PlantDiseaseInSchema, PlantDiseaseOutSchema, UpdatePlantDisease
from src.schemas.token import Status

router = APIRouter()

class_labels = ['Coffee__Healthy',
                'Coffee__Miner',
                'Coffee__Phoma',
                'Coffee__Rust',
                'Corn_(Maize)__Cercospora_Leaf_Spot Gray_leaf_spot',
                'Corn_(Maize)__Common_Rust',
                'Corn_(Maize)__Healthy',
                'Corn_(Maize)__Northern_Leaf_Blight',
                'Grape__Black_Rot',
                'Grape__Esca_(Black_Measles)',
                'Grape__Healthy',
                'Grape__Leaf_Blight_(Isariopsis_Leaf_Spot)',
                'Jackfruit__Algal_Leaf_Spot',
                'Jackfruit__Black_Spot',
                'Jackfruit__Healthy',
                'Mango__Anthracnose',
                'Mango__Bacterial_Canker',
                'Mango__Cutting_Weevil',
                'Mango__Die_Back',
                'Mango__Gall_Midge',
                'Mango__Healthy',
                'Mango__Powdery_Mildew',
                'Mango__Sooty_Mould',
                'Rice__Bacterial_Leaf_Blight',
                'Rice__Brown_Spot',
                'Rice__Healthy',
                'Rice__Leaf_Blast',
                'Rice__Leaf_Scald',
                'Rice__Narrow_Brown_Spot',
                'Sugarcane__Healthy',
                'Sugarcane__Mosaic',
                'Sugarcane__Red_Rot',
                'Sugarcane__Rust',
                'Sugarcane__Yellow',
                'Tea__Algal_Spot',
                'Tea__Brown_Blight',
                'Tea__Gray_Blight',
                'Tea__Healthy',
                'Tea__Helopeltis',
                'Tea__Red_Spot']

# class_labels = ['Grape__Black_Rot',
#                 'Grape__Esca_(Black_Measles)',
#                 'Grape__Healthy',
#                 'Grape__Leaf_Blight_(Isariopsis_Leaf_Spot)'
# ]

# def segment(img):
#   results = segmentation_model.predict(img)
#   # print(results[0].masks)
#   if(results[0].masks is not None):
#       # Convert mask to single channel image
#       mask_raw = results[0].masks[0].cpu().data.numpy().transpose(1, 2, 0)

#       # Convert single channel grayscale to 3 channel image
#       mask_3channel = cv2.merge((mask_raw,mask_raw,mask_raw))

#       # Get the size of the original image (height, width, channels)
#       h2, w2, c2 = results[0].orig_img.shape

#       # Resize the mask to the same size as the image (can probably be removed if image is the same size as the model)
#       mask = cv2.resize(mask_3channel, (w2, h2))

#       # Convert BGR to HSV
#       hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)

#       # Define range of brightness in HSV
#       lower_black = np.array([0,0,0])
#       upper_black = np.array([0,0,1])

#       # Create a mask. Threshold the HSV image to get everything black
#       mask = cv2.inRange(mask, lower_black, upper_black)

#       # Invert the mask to get everything but black
#       mask = cv2.bitwise_not(mask)

#       # Apply the mask to the original image
#       masked = cv2.bitwise_and(results[0].orig_img, results[0].orig_img, mask=mask)

#       # Show the masked part of the image
#       # cv2_imshow(masked)

#       return masked

#   return None

@router.post(
    "/single_file",
    response_model=object,
    dependencies=[],
)
async def classify_image(file: UploadFile = File(...)):

    # image_bytes = await file.read()
    # image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    # image = np.array(image)

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # image = segment(image)

    results = model(image)
    print('result: ', results)
    indexes = [results[i].probs.top1 for i in range(len(results))]
    #print('indexes: ', indexes)
    max_probs = [results[i].probs.top1conf.item() for i in range(len(results))]
    #print('max_probs: ', max_probs)
    most_class_index = np.argmax(max_probs)
    #print('most_class_index: ', most_class_index)
    most_class_prob = max_probs[most_class_index]
    #print('most_class_prob: ', most_class_prob)
    predicted_class = class_labels[indexes[most_class_index]]
        
    # Prepare the response
    response_data = {
        "predicted_class": predicted_class,
        "class_probability": most_class_prob
    }

    return JSONResponse(content=response_data)

@router.post(
    "/multiple_files",
    response_model=object,
    dependencies=[],
)
async def classify_images(files: List[UploadFile] = File(...)):
    response_data = []
    for file in files:
        # image_bytes = await file.read()
        # image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        # image = np.array(image)

        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # image = cv2.resize(image, (640, 640))

    # # Get image dimensions
    #     height, width = image.shape[:2]

    #     # Find the maximum dimension (width or height)
    #     max_dimension = max(height, width)

    #     # Create a square canvas with white background
    #     square_img = np.full((max_dimension, max_dimension, 3), 255, dtype=np.uint8)

    #     # Calculate the position to paste the original image
    #     x_position = (max_dimension - width) // 2
    #     y_position = (max_dimension - height) // 2

    #     # Paste the original image onto the square canvas
    #     square_img[y_position:y_position + height, x_position:x_position + width] = image    
    #     image = square_img
    #     print(image.shape)

        results = model(image)
        print('result: ', results)
        indexes = [results[i].probs.top1 for i in range(len(results))]
        #print('indexes: ', indexes)
        max_probs = [results[i].probs.top1conf.item() for i in range(len(results))]
        #print('max_probs: ', max_probs)
        most_class_index = np.argmax(max_probs)
        #print('most_class_index: ', most_class_index)
        most_class_prob = max_probs[most_class_index]
        #print('most_class_prob: ', most_class_prob)
        predicted_class = class_labels[indexes[most_class_index]]
        response_data.append({
            'Sample': file.filename,
            'Result': predicted_class,
            'Confidence': most_class_prob
        })

    return JSONResponse(content=response_data)

@router.get(
    "/all",
    response_model=List[PlantDiseaseOutSchema],
    dependencies=[],
)
async def get_plant_diseases():
    return await crud.get_plant_diseases()

@router.get(
    "/plant_disease/{plant_disease_name}",
    response_model=PlantDiseaseOutSchema,
    dependencies=[],
)
async def get_plant_disease(plant_disease_name: str) -> PlantDiseaseOutSchema:
    try:
        return await crud.get_plant_disease(plant_disease_name)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Plant disease does not exist",
        )

@router.post(
    "/add",
    response_model=PlantDiseaseOutSchema,
    dependencies=[],
)
async def create_plant_disease(
    plant_disease: PlantDiseaseInSchema
) -> PlantDiseaseOutSchema:
    return await crud.create_plant_disease(plant_disease)

@router.delete(
    "/plant_disease/{plant_disease_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[],
)
async def delete_plant_disease(
    plant_disease_id: int
):
    return await crud.delete_plant_disease(plant_disease_id)

@router.patch(
    "/plant_disease/{plant_disease_id}",
    response_model=PlantDiseaseOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[],
)
async def update_plant_disease(
    plant_disease_id: int,
    plant_disease: UpdatePlantDisease
) -> PlantDiseaseOutSchema:
    return await crud.update_plant_disease(plant_disease_id, plant_disease)