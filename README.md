# Etudier - Elearning Project 

Etudier is a web application for a hypothetical E-learning platform called Etudier (french for "to study"). 

The overall objective of creating this project and deploying it end to end was to gain a robust understanding about how to build agile development and integration pipelines like CI/CD using AWS Developer tools like - AWS CodePipeline and AWS CodeBuild.

The code to the project can be accessed at the following github url - https://github.com/rmalhotra2192/elearning-platform

The application is built upon the following Technology stack:
- Frontend
  - Vue.JS for SPA functionality
  - HTML & Tailwind CSS for UI
- Backend
  - Python
  - FastAPI
- Database
  - AWS RDS Powered PostgreSQL for Data persistence
- Source Version Control
  - Github
- Environment Handling
  - Docker Containers
- Deployment
  - AWS CodePipeline for orchestrating the complete build and deployment process
  - AWS CodeBuild for building Docker Container images
  - AWS ECR for storing docker container images
  - AWS Cloud Formation for creating and managing Infrastructure as Code
  - AWS ECS Cluster for deploying the application on the Fargate instances (serverless).



The project is powered using AWS ECS cluster that is automatically deployed using CI/CD pipeline. The CI/CD pipeline is built using the AWS CodePipeline, AWS CodeBuild and AWS CloudFormation Services and is triggered when changes are detected in source code repository i.e. github repository. 

The architecture of the application is depicted in the below given diagram.

[![Docker-Environment-2.png](https://i.postimg.cc/GtV6BYnb/Docker-Environment-2.png)](https://postimg.cc/n9K3gXLW)

### AWS Cloud Formation Environment

[![AWS-Cloud-Formation.png](https://i.postimg.cc/SNFhg6JQ/AWS-Cloud-Formation.png)](https://postimg.cc/mhwJDFYK)

### AWS Elastic Container Registry

[![AWS-Elastic-Container-Registry.png](https://i.postimg.cc/hPLq6XdL/AWS-Elastic-Container-Registry.png)](https://postimg.cc/qzvYCMQq)

### AWS Elastic Container Service

[![AWS-Elastic-Container-Service.png](https://i.postimg.cc/T3TX6TVZ/AWS-Elastic-Container-Service.png)](https://postimg.cc/rKZHGXYJ)

### AWS Code Pipeline Environment

[![AWS-Code-Pipeline-Environment.png](https://i.postimg.cc/T3Qv2BQh/CICD-Pipeline-using-AWS-Code-Pipeline.png)](https://postimg.cc/18gjJCkZ)

