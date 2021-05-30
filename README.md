This repo provides a minimal proof on concept around containerizing machine learning models. The Data Scientist defines a prediction function 
and adds a few more lines to expose an endpoint. The docker file containerizes everything. After this, the Dev Ops team can upload the container 
to their cloud of choice and the Software Engineers can call an endpoint.

Big take away is data science only needs to write a few extra lines, and engineering only needs to call endpoints.

Mains steps:
* Create simulated dataset.
* Train a model.
* Define a scoring function.
* Expose an endpoint.
* Containerize with docker.

This model is in AWS using ECR/ECS and can be found [here](http://54.244.68.174:8888/scoreHere?json_input=[[0.0,%200.0]]).
