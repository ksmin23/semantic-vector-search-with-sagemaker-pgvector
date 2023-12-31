#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sagemaker_pgvector import (
  VpcStack,
  AuroraPostgresqlStack,
  SageMakerStudioStack
)

APP_ENV = cdk.Environment(
  account=os.environ["CDK_DEFAULT_ACCOUNT"],
  region=os.environ["CDK_DEFAULT_REGION"]
)

app = cdk.App()

vpc_stack = VpcStack(app, 'VectorSearchVpcStack',
  env=APP_ENV)

aurora_pgsql_stack = AuroraPostgresqlStack(app, 'VSPgVectorStack',
  vpc_stack.vpc,
  env=APP_ENV
)
aurora_pgsql_stack.add_dependency(vpc_stack)

sm_studio_stack = SageMakerStudioStack(app, 'VSSageMakerStudioStack',
  vpc_stack.vpc,
  aurora_pgsql_stack.sg_rds_client,
  env=APP_ENV
)
sm_studio_stack.add_dependency(aurora_pgsql_stack)

app.synth()
