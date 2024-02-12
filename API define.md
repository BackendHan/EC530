## Data Upload Module

will handle the upload of images and their associated label or class data, allowing users to manage their datasets effectively.


### 1. Create a Project

Endpoint: /api/projects
Method: POST
Description: Create a new ML image classification or object detection project.
Request Body:

```json
{
  "name": "DIY ML for images",
  "type": "classification/object_detection",
  "description": "Project Description of DIY ML for images"
}
```
Response:
```json
{
  "projectId": "unique_project_id"
}
```

### 2. Upload Images

Endpoint: /api/projects/{MLForImages}/images
Method: POST
Description: Upload images for training in a project.
Request Body: Form-data with files.
Response:
```json
{
  "uploadedImages": [
    {
      "imageId": "unique_image_id",
      "fileName": "image_name.jpg"
    }
  ]
}
```

### 3. Upload Label/Class Data

Endpoint: /api/projects/{MLForImages}/labels
Method: POST
Description: Upload label or class data for images in a project.
Request Body:
```json
{
  "labels": [
    {
      "imageId": "unique_image_id",
      "label": "class_label"
    }
  ]
}
```
Response:
```json
{
  "message": "Labels uploaded successfully"
}
```


## Training Module

will cover the configuration, initiation, and monitoring of the training process, including the management of training parameters and results.

### 1. Analyze Data Before Training

Endpoint: /api/projects/{MLForImages}/data/analyze
Method: GET
Description: Analyze data to get insights before starting the training.
Response:
```json
{
  "dataAnalysis": {
    "totalImages": 100,
    "labelsDistribution": {
      "label1": 50,
      "label2": 50
    }
  }
}
```
### 2. Configure Training Parameters

Endpoint: /api/projects/{MLForImages}/training/configure
Method: POST
Description: Configure training parameters.
Request Body:

```json
{
  "parameters": {
    "learningRate": 0.001,
    "epochs": 10,
    "batchSize": 32
  }
}
```

Response:

```json
{
  "message": "Training configuration updated successfully"
}
```

### 3. Start Training

Endpoint: /api/projects/{MLForImages}/training/start
Method: POST
Description: Start the training process for the project.
Response:
```json
{
  "trainingId": "unique_training_id",
  "message": "Training started successfully"
}
```

### 4. Get Training Stats

Endpoint: /api/projects/{MLForImages}/training/{MLForImages}/stats
Method: GET
Description: Get stats when the training is completed.
Response:
```json
{
  "accuracy": 0.95,
  "loss": 0.05,
  "epochsCompleted": 10
}
```





