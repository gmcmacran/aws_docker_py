There is a natural friction between Data Scientists and Software Engineers. Data Scientists make machine learning models and reports. 
Typically they don't have experance around app creation. Software Engineers make apps but don't do machine learning. There is both a 
spoken language barrier and programming language barrier between the two teams. 

How can the devs interact with a model given Java or C# can't load scikit learn files? How can model delivery be defined when 
neither teams understand what the other team needs?

This repo provides a minimal proof on concept around bridging this gap. The Data Scientist defines a prediction function and adds a 
few more lines to expose an endpoint. The docker file containerizes everything. After this, the Dev Ops team can upload the container 
to their cloud of choice and the Software Engineers can call an endpoint.

Big take away is data science only needs to write a few extra lines, and engineering only needs to call endpoints.

Mains steps:
* Create simulated dataset.
* Train a model
* Define a scoring function.
* Expose an endpoint.
* Containerize with docker.

This model is in AWS's cloud using ECR/ECS and can be found [here](http://54.244.68.174:8888/scoreHere?json_input=[[0.0,%200.0]]).
