# Smart Photo Album

In this project, we implemented a photo album web application, that can be searched using natural language through both text and voice to retrieve images. We used AWS S3, API Gateway, Lambda to build a scalable website. In addition, we also used Lex, ElasticSearch, and Rekognition to create an intelligent search layer to query photos for people, objects, actions, landmarks and more. This is one of the course project of COMS E6998 Cloud Computing & Big Data at Columbia University. 

### How it works

Users can upload their photo through our website and store on the cloud storage. On the other hand, for a given search query, the application would return every photo that matches the query. 

### Built With
* [S3](https://aws.amazon.com/s3/) - Host static frontend and store images.
* [API Gateway](https://aws.amazon.com/api-gateway/) - For creating, monitoring, and securing REST APIs at any scale. 
* [Lambda](https://aws.amazon.com/lambda/) - Function as a Service,  event-driven, and serverless computing platform. Acted as backend to run code without provisioning or managing servers.  
* [Lex](https://aws.amazon.com/lex/) - Extract keywords in user search query. 
* [ElasticSearch](https://www.elastic.co/products/elasticsearch) - Search engine to handle unstructured search. 
* [Amazon Rekognition](https://aws.amazon.com/rekognition/) - Extract objects in each images by using machine learning and computer vision technologies. 


### Architecture
![image](https://drive.google.com/uc?export=view&id=14LXEb4fezytMfRFkZkVw-QWAiDYrObD3)