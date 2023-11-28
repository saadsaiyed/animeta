# deploy_sagemaker.py
import sagemaker

role = "arn:aws:iam::944903593486:role/service-role/AmazonSageMaker-ExecutionRole-20231128T115277"

# Create a SageMaker model
model = sagemaker.model.Model(
    image_uri="944903593486.dkr.ecr.ca-central-1.amazonaws.com/animatediff:latest",
    role=role,
    sagemaker_session=sagemaker.Session(),
)

# Deploy the model as an endpoint
predictor = model.deploy(initial_instance_count=1, instance_type="ml.t2.medium")