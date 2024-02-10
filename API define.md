Data Upload Module
This module will handle the upload of images and their associated label or class data, allowing users to manage their datasets effectively.



Data Upload Module
This module will handle the upload of images and their associated label or class data, allowing users to manage their datasets effectively.

1. Create a Project

Endpoint: /api/projects
Method: POST
Description: Create a new ML image classification or object detection project.
Request Body:

```json
{
  "name": "Project Name",
  "type": "classification/object_detection",
  "description": "Project Description"
}
