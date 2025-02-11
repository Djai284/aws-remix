# AWS Remix Report

**Report Generated:** 2025-02-10T22:41:14.475964

## Table of Contents
- [AWS Account Information](#aws-account-information)
- [Cost](#cost)
- [EC2](#ec2)
- [Lambda](#lambda)
- [ECS](#ecs)
- [S3](#s3)
- [RDS](#rds)
- [VPC](#vpc)
- [IAM](#iam)

## AWS Account Information

**Account Number:** 076812642930
**Account Alias:** tabprodaws
**Active Regions:** us-west-2, us-east-2

## Cost

**ThirtyDayCost:** 
**TimePeriod:** 
**Start:** 2025-01-12

    **End:** 2025-02-11

  **TotalUnblendedCost:** 8479.8896101114

**RegionCosts90Day:** 
**StartDate:** 2024-11-13

  **EndDate:** 2025-02-11

  **RegionCosts:** 
**Region:** us-west-2

    **Cost:** 32696.074433785998

    **Region:** us-east-2

    **Cost:** 1945.2603901102

    **Region:** us-east-1

    **Cost:** 0.0501448264

    **Region:** us-west-1

    **Cost:** 8.4e-06

    **Region:** ap-northeast-1

    **Cost:** 0.0

    **Region:** ap-northeast-2

    **Cost:** 0.0

    **Region:** ap-northeast-3

    **Cost:** 0.0

    **Region:** ap-south-1

    **Cost:** 0.0

    **Region:** ap-southeast-1

    **Cost:** 0.0

    **Region:** ap-southeast-2

    **Cost:** 0.0

    **Region:** ca-central-1

    **Cost:** 0.0

    **Region:** eu-central-1

    **Cost:** 0.0

    **Region:** eu-north-1

    **Cost:** 0.0

    **Region:** eu-west-1

    **Cost:** 0.0

    **Region:** eu-west-2

    **Cost:** 0.0

    **Region:** eu-west-3

    **Cost:** 0.0

    **Region:** global

    **Cost:** 0.0

    **Region:** sa-east-1

    **Cost:** 0.0

  **TotalCost:** 34641.384977122594

**RelevantRegions:** 
us-west-2

  us-east-2

**ThreeMonthCostBreakdown:** 
**TimePeriod:** 
**Start:** 2024-11-13

    **End:** 2025-02-11

  **CostByService:** 
**Service:** AWS CloudTrail

    **Amount:** 0.0

    **Service:** AWS Direct Connect

    **Amount:** 10.4688272876

    **Service:** AWS Key Management Service

    **Amount:** 47.3466510264

    **Service:** AWS Secrets Manager

    **Amount:** 7.050118318399999

    **Service:** AWS Transfer Family

    **Amount:** 647.3848536605

    **Service:** Amazon DynamoDB

    **Amount:** 0.0

    **Service:** EC2 - Other

    **Amount:** 4958.941309397201

    **Service:** Amazon Elastic Compute Cloud - Compute

    **Amount:** 21334.162646687997

    **Service:** Amazon Elastic Container Service for Kubernetes

    **Amount:** 1725.6

    **Service:** Amazon Elastic Load Balancing

    **Amount:** 185.03983151199998

    **Service:** Amazon GuardDuty

    **Amount:** 29.9825116617

    **Service:** Amazon Relational Database Service

    **Amount:** 3635.9813188808

    **Service:** Amazon Simple Notification Service

    **Amount:** 9.9372e-06

    **Service:** Amazon Simple Queue Service

    **Amount:** 0.2303547434

    **Service:** Amazon Simple Storage Service

    **Amount:** 629.5223342991001

    **Service:** Amazon Virtual Private Cloud

    **Amount:** 377.5577260077

    **Service:** AmazonCloudWatch

    **Amount:** 1052.0664837026

    **Service:** AWS Cost Explorer

    **Amount:** 0.05

    **Service:** AWS Glue

    **Amount:** 0.0

  **CostByRegion:** 
**Region:** ap-northeast-1

    **Amount:** 0.0

    **Region:** ap-northeast-2

    **Amount:** 0.0

    **Region:** ap-northeast-3

    **Amount:** 0.0

    **Region:** ap-south-1

    **Amount:** 0.0

    **Region:** ap-southeast-1

    **Amount:** 0.0

    **Region:** ap-southeast-2

    **Amount:** 0.0

    **Region:** ca-central-1

    **Amount:** 0.0

    **Region:** eu-central-1

    **Amount:** 0.0

    **Region:** eu-north-1

    **Amount:** 0.0

    **Region:** eu-west-1

    **Amount:** 0.0

    **Region:** eu-west-2

    **Amount:** 0.0

    **Region:** eu-west-3

    **Amount:** 0.0

    **Region:** global

    **Amount:** 0.0

    **Region:** sa-east-1

    **Amount:** 0.0

    **Region:** us-east-1

    **Amount:** 0.0501448264

    **Region:** us-east-2

    **Amount:** 1945.2603901102

    **Region:** us-west-1

    **Amount:** 8.4e-06

    **Region:** us-west-2

    **Amount:** 32696.074433785998

  **Forecast:** 
**TotalCostForecast:** 11849.14031993908

  **TotalCost:** 34641.384977122594

## EC2

**us-east-2:** 
**InstanceId:** i-09f22b87e4f46c7af

  **InstanceType:** t2.medium

  **State:** running

  **LaunchTime:** 2023-06-04 14:11:49+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** True

  **PrivateIpAddress:** 10.0.3.65

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0712fdc452bdd35b2

    **GroupName:** eks-cluster-sg-prod-3449687

  **Tags:** 
**Key:** k8s.io/cluster-autoscaler/prod

    **Value:** owned

    **Key:** aws:ec2launchtemplate:version

    **Value:** 1

    **Key:** aws:eks:cluster-name

    **Value:** prod

    **Key:** aws:autoscaling:groupName

    **Value:** eks-prod-2023060414105047940000000b-56c4435f-8c1a-f712-f0a0-438b1ef23bf6

    **Key:** eks:cluster-name

    **Value:** prod

    **Key:** kubernetes.io/cluster/prod

    **Value:** owned

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-00f9c103a09ea6147

    **Key:** eks:nodegroup-name

    **Value:** prod-2023060414105047940000000b

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-b52eca84-a115-e39e-a41a-8420afc6ee39

  **EBSVolumes:** 
**VolumeId:** vol-06c1cf1d87beec892

    **Encrypted:** False

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 45929.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 46280.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 45937.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 42279.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 37534.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 44265.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 44697.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 44938.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 46080.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 45161.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 45352.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 45385.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 45017.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 44956.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 86016.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 61440.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 273846272.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 276698112.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 271004160.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 266795008.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 256568832.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 273236992.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 268879360.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 426616832.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 665679872.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 272428544.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 267043840.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 271119872.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 270542336.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 266343424.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 4.671478303893876

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 4.672427354959308

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 4.699364381560322

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 4.72850189498386

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 4.739689791583698

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 4.725498367527742

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 4.755605714350383

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 4.738665531202968

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 4.705095654507452

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 4.669462167331554

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 4.633800882890667

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 4.5894134247085026

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 4.597711160522265

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 4.64022698493987

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 413381.0548611111

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 413280.0916666667

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 413495.88402777776

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 414850.25416666665

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 413378.18888888886

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 413232.08125

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 413040.89930555556

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 439516.3722222222

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 468367.6638888889

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 413269.5388888889

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 413372.2951388889

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 413438.0729166667

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 413452.2673611111

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 413364.8473867596

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 185158.81319444443

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 185203.94722222222

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 185436.20277777777

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 185769.26944444445

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 185494.13125

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 185679.89930555556

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 185441.94722222222

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 185336.44791666666

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 185123.13472222222

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 184981.04444444444

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 185041.6611111111

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 185320.01527777777

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 185468.51805555556

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 185363.36864111497

  **InstanceId:** i-044bbe17d7775fdbb

  **InstanceType:** t2.medium

  **State:** running

  **LaunchTime:** 2023-06-04 14:11:49+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** True

  **PrivateIpAddress:** 10.0.1.220

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0712fdc452bdd35b2

    **GroupName:** eks-cluster-sg-prod-3449687

  **Tags:** 
**Key:** aws:eks:cluster-name

    **Value:** prod

    **Key:** aws:ec2launchtemplate:version

    **Value:** 1

    **Key:** eks:nodegroup-name

    **Value:** prod-2023060414105047940000000b

    **Key:** aws:autoscaling:groupName

    **Value:** eks-prod-2023060414105047940000000b-56c4435f-8c1a-f712-f0a0-438b1ef23bf6

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-bd3d49a6-73ae-4c9e-8e3a-27aaea7a5ca9

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-00f9c103a09ea6147

    **Key:** eks:cluster-name

    **Value:** prod

    **Key:** k8s.io/cluster-autoscaler/prod

    **Value:** owned

    **Key:** kubernetes.io/cluster/prod

    **Value:** owned

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

  **EBSVolumes:** 
**VolumeId:** vol-00bce9bf2ff7b541f

    **Encrypted:** False

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 43086.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 44091.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 43813.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 44062.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 43666.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 35385.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 39823.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 42846.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 42589.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 40767.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 41114.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 41406.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 42099.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 42966.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 114688.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 126976.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 239281152.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 240695808.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 239819776.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 241280512.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 237315584.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 228222464.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 232775168.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 397169664.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 630663680.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 230220800.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 230426112.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 231655424.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 233941504.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 236097536.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 2.118790516680775

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 2.1180304699247205

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 2.114671406483128

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 2.106342359383345

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2.0958557368954946

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2.0970806902415946

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 2.101359758684886

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 2.0966697168948953

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2.1026429489783722

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 2.104628624379271

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 2.1039617864987084

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 2.0889262246116087

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 2.089026984523756

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 2.090866313842404

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 115468.56527777777

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 115486.45763888888

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 115454.94791666667

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 115520.17986111112

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 115465.2625

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 115596.81944444444

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 115439.41944444444

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 140931.22708333333

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 172344.04513888888

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 115476.47083333334

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 115424.63055555556

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 115562.74513888889

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 115448.52222222222

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 115436.26341463414

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 45399.62222222222

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 45632.910416666666

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 45594.57986111111

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 45613.19861111111

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 45594.294444444444

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 45623.44236111111

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 45502.40416666667

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 45416.60555555556

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 45411.084027777775

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 45328.572222222225

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 45315.75277777778

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 45480.6375

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 45567.05347222222

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 45705.09337979094

  **InstanceId:** i-057b9cd2c0ba5a0ba

  **InstanceType:** t2.medium

  **State:** running

  **LaunchTime:** 2023-06-04 14:11:49+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** True

  **PrivateIpAddress:** 10.0.2.4

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0712fdc452bdd35b2

    **GroupName:** eks-cluster-sg-prod-3449687

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-a11df7bd-4606-ec0f-0c98-0900a05b8c75

    **Key:** aws:autoscaling:groupName

    **Value:** eks-prod-2023060414105047940000000b-56c4435f-8c1a-f712-f0a0-438b1ef23bf6

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-00f9c103a09ea6147

    **Key:** eks:nodegroup-name

    **Value:** prod-2023060414105047940000000b

    **Key:** eks:cluster-name

    **Value:** prod

    **Key:** kubernetes.io/cluster/prod

    **Value:** owned

    **Key:** aws:ec2launchtemplate:version

    **Value:** 1

    **Key:** aws:eks:cluster-name

    **Value:** prod

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** k8s.io/cluster-autoscaler/prod

    **Value:** owned

  **EBSVolumes:** 
**VolumeId:** vol-08388187005a1cf11

    **Encrypted:** False

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 195.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 279.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 8.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 49501.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 49058.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 49201.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 48849.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 49283.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 39975.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 44894.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 49240.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 46949.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 46467.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 46551.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 46855.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 48108.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 48099.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 90112.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 118784.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 69632.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 3215360.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 2826240.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 81920.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 40960.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 208896.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 4096.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 290289152.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 286021632.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 286912512.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 283815936.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 289148416.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 270256640.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 276728320.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 835782656.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 283810816.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 278283776.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 276909568.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 278840320.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 282031616.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 283355136.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 2.454508348957222

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 2.4424495080430564

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 2.4406020712788044

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 2.4389182966512135

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2.4354066667325247

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2.433885090840498

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 2.4535218181045835

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 2.4469480492987143

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2.438096607989093

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 2.4632104666498056

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 2.4735178055953213

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 2.46290405595092

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 2.4605000213459736

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 2.4720325226513777

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 196497.37569444443

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 196370.25833333333

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 196270.38958333334

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 196388.3875

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 196556.74097222224

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 196967.125

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 196603.42083333334

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 275994.6736111111

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 196259.81180555557

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 196490.06458333333

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 196735.3361111111

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 197230.25694444444

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 197105.65625

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 196794.6912891986

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 66598.675

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 66786.56944444444

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 66796.20694444445

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 66848.90208333333

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 66880.56666666667

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 67032.15625

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 66744.22083333334

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 66573.58402777778

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 66459.0923611111

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 66530.17708333333

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 66565.12569444445

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 66870.99652777778

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 66996.27361111112

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 66994.00278745644

  **InstanceId:** i-05e7ece439218cac1

  **InstanceType:** t2.medium

  **State:** running

  **LaunchTime:** 2024-09-30 02:01:14+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** True

  **PrivateIpAddress:** 10.0.3.209

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0712fdc452bdd35b2

    **GroupName:** eks-cluster-sg-prod-3449687

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-a99df595-6486-4ea5-2eb2-a988e2342a48

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-00f9c103a09ea6147

    **Key:** k8s.io/cluster-autoscaler/prod

    **Value:** owned

    **Key:** aws:ec2launchtemplate:version

    **Value:** 1

    **Key:** aws:eks:cluster-name

    **Value:** prod

    **Key:** aws:autoscaling:groupName

    **Value:** eks-prod-2023060414105047940000000b-56c4435f-8c1a-f712-f0a0-438b1ef23bf6

    **Key:** eks:nodegroup-name

    **Value:** prod-2023060414105047940000000b

    **Key:** eks:cluster-name

    **Value:** prod

    **Key:** kubernetes.io/cluster/prod

    **Value:** owned

  **EBSVolumes:** 
**VolumeId:** vol-074cac6a9f92b97a0

    **Encrypted:** False

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 43580.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 38615.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 35323.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 40301.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 41269.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 40887.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 41302.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 42351.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 45822.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 42276.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 43233.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 43026.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 42799.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 43169.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 49152.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 241657856.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 228697600.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 232194560.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 232526848.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 235446784.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 232461824.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 234513408.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 393858560.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 637258240.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 237926912.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 243811328.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 241515520.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 238200832.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 241203200.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 5.159458852748157

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 5.149884576070682

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 5.127265642671301

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 5.094490010193586

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 5.110939338052093

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 5.094883266924555

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 5.1328040292233865

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 5.159659251515092

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 5.132014227573639

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 5.159889607745715

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 5.154485421284877

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 5.1628869971840885

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 5.172942364376042

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 5.181944538249151

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 100474.00972222222

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 100583.3111111111

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 100613.13333333333

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 100509.85694444444

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 100539.68680555555

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 100550.48436414177

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 100554.77569444444

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 125311.42083333334

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 157786.80833333332

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 100607.45138888889

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 100563.87847222222

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 100516.36622654622

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 100592.94166666667

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 100622.92061281337

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 36289.5125

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 36544.92083333333

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 36585.65902777778

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 36564.751388888886

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 36594.8375

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 36598.4530924253

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 36383.76944444444

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 36376.066666666666

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 36875.66736111111

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 36312.74097222222

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 36312.59166666667

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 36475.75330090341

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 36562.895833333336

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 36642.74512534819

**us-west-2:** 
**InstanceId:** i-0fcd40a888a44eb39

  **InstanceType:** t2.micro

  **State:** stopped

  **LaunchTime:** 2023-07-17 21:09:15+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** True

  **PrivateIpAddress:** 10.27.31.120

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-021c493b216add148

    **GroupName:** prod-ping-sec-group

  **Tags:** 
**Key:** Name

    **Value:** Prod-Ping

  **EBSVolumes:** 
**VolumeId:** vol-0a8d014c9bdc166a4

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 100

    **Throughput:** None

    **SizeGiB:** 8

    **Utilization:** 
**VolumeReadOps:** 


      **VolumeWriteOps:** 


      **VolumeReadBytes:** 


      **VolumeWriteBytes:**

  **Utilization:** 
**CPU:** 


    **NetworkIn:** 


    **NetworkOut:**

  **InstanceId:** i-0f7670bc3113446af

  **InstanceType:** t3a.small

  **State:** running

  **LaunchTime:** 2023-08-18 16:33:11+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.20.200

  **PublicIpAddress:** None

  **KeyName:** sectigokeypair

  **SecurityGroups:** 
**GroupId:** sg-01ca024603126a921

    **GroupName:** sectigo_security_group

  **Tags:** 
**Key:** owner

    **Value:** tabbank

    **Key:** environment

    **Value:** tabprodaws

    **Key:** Name

    **Value:** sectigo-private

    **Key:** managed-by

    **Value:** terraform

  **EBSVolumes:** 
**VolumeId:** vol-00b9df3d647f71e4f

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 100

    **Throughput:** None

    **SizeGiB:** 8

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 1372.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1237.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 1589.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 515.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 62.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 11.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 605.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 330.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 1883.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 23234.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 26773.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 37577.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 29647.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 32705.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 31235.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 29527.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 23369.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 27230.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 28160.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 30265.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 26576.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 27365.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 24253.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 43237376.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 28930048.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 19181568.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 17379328.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 1163264.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 45056.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 159744.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 7192576.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 5828608.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 36720640.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 45056.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 482467840.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 553574400.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 742838272.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 434429952.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 407523328.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 397791232.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 654913536.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 133361664.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 711020544.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 280940544.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 438079488.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 854167552.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 147935232.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 360964096.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 0.38550257893683687

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 0.38897535709753284

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 0.4097211994145364

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 0.3842151712993713

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 0.3723602412793992

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 0.3699496830426904

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 0.37782916069048156

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 0.3616771328842803

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 0.3885937807120242

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 0.37766041499135455

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 0.376145073376072

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 0.4057065768363937

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 0.36166642806467947

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 0.37292567315780906

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 11570.988194444444

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 10539.045170257123

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 8197.195697432338

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 5685.236805555555

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 1808.9673611111111

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 940.950660180681

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 6052.716666666666

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 645.3972222222222

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 10817.500694444445

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 614.8429464906185

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 11445.60625

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 3784.7965277777776

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 616.1763888888889

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 1023.675487465181

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 280.05902777777777

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 320.67546907574706

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 297.5024288688411

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 271.4840277777778

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 247.72152777777777

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 238.12161223071578

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 278.59166666666664

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 230.9013888888889

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 311.07430555555555

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 225.10910354412786

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 283.36041666666665

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 256.58125

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 221.71597222222223

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 238.08286908077994

  **InstanceId:** i-0e9fc23d12c750ae8

  **InstanceType:** r7a.large

  **State:** stopped

  **LaunchTime:** 2023-09-14 19:41:54+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.9

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-00113d11b61e25a77

    **GroupName:** launch-wizard-6

  **Tags:** 
**Key:** Name

    **Value:** fgfgfg

  **EBSVolumes:** 
**VolumeId:** vol-095c6cee7ea6d8bb0

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 8

    **Utilization:** 
**VolumeReadOps:** 


      **VolumeWriteOps:** 


      **VolumeReadBytes:** 


      **VolumeWriteBytes:**

  **Utilization:** 
**CPU:** 


    **NetworkIn:** 


    **NetworkOut:**

  **InstanceId:** i-0d58304d5cbfcb943

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:14:23+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.37

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-ba9ea2a6-d1a5-eebe-8e98-278246e770e0

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

  **EBSVolumes:** 
**VolumeId:** vol-0a605417169fdb4e4

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 12.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1401.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 2054.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 41.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 239.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2504.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 1451024.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 875831.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 1006378.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 363670.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 242301.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 178633.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 1118333.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1034324.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 1462388.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 1326718.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 880440.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 187715.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 171755.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1531151.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 278528.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 98304.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 454656.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 163840.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 63873024.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 12804096.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 1404928.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 10035200.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 12288.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 19140608.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 97750513664.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 54692639232.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 55474759168.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 11616409088.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 6688072704.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2087508480.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 52257463808.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 51029965824.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 38768530944.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 38219455488.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 28253258752.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3632773632.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 2272184832.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 44542957568.0

    **VolumeId:** vol-0bab267937ab2e3d3

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 16682.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 19269.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 9987.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 19328.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 17546.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 10764.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 11886.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 16207.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 48232.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 3926.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 7325.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 2056.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 8863.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 6893.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 6117.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2782.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 6747.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 27309.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 198888448.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 278617088.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 50890752.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 279165952.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 258611200.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 212632576.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 173893632.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 246536192.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 576985088.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 22999040.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 161857536.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 11137024.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 220110848.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 248934400.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 250671104.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 17235968.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 254623744.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1710243840.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 1.978360932508331

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 1.9425301426860715

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 1.8296608642857024

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 1.6904571726520727

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 1.5584039017800655

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 1.577866887079222

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 1.949570649688789

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 2.076204913646903

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2.0441630463303304

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 1.8660659918597235

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 1.8410409245797603

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 1.5804699068219488

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 1.6056944416485979

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 2.0184675277300665

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 19205944.618055556

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 14453524.761805555

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 11159577.846527778

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 5671144.651388889

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 5051321.936805556

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 4429731.100694444

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 7997638.043055556

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 11235146.459722223

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 8018820.198611111

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 7187912.384989576

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 6829866.346527778

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 4558230.404166667

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 4319671.520833333

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 8748337.374739764

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 13434903.040277777

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 13324824.339583334

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 13140434.326388888

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 13006836.155555556

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 12235461.933333334

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 11745930.066666666

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 12311154.091666667

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 12628805.30138889

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 13369329.455555556

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 12836911.437109103

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 12595442.929861112

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 11676022.168055555

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 11376166.997916667

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 13602565.208882721

  **InstanceId:** i-0eca70770ceafcc65

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:14:23+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.28

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-ba9ea2a6-d1a5-eebe-8e98-278246e770e0

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

  **EBSVolumes:** 
**VolumeId:** vol-03adbba251f33491b

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 169.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 1735.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 3627.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 28.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 217.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 338.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 718341.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 352197.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 423798.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 651854.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 169421.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 150647.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 678698.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1391515.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 1065245.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 1264857.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 1058226.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 147451.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 148956.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 489651.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 839680.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 102400.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 22982656.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 54267904.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 1724416.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2629632.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 20480.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1556480.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 43924649984.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 18374330368.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 23860139520.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 42770668032.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 3654748672.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2042811392.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 37116261888.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 54480966656.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 47051601920.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 44306388480.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 45757680128.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 1981919744.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 1991411712.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 23166361600.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 17.251938585439575

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 17.288946668381808

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 17.385739997621464

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 17.508287872143434

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 16.919252836157618

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 16.785702781209277

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 17.171945300054443

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 17.516198276195894

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 17.30540275108982

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 17.520950474160376

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 17.12243711752569

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 16.68572956440515

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 16.492403919130876

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 17.09550266152871

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 84460944.31319444

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 80915424.73194444

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 82755004.49271339

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 84347008.36849411

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 76031827.34676859

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 76694819.91111112

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 78355420.52569444

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 84337020.98819445

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 81210640.97152779

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 81572620.59791666

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 79251100.8625

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 74603030.52847221

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 74078908.54791667

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 80221966.96038915

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 31048995.996527776

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 29976426.607638888

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 31583905.852879945

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 30483952.38445524

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 28478256.829047948

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 29452639.254861113

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 28809752.531944446

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 31692288.58263889

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 31113045.986805554

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 31257746.3375

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 29457735.327083334

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 27920380.030555554

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 27246120.01875

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 31089714.345378734

  **InstanceId:** i-00aa6398583a8ee1f

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:14:23+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.125

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-ba9ea2a6-d1a5-eebe-8e98-278246e770e0

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

  **EBSVolumes:** 
**VolumeId:** vol-0d7e585fc34c1ac90

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 169.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 11.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 2150.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 1365.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 2124.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 292.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 314274.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 338100.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 182865.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 274445.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 165175.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 155422.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 517029.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 556966.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 264412.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 572850.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 547360.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 197344.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 152645.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 443599.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 778240.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 1101824.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 40960.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 48668672.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 94908416.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 16146432.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 5079040.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 12862631936.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 15937631232.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 5606372352.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 10841726976.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 4679664128.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3907027968.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 25939531264.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 28388971008.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 12239976448.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 14886904832.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 27523603456.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 7061880832.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 3670535168.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 19948525568.0

    **VolumeId:** vol-012d693c9436d045b

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 100

    **Throughput:** None

    **SizeGiB:** 10

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 10306.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 11187.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 9382.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 8981.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 9080.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 6993.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 9048.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 11774.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 9363.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 9853.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 9105.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 7953.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 7009.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 8527.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 1452662784.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1667293184.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 1187811328.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 1102753792.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 1141227520.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 584196096.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 1096814592.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1787875328.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 1175470080.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 1313357824.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 1122443264.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 819441664.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 572428288.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 984698880.0

    **VolumeId:** vol-057fd65c01518d898

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 202213.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 197923.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 192591.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 190471.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 173864.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 170260.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 206336.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 226497.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 186186.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 188123.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 192539.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 168179.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 163804.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 185496.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 23499522048.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 23111487488.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 22894829568.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 22688116736.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 21798547456.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 21499445248.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 24016781312.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 27162939392.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 21274435584.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 21416914944.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 21371891712.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 20481716224.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 20203823104.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 21159055360.0

    **VolumeId:** vol-0daa890a8338134af

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 3.4599686570699815

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 3.3598021534691997

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 3.2325301857771533

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 3.317454871957413

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 3.223682871010596

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 3.2094247651706276

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 3.4309365732254005

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 3.407185180158021

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 3.1560335731469276

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 3.2169790942849033

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 3.2413023328173054

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 3.136053289817207

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 3.078442279196836

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 3.280337368420993

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 22043180.972222224

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 21683095.380555555

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 20774565.463888887

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 21115529.8

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 20516176.72986111

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 20209680.361805554

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 22290194.30625

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 25519026.267361112

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 19841239.088194445

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 20493739.1625

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 21518638.71369006

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 19147941.89722222

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 18860679.145833332

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 20552604.10138889

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 20067479.52222222

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 19756485.364583332

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 19620868.406944446

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 19401855.034027778

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 19439619.18611111

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 19327961.854166668

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 19781809.864583332

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 20842163.23125

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 18425242.246527776

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 18729527.83263889

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 18493933.548992354

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 18065613.610416666

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 18006899.291666668

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 19019021.089583334

  **InstanceId:** i-09509e569fde614f1

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:15:45+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.90.37

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-01cc91ab06316eb72

    **GroupName:** prodtabeks-node-20230815201205877700000004

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-129e002e-798d-ee14-ae1a-07082073f9b1

    **Key:** kubernetes.io/cluster/prodtabeks

    **Value:** owned

    **Key:** aws:ec2launchtemplate:version

    **Value:** 5

    **Key:** k8s.io/cluster-autoscaler/prodtabeks

    **Value:** owned

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** eks:nodegroup-name

    **Value:** managed-prodtabeks-20231207205602416800000001

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** Blueprint

    **Value:** prodtabeks

    **Key:** aws:eks:cluster-name

    **Value:** prodtabeks

    **Key:** Name

    **Value:** managed-prodtabeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodtabeks-20231207205602416800000001-1ac62308-747d-a404-eed6-604b8a3778e2

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0a30753df7e3648b4

    **Key:** eks:cluster-name

    **Value:** prodtabeks

  **EBSVolumes:** 
**VolumeId:** vol-03ffc26db02d337ec

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 20.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 19.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 254.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 689209.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 683343.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 686094.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 581603.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 357308.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 353287.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 352272.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 353663.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 358247.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 358223.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 355239.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 355996.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 357974.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 355727.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 159744.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 143360.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 5025792.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 98304.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 40960.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 6169296384.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 6110559744.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 6133501440.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 5357437440.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 3558093312.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3539128320.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 3484833280.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 3698471936.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 3953616384.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 3590392832.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 3593599488.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3571503616.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 3590675968.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 3587165696.0

    **VolumeId:** vol-0dd6673b0219d3539

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 3223450.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 3231943.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 3240217.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 3255111.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 3233245.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3232469.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 3246679.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 3260803.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 3241779.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 3223316.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 3412018.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3472520.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 3244747.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 3250043.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 68365860864.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 69116575744.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 69882150912.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 72804712448.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 68822745088.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 68226646016.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 72775434240.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 74445533184.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 74898493440.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 70446473216.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 106180390912.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 120813051904.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 71312564224.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 72236339200.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 4.772035888786304

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 4.729745362277278

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 4.770450219519147

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 4.384877367595952

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 3.41714934314158

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 3.4331018668938458

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 3.486311201797991

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 3.4744156057761044

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 3.4657674077134764

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 3.4489722577295145

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 3.629631857824337

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 3.614594950912929

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 3.4550301514199058

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 3.4856618853876595

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 26756494.1875

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 25808473.00208478

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 26494576.663428176

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 28446826.70972222

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 26204316.250694446

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 27162484.69722222

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 28300254.7685893

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 28282714.781944446

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 28932425.385416668

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 27909727.741666667

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 47705996.152777776

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 53406954.92990979

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 28793212.700694446

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 28414281.593055554

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 31048559.684027776

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 30202835.897845726

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 30686524.57182512

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 32485200.986805554

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 29756512.682638887

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 30651793.666666668

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 31746415.788047254

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 31806185.743055556

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 32661479.530555554

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 31389223.8875

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 50971022.61597222

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 58527725.614156835

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 32206180.184027776

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 31857821.315277778

  **InstanceId:** i-0bd7f8abb69178202

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:11:14+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.107

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-929e8086-7987-c636-a4b0-0daae7660213

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

  **EBSVolumes:** 
**VolumeId:** vol-0a2d8b2d3a0a7d9ac

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 15.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1893.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 168021.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 141018.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 141187.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 141001.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 137776.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 136589.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 322566.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 404662.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 133262.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 157090.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 265793.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 134727.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 132944.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 415557.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 196608.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 360448.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 11411456.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 2996793344.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1229870592.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 1230035968.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 1232942080.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 1188879872.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 1178140672.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 14105753600.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 18212840960.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 1558953472.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2855101440.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 11369355776.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 1150367232.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 1134134784.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 15759088640.0

    **VolumeId:** vol-09bdc53b4a3b8e882

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1419.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 318.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 10077184.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2232320.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 1.6669803164433594

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 1.6664988256285422

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 1.6750150281110208

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 1.6788680874303468

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 1.652184824272227

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 1.6495972618309767

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 1.7343485318679288

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 1.78570263648232

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 1.64119678854368

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 1.6435798721961226

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 1.6713298630458404

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 1.6354976844488327

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 1.636900448180531

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 1.7015960956578886

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 34192875.190972224

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 34131095.05

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 33627560.15416667

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 33066387.000694446

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 31681736.704861112

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 31188575.844444446

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 32691188.532314107

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 33446050.669444446

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 31933795.108333334

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 32089706.34513889

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 31962668.70763889

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 30940229.090972222

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 30541235.278472222

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 32626714.61597222

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 2073381.53125

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 2088446.548611111

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 2079572.4395833334

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 2068645.69375

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2023103.23125

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2005826.2902777777

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 2045987.576789437

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 2099038.103472222

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2018194.5131944444

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 2022407.3659722223

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 2017707.1541666666

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 1995904.7916666667

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 1986385.5506944444

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 2045284.2354166666

  **InstanceId:** i-095a8c2cf59c995e7

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:07:07+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.11

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-8cb4143f-662f-ee2f-2c10-8300c9d38e46

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** Name

    **Value:** managed-prodinfraeks

  **EBSVolumes:** 
**VolumeId:** vol-0eecc78db55793398

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 8248.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1176.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 623.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 123.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 385.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 49.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 149.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 6237.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 4338.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2891.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 2245.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 104.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 20.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 4480.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 1158166.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 664009.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 676953.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 873078.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 255046.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 174356.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 837011.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 992649.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 546258.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 530428.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 819205.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 179781.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 172306.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 778510.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 146325504.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 60375040.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 27250688.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 2424832.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 12480512.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 974848.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 5332992.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 142639104.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 76701696.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 49385472.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 45965312.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 1191936.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 745472.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 66093056.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 62986612736.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 29517175296.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 31689190400.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 45358318080.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 7191757312.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2184142336.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 35714000896.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 41707871744.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 24349126144.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 19338002944.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 41145577472.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 2621864960.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 1984788480.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 31103832576.0

    **VolumeId:** vol-0c9ccc8b0259cb33f

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 1201.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 2582.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 7396.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 3001.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 8955.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 6661.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 442.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 3174.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 2981.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 12422.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 3332.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 35923.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 10494976.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 24369152.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 276552704.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 26920960.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 75532288.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 127473664.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 2871296.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 398954496.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 21061632.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 902090752.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 18063360.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1989980160.0

    **VolumeId:** vol-07dd743750e581cb7

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 200

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 14.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 10.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 90935.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 91755.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 95152.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 90748.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 88253.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 91580.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 90066.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 96384.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 91917.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 89357.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 89465.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 93581.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 87630.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 89217.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 57344.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 40960.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 12288.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 49152.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 10338185216.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 10316976128.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 11141386240.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 10268798976.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 10090582016.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 10930262016.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 10416390144.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 11546808320.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 10743087104.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 10116444160.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 10153492480.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 10858475520.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 9837674496.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 9903407104.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 3.4945220271842667

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 3.376651766508599

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 3.3145315199721765

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 3.3870625931082152

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2.973923617041237

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2.960447855751638

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 3.4803517057462767

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 3.6396655299723113

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 3.2165187257905763

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 3.2550447258956714

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 3.282308990230758

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 3.0721968268541016

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 3.015353050075526

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 3.3088619145142952

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 27300490.055555556

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 22972369.68979875

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 23580929.995138887

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 25714188.25

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 20623513.54027778

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 20269272.49097222

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 23943571.600694444

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 29039273.753300905

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 21774828.0125

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 21578248.89652778

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 22762336.91388889

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 19651159.588888887

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 19647242.808895066

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 22685320.06875

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 14033014.500694444

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 14408608.690492714

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 13861054.090972222

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 13638754.358333332

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 12439465.168055555

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 12330439.168055555

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 12771613.409027778

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 13499745.169562196

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 12915431.986111112

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 13465635.659722222

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 12455333.54236111

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 12200089.578472223

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 12001094.515635857

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 13578145.63125

  **InstanceId:** i-0edcf02aea7e8e46c

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:18:42+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.90.15

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-01cc91ab06316eb72

    **GroupName:** prodtabeks-node-20230815201205877700000004

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-2c3e9c15-e607-442d-2412-a3aa21335d3a

    **Key:** Blueprint

    **Value:** prodtabeks

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0a30753df7e3648b4

    **Key:** Name

    **Value:** managed-prodtabeks

    **Key:** k8s.io/cluster-autoscaler/prodtabeks

    **Value:** owned

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodtabeks-20231207205602416800000001-1ac62308-747d-a404-eed6-604b8a3778e2

    **Key:** eks:cluster-name

    **Value:** prodtabeks

    **Key:** kubernetes.io/cluster/prodtabeks

    **Value:** owned

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** eks:nodegroup-name

    **Value:** managed-prodtabeks-20231207205602416800000001

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:eks:cluster-name

    **Value:** prodtabeks

    **Key:** aws:ec2launchtemplate:version

    **Value:** 5

  **EBSVolumes:** 
**VolumeId:** vol-0cd0eacef7a9d116b

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 26.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 91.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 321.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 1052691.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1051181.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 1054122.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 866764.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 327965.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 315163.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 316293.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 315683.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 318846.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 317451.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 315046.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 315767.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 315109.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 315661.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 20480.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 454656.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 2351104.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 131072.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 9515008.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 249856.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 364544.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 8248343552.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 8248375296.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 8276403200.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 6867182592.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 2961113600.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2936747520.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 2939512320.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 3090134528.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 3357656064.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2960966656.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 2916003328.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 2978756608.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 2921635328.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2942333952.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 4.2731724588681965

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 4.247217689510683

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 4.233527854301602

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 3.6516238785632646

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2.043386456183738

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2.0792650935788974

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 2.0640891273638458

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 2.05129633700785

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2.052924798632449

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 2.0342407575294463

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 2.0419490432546517

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 2.048037037876278

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 2.043381962660107

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 2.0601851101680975

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 7789615.728472223

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 7494960.198611111

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 7874124.360416667

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 7779820.317361111

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 7214549.522916666

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 7563850.351388888

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 7266690.645138889

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 7419000.709722222

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 7571534.455555555

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 6336092.350694444

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 7093280.51664355

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 8649835.81514941

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 7639067.059027778

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 7807827.775694445

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 11818705.435416667

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 11521335.035416666

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 11917166.083333334

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 11471438.127083333

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 10088242.576388888

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 10468983.564583333

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 10159829.425

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 10276126.355555555

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 10414177.913194444

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 9171541.920138888

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 9954755.198335646

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 11604179.896455873

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 10548372.384027777

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 10714308.279166667

  **InstanceId:** i-088aa4d1daddb1779

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:07:07+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.222

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-ae36343d-ee85-6cad-2612-8122c291f16a

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

  **EBSVolumes:** 
**VolumeId:** vol-01fb1771a1c77ee1f

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 899.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 7.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 230663.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 274058.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 223931.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 239800.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 188749.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 182324.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 608414.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 566725.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 313454.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 301033.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 426255.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 205234.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 181458.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 209605.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 143360.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 20926464.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 655360.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 417792.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 9758327808.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 12546765312.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 8856426496.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 10107866112.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 4905824256.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 4792754688.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 36225512960.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 32830158336.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 15888463360.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 13367187968.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 23284301824.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 6311135744.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 4566745600.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 7757625856.0

    **VolumeId:** vol-0091077b842be2710

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 100

    **Throughput:** None

    **SizeGiB:** 10

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 5269.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 5572.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 4830.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 4659.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 4796.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3907.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 4675.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 5812.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 4796.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 5018.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 4621.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 4304.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 3871.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 4460.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 631914496.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 724992000.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 508592128.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 478646272.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 516616192.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 270680064.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 480403456.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 756150272.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 506552320.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 572420096.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 476090368.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 373256192.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 261169152.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 431132672.0

    **VolumeId:** vol-0dfb6665655ae8c63

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 10

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

    **VolumeId:** vol-0e71d20dbcbc9e726

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1293.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 10875.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 275.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 9826.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 9511936.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 247028736.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1867776.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 387657728.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 11.514866950553564

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 11.486810467468548

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 11.222384339479913

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 10.96802963693534

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 10.916616705548506

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 10.880552086511342

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 11.231873707038995

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 11.403000567782575

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 11.115268511988248

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 11.43102286518648

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 11.048333028694216

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 10.860303258806912

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 10.824356122961877

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 11.090859028338377

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 103261864.61805555

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 102930428.10902777

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 101256946.08819444

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 99176908.35347222

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 94890971.70833333

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 93234914.91603054

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 97378729.30159833

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 100062173.11458333

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 96231460.27638888

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 97230757.81666666

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 95773117.55486111

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 92741340.77430555

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 91078630.92847222

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 93432653.21612231

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 111393385.88055556

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 111084232.75

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 109398709.94027779

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 107433516.3298611

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 103252716.63333334

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 101782210.50589868

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 103705911.65114664

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 104397048.59444444

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 103933505.29097222

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 104351176.50416666

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 102324305.56111111

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 100734648.67569445

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 99325343.1701389

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 101580175.26129256

  **InstanceId:** i-010c0b3b00f1a1335

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:07:07+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.181

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-ae36343d-ee85-6cad-2612-8122c291f16a

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

  **EBSVolumes:** 
**VolumeId:** vol-025236a579f99a0b3

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 14.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 2453.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 171437.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 194335.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 171008.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 172978.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 178540.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 167165.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 211922.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 226887.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 167567.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 164214.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 241034.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 163579.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 162211.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 163469.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 12288.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 1114112.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 87277568.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 81920.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 69632.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 2306500608.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 4034914816.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 2308380160.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 2338875904.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 3046690304.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2258276352.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 5688512512.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 6824504320.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 2621314048.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2200189440.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 7863133184.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 2189049344.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 2181750272.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2204291072.0

    **VolumeId:** vol-022214e261e1f16ee

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 10

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 2190.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 2182.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 2185.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 2188.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 2188.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2181.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 2178.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 2476.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 2210.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2251.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 2246.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 2198.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 2199.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2235.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 17420288.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 17424384.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 17432576.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 17432576.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 17436672.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 17432576.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 17432576.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 20402176.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 17625088.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 18001920.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 17813504.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 17420288.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 17420288.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 17731584.0

    **VolumeId:** vol-0b8967c3802401ec9

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

    **VolumeId:** vol-0ec548da7ab16590d

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 200158.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 196247.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 190922.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 188733.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 172018.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 168843.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 202668.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 221937.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 182720.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 184710.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 190186.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 165399.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 162316.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 184073.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 23471378432.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 23134208000.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 22945992704.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 22667993088.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 21763960832.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 21485678592.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 23928655872.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 27146706944.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 21282308096.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 21384884224.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 21399224320.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 20419547136.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 20167073792.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 21111271424.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 3.2102489168521737

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 3.18861086633825

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 3.1647407608308304

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 3.1416793868917243

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 3.134047395247685

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 3.1233669028526365

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 3.1506967546311513

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 3.159541736352564

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 3.0983854142439293

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 3.0872326210050844

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 3.1517487328683753

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 3.064285886294251

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 3.0648680569152935

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 3.0937592592080154

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 58593223.584027775

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 58402522.19375

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 57656860.239583336

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 56910506.39444444

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 55314728.079166666

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 54634879.22152778

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 56997328.86657401

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 60031234.31944445

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 54799580.39513889

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 54981748.01527778

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 54837017.75625

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 53414634.52222222

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 52901527.503472224

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 54143659.87361111

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 14850936.130555555

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 14695571.898611112

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 14572966.38611111

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 14439956.1

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 14270619.731944444

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 14148908.429861112

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 14804536.56914524

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 15737141.579166668

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 13741079.260416666

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 13742877.824305555

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 13752318.097222222

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 13447025.678472223

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 13409030.249305556

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 13663156.591666667

  **InstanceId:** i-0d34a211ac0623e10

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:05:22+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.90.174

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-01cc91ab06316eb72

    **GroupName:** prodtabeks-node-20230815201205877700000004

  **Tags:** 
**Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodtabeks-20231207205602416800000001-1ac62308-747d-a404-eed6-604b8a3778e2

    **Key:** eks:cluster-name

    **Value:** prodtabeks

    **Key:** Blueprint

    **Value:** prodtabeks

    **Key:** Name

    **Value:** managed-prodtabeks

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-38362a8c-792d-6e34-0e18-2f0a43892654

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0a30753df7e3648b4

    **Key:** kubernetes.io/cluster/prodtabeks

    **Value:** owned

    **Key:** aws:eks:cluster-name

    **Value:** prodtabeks

    **Key:** aws:ec2launchtemplate:version

    **Value:** 5

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** eks:nodegroup-name

    **Value:** managed-prodtabeks-20231207205602416800000001

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** k8s.io/cluster-autoscaler/prodtabeks

    **Value:** owned

  **EBSVolumes:** 
**VolumeId:** vol-0618fd6b4d6594ed4

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 188.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 109.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 1266.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 8.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 59.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 185.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 1147716.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1147644.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 1150683.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 940596.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 402207.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 386486.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 387795.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 381741.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 382969.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 386875.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 386731.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 382472.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 384955.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 386116.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 4300800.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 98304.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 974848.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 97849344.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 77824.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 86016.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1110016.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 4874240.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 102400.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 9821157888.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 9846077952.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 9873212416.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 8154807808.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 3530994688.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3521492480.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 3543865344.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 4138036736.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 3530663936.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 3605871104.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 3554198016.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3490702848.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 3528971776.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 3564516864.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 5.613259330993428

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 5.63476827566767

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 5.650563711599336

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 4.70438540861618

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2.473332279325974

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2.46403000211722

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 2.4706261642281797

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 2.483018505007883

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2.4773842679650886

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 2.4874640686601386

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 2.4766111965888067

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 2.4653402312690775

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 2.461699142660578

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 2.4568633991066506

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 10791994.206944445

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 11819110.672916668

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 12832609.423210563

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 11087951.565972222

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 9677611.239583334

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 10011685.646527778

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 11133293.530555556

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 12566276.976388888

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 10866733.402777778

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 11925781.669444444

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 10516078.560416667

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 10058671.927777778

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 10166189.581944445

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 9678507.137595553

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 15831587.882638888

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 16913162.002777778

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 17993041.265462127

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 15717542.710416667

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 12995077.355555555

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 13337681.87986111

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 14510625.153472222

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 15931954.909027778

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 14241284.300694445

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 15361373.8375

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 13875906.83263889

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 13396531.177083334

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 13510396.284722222

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 12998644.525364837

  **InstanceId:** i-0af73fd36f755036b

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:05:22+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.90.136

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-01cc91ab06316eb72

    **GroupName:** prodtabeks-node-20230815201205877700000004

  **Tags:** 
**Key:** Name

    **Value:** managed-prodtabeks

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0a30753df7e3648b4

    **Key:** aws:ec2launchtemplate:version

    **Value:** 5

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:eks:cluster-name

    **Value:** prodtabeks

    **Key:** kubernetes.io/cluster/prodtabeks

    **Value:** owned

    **Key:** eks:cluster-name

    **Value:** prodtabeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodtabeks-20231207205602416800000001-1ac62308-747d-a404-eed6-604b8a3778e2

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-38362a8c-792d-6e34-0e18-2f0a43892654

    **Key:** eks:nodegroup-name

    **Value:** managed-prodtabeks-20231207205602416800000001

    **Key:** k8s.io/cluster-autoscaler/prodtabeks

    **Value:** owned

    **Key:** Blueprint

    **Value:** prodtabeks

  **EBSVolumes:** 
**VolumeId:** vol-09c4a01e207b779d2

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 7.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 14.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 22.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 79.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 66.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 9.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 8.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 8.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 740037.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 739814.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 741022.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 668045.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 429745.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 421483.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 430525.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 428611.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 427909.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 429176.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 429384.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 432417.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 428189.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 428905.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 143360.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 299008.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 311296.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 45056.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 1183744.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 61440.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1019904.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 483328.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 77824.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 163840.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 131072.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 8258434560.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 8345785856.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 8305684992.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 8767987200.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 5855168000.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 5671740928.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 5948968448.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 5948329472.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 6134752256.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 5753993216.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 5853904896.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 5711717376.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 5632915968.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 5710916096.0

    **VolumeId:** vol-052f2d95770ad83b1

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 100

    **Throughput:** None

    **SizeGiB:** 20

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 117954.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 127383.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 153872.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 126099.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 138649.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 100277.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 137673.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 124684.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 126233.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 132995.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 150872.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 153498.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 106746.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 135037.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 65536.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 29831827456.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 31942238208.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 38639443968.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 31728881664.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 35031490560.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 25643515904.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 34715910144.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 31053537280.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 31353634816.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 33356152832.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 37549998080.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 38587031552.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 26974269440.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 33772748800.0

    **VolumeId:** vol-0a8e5c27b36515ba4

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 3221786.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 3233214.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 3245332.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 3258348.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 3238539.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3230566.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 3252353.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 3268816.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 3250876.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 3223060.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 3415119.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3470950.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 3245543.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 3249960.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 68459184128.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 69159866368.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 69955457024.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 72860332032.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 68939677696.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 68287324160.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 72803409920.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 74546778112.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 74971009024.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 70415708160.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 106098827264.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 120911884288.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 71470104576.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 72248557568.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 6.272822041497109

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 6.297462909138191

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 6.27865172432664

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 6.967461807696728

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 5.348152755636612

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 5.23875594462961

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 5.483791166709734

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 5.365330103280225

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 5.618482589800874

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 5.32362000656573

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 5.588775689797852

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 5.437143485486658

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 5.316499604757946

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 5.326338008962738

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 42927619.52222222

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 44815354.51111111

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 47106080.46597222

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 49302222.614583336

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 43559229.00625

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 39511211.48194444

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 48257153.82430556

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 49468073.128472224

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 50915987.30069444

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 45295637.20222376

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 68748597.65625

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 74121265.01944445

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 44025454.08194444

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 47948743.71458333

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 43133970.384722225

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 44667748.05833333

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 43104727.10486111

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 48738401.833333336

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 41885418.63888889

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 40072566.50902778

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 44022619.47083333

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 44532847.505555555

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 42961795.37638889

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 42274493.23766504

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 63078265.92430556

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 70287191.96111111

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 41440310.911805555

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 44069901.93125

  **InstanceId:** i-0dad49f8cfb2a1ed4

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:11:26+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.151

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-06b69637-4685-462f-8410-2ba0cb479a7d

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

  **EBSVolumes:** 
**VolumeId:** vol-0c02a65af8565cd2e

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 2042.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 255.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 14.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 29.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 329.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 3149.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 31.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 432.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 1522.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 8.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1179.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 601500.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 520762.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 325456.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 309631.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 182825.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 180679.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 669398.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 768045.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 505290.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 603807.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 597979.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 186460.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 186930.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 589301.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 21209088.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 7262208.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 57344.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 180224.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 81920.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 7155712.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 96120832.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 360448.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 8536064.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 9650176.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 253952.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 430080.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 18456576.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 20248879104.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 19119003648.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 9960843264.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 8714536448.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 2638731264.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2231514624.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 29581575680.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 32499836416.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 20613572608.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 27612975104.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 21868910080.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 2904115200.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 2553200128.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 25339485696.0

    **VolumeId:** vol-06ee71a1463c63bc8

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 203658.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 198909.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 194851.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 191835.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 175444.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 171757.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 207414.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 228611.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 187701.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 189144.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 194331.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 169166.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 165840.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 188161.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 23554449408.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 23107825664.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 22968193024.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 22687698944.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 21817778176.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 21539475456.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 23998689280.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 27213099008.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 21311197184.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 21430898688.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 21410418688.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 20458082304.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 20215926784.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 21132734464.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 3.038964278401446

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 3.106681764715103

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 2.845662129859674

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 2.866580999303521

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2.7478090933400274

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2.7615625726145243

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 2.96698141689752

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 3.177680474345073

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2.9556115931533427

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 2.845938938038136

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 2.934872547456381

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 2.7998867158351994

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 2.781510387908512

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 3.0551820447361244

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 30518690.243055556

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 30295853.08402778

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 28980734.1875

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 26663181.08611111

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 28260989.780555554

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 25664188.45902778

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 29003483.546527777

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 32869673.497916665

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 27480812.094510075

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 28044302.28125

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 28524417.713194445

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 26620862.73888889

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 27352378.199305557

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 27863812.37638889

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 36691014.463194445

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 36572579.67916667

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 36154775.73263889

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 33849706.225

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 34987724.963194445

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 32199432.9875

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 34235995.09583333

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 39282146.42013889

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 32926612.111188326

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 33690084.13888889

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 33807903.82638889

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 33350600.252777778

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 33835424.20138889

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 32125630.52361111

  **InstanceId:** i-09fe7de44041bad35

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:11:26+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.224

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-06b69637-4685-462f-8410-2ba0cb479a7d

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

  **EBSVolumes:** 
**VolumeId:** vol-0a8c72e5a87edc5e5

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 177593.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 177023.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 176149.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 177282.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 173121.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 172191.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 174363.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 174157.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 173883.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 173660.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 171241.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 171503.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 171832.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 173014.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 102400.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 454656.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 28672.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 4245391360.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 4197083648.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 4152001536.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 4146107904.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 4190979584.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 4169566208.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 4114061312.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 4207328256.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 4389734400.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 4006048768.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 3972221952.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3930749952.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 3940237312.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 4009629696.0

    **VolumeId:** vol-0ae96dc4c6f947fba

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 151

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 1.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 11547.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 12078.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 42732.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 43695.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 44654.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 43586.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 45972.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 40735.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 37460.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 41392.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 41376.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 43138.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 43904.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 39858.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 12288.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 4096.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 2628284416.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 2718130176.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 3098513408.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 3092594688.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 3095695360.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3076268032.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 3117793280.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 2454851584.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 3094585344.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 3069997056.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 2425806848.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3114995712.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 3116466176.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2384027648.0

    **VolumeId:** vol-04f9b43d5a684ec24

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 100

    **Throughput:** None

    **SizeGiB:** 10

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 4241.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 4619.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 3825.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 3708.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 3872.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 2951.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 3678.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 4733.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 3821.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 4075.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 3726.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 3370.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 2949.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 3531.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 592990208.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 687575040.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 471715840.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 442306560.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 486445056.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 241590272.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 441016320.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 714907648.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 470134784.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 534597632.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 442966016.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 346828800.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 236589056.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 393064448.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 2.8526133744085502

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 2.8440034887437227

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 2.8304063409905535

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 2.837856263859233

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2.821600702465466

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2.8657952512946703

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 2.833946561143154

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 2.810299733584944

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2.7876573844370207

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 2.7945010170433937

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 2.7805750230505204

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 2.7562780215343303

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 2.746318398181709

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 2.7387170887353274

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 22538923.565972224

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 22954136.972916666

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 21701043.693055555

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 23426292.66527778

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 21264696.58263889

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 22519027.833333332

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 22026814.421820708

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 20637599.9

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 21530349.89722222

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 21201158.58263889

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 20868465.12638889

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 21064676.484722223

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 20643098.83611111

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 20196811.479166668

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 22810661.45902778

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 23174428.780555554

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 21899852.50763889

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 23581750.524305556

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 21528978.425

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 22819132.445833333

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 22229594.404447533

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 20732880.505555555

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 21752973.929166667

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 21386755.402777776

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 21136532.761805557

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 21289811.261805557

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 20913775.142361112

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 20506515.418055557

  **InstanceId:** i-0592b2b69c089d5cc

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:19:23+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.221

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-38948206-d1a7-663e-ae1a-278893827c2d

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

  **EBSVolumes:** 
**VolumeId:** vol-09eef572e3ee62e11

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 63.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 195.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 202.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 10.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 13.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 7.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 48.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 514623.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 702189.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 301275.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 360511.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 232121.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 204233.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 662062.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1142436.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 502803.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 526986.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 707112.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 230140.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 206820.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 379345.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 2859008.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 131072.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 12288.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 118784.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 262144.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 131072.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 1921024.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 1941504.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 647168.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 110592.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 495616.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 647168.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 2113536.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

        **Sum:** 19053161472.0

        **Timestamp:** 2025-01-29T03:41:00+00:00

        **Sum:** 11418177536.0

        **Timestamp:** 2025-01-30T03:41:00+00:00

        **Sum:** 6821893120.0

        **Timestamp:** 2025-01-31T03:41:00+00:00

        **Sum:** 10497399808.0

        **Timestamp:** 2025-02-01T03:41:00+00:00

        **Sum:** 4339953152.0

        **Timestamp:** 2025-02-02T03:41:00+00:00

        **Sum:** 3449455104.0

        **Timestamp:** 2025-02-03T03:41:00+00:00

        **Sum:** 25575404032.0

        **Timestamp:** 2025-02-04T03:41:00+00:00

        **Sum:** 37122126336.0

        **Timestamp:** 2025-02-05T03:41:00+00:00

        **Sum:** 22184561664.0

        **Timestamp:** 2025-02-06T03:41:00+00:00

        **Sum:** 24149377024.0

        **Timestamp:** 2025-02-07T03:41:00+00:00

        **Sum:** 34022380544.0

        **Timestamp:** 2025-02-08T03:41:00+00:00

        **Sum:** 4153074688.0

        **Timestamp:** 2025-02-09T03:41:00+00:00

        **Sum:** 2876506624.0

        **Timestamp:** 2025-02-10T03:41:00+00:00

        **Sum:** 12115929088.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 2.377504683463201

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 2.499566330223825

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 2.344121589326899

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 2.34974877463499

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 2.261731482318082

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 2.256917823520618

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 2.566301210731141

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 2.7485510526832737

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 2.349045169623836

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 2.356589126555629

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 2.447335666616683

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 2.2634224805032406

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 2.24749074412879

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 2.353681675458734

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:41:00+00:00

      **Average:** 8799546.840166783

      **Timestamp:** 2025-01-29T03:41:00+00:00

      **Average:** 8918712.990972223

      **Timestamp:** 2025-01-30T03:41:00+00:00

      **Average:** 8019675.365277777

      **Timestamp:** 2025-01-31T03:41:00+00:00

      **Average:** 8312680.458333333

      **Timestamp:** 2025-02-01T03:41:00+00:00

      **Average:** 7521314.530555556

      **Timestamp:** 2025-02-02T03:41:00+00:00

      **Average:** 7365467.9375

      **Timestamp:** 2025-02-03T03:41:00+00:00

      **Average:** 10042833.534722222

      **Timestamp:** 2025-02-04T03:41:00+00:00

      **Average:** 13989536.605281446

      **Timestamp:** 2025-02-05T03:41:00+00:00

      **Average:** 9259531.570833333

      **Timestamp:** 2025-02-06T03:41:00+00:00

      **Average:** 8937015.591666667

      **Timestamp:** 2025-02-07T03:41:00+00:00

      **Average:** 9741558.497222222

      **Timestamp:** 2025-02-08T03:41:00+00:00

      **Average:** 7297067.406944444

      **Timestamp:** 2025-02-09T03:41:00+00:00

      **Average:** 7083189.460041695

      **Timestamp:** 2025-02-10T03:41:00+00:00

      **Average:** 7938067.626388889

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 23954135.528144546

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 24709522.109027777

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 23998336.288194444

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 23745522.508333333

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 22845588.888194446

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 22637495.236111112

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 23568300.674305554

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 25062747.5476025

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 23251371.692361113

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 22873250.899305556

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 22886753.858333334

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 22273388.549305554

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 22021467.558026407

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 22120267.701388888

  **InstanceId:** i-03f00ac4181d73911

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:15:54+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.90.139

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-01cc91ab06316eb72

    **GroupName:** prodtabeks-node-20230815201205877700000004

  **Tags:** 
**Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** aws:ec2launchtemplate:version

    **Value:** 5

    **Key:** eks:nodegroup-name

    **Value:** managed-prodtabeks-20231207205602416800000001

    **Key:** Name

    **Value:** managed-prodtabeks

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0a30753df7e3648b4

    **Key:** eks:cluster-name

    **Value:** prodtabeks

    **Key:** Blueprint

    **Value:** prodtabeks

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-ae1c3c35-4c87-6eaf-061a-8b8864eae812

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodtabeks-20231207205602416800000001-1ac62308-747d-a404-eed6-604b8a3778e2

    **Key:** k8s.io/cluster-autoscaler/prodtabeks

    **Value:** owned

    **Key:** kubernetes.io/cluster/prodtabeks

    **Value:** owned

    **Key:** aws:eks:cluster-name

    **Value:** prodtabeks

  **EBSVolumes:** 
**VolumeId:** vol-0873d24f2f0f97208

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 49.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 62.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 19.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 572.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 12.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 117.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 22.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 9.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 22.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1235950.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1234875.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 1236847.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 993645.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 372908.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 362934.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 353469.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 362720.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 367271.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 365402.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 362851.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 364184.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 364935.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 366497.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1499136.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 958464.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 385024.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 11657216.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 307200.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 20480.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1761280.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 106496.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 270336.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 241664.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 290816.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 40960.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 704512.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 9507043840.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 9483401216.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 9458388480.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 7723234304.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 3293540352.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 3268594176.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 3244523520.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 3445455360.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 3707521536.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 3289029632.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 3283854848.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 3306907136.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 3296804352.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 3288481792.0

    **VolumeId:** vol-052894fb666f5376f

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 10

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 30.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 7.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 72791.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 81875.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 81299.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 84024.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 80634.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 80192.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 82616.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 82721.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 82220.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 81264.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 83313.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 80889.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 81107.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 81520.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 196608.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 49152.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 694743040.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 786796544.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 780746752.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 807510016.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 773517312.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 770179072.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 791375872.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 794320896.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 788426752.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 781463552.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 800600064.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 774332416.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 774881280.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 781590528.0

    **VolumeId:** vol-0946d72aacd9b9e88

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 200

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 71205.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 72954.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 75708.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 72594.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 69062.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 71131.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 70338.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 69881.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 71265.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 69940.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 68733.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 71010.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 69799.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 69373.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 6211194880.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 6613176320.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 7180963840.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 6540718080.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 6157520896.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 6622961664.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 6150258688.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 6082760704.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 6490157056.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 6014480384.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 6021038080.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 6530834432.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 6063517696.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 6052356096.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 6.083333288036805

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 6.085931816418306

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 6.038788254470574

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 5.262159643013354

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 3.3353588050890157

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 3.3498588886242016

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 3.363489600162874

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 3.376752448812945

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 3.3632661828444865

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 3.3573053472897065

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 3.391329942035123

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 3.3722140945180685

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 3.370221127127291

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 3.366801004852096

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 23676153.13611111

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 23978506.12638889

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 23416406.4125

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 23013991.82928522

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 19951968.49861111

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 19418988.152083334

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 18421204.925

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 19392447.00625

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 21012959.002083335

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 19873376.27222222

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 22073485.216817234

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 21938103.710416667

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 19509998.151388887

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 18801706.91597222

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 34893069.89791667

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 35420560.11319444

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 34749650.95694444

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 34016127.42192922

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 30091918.608333334

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 29577204.42986111

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 28614534.4375

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 30046141.95972222

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 30858799.63402778

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 29784090.00902778

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 32138489.273106325

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 32032196.124305554

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 29523053.710416667

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 28732005.755555555

  **InstanceId:** i-00be5d750430b38f0

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-12-19 17:37:00+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.148

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-269e1e1d-6ca7-460d-8c18-0b0806b8a6c7

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

  **EBSVolumes:** 
**VolumeId:** vol-01b13b5d267fb31d3

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1222.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 971.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 98.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 5948.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 1.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1202550.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1078553.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 953069.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 535633.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 175200.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 128959.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 1130183.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 945961.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 1341860.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 814403.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 1136344.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 187486.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 132319.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 490636.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 8773632.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 454656.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 61440.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 196608.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 28123136.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 3428352.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 102653952.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 77824.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 446464.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 4096.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 83452168192.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 76157105152.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 71583294464.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 28851895808.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 4445829632.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 1017981952.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 72089975808.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 56223972352.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 46038028288.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 48013165056.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 52864542208.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 5172298240.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 1055585792.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 25682880512.0

    **VolumeId:** vol-0481663e0271f7cbf

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 8139.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 15042.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 11639.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 19970.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 9938.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 12976.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 36233.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 4136.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 4181.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1634.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 3977.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 6967.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 4887.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 2421.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 3245.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 27844.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 811.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 816.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 42653696.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 231418880.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 167479296.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 329723904.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 164272128.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 88656896.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 476588032.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 21599232.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 21791744.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 8867840.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 25300992.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 212418560.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 30416896.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 14487552.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 20070400.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 1276833792.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 4104192.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 4763648.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 1.3972895222149648

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1.355799154742472

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1.2850786685164886

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1.3800604786258373

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1.1481689454173865

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1.0826875021891493

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1.526068523306411

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1.5870769403937355

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1.4515048770605425

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1.488670371344702

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1.3180282177871547

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1.0331343957960997

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1.0639594846942135

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1.296633586076267

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 10017516.055594163

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 7314209.225

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 8998115.53611111

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 2917984.698611111

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 847198.0381944445

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 643223.6041666666

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 6010385.325694445

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 6332282.859722222

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 4206011.339583334

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 4811559.903472222

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 5302206.013888889

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1041429.9923558027

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 608052.2347222222

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 2463796.3493055557

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 841936.9061848506

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1296397.5340277778

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1076464.463888889

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 750081.575

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 731575.23125

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 692833.4590277778

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 852838.6868055556

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 2153935.857638889

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 2259954.29375

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 2127273.535416667

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1172534.9388888888

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 649681.2863099375

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 683406.317361111

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 733586.4006944444

  **InstanceId:** i-0230b130570aee25e

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-12-24 21:53:32+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.166

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-b2beaa8c-f30d-eeb4-0e92-87029339ca94

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

  **EBSVolumes:** 
**VolumeId:** vol-0fb1fa1927be53c40

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 2125.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 19.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 64.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 3407.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 679.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 713215.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1075539.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 861471.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 406663.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 127220.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 126305.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 683028.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 734171.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 740892.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 799034.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 1589416.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 165324.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 125381.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 843999.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 270336.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 33906688.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 2060288.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 745472.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 106496.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 21286912.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 7835648.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 46114938368.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 75984312320.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 48257376256.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 21784242176.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 1023662592.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 1010673664.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 40532149760.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 47708339712.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 23268438528.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 49335087104.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 69585313280.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 4319395328.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 990079488.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 53648434176.0

    **VolumeId:** vol-0e7c5387692b8b034

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 5413.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 10953.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 5474.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 5474.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 7915.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 5438.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 5486.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1339.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 2682.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 1332.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 1337.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 5152.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 1475.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 1440.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 27575296.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 55638016.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 27788288.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 27784192.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 107697152.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 27751424.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 27911168.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 6774784.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 14991360.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 8093696.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 8110080.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 178003968.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 8400896.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 8110080.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 1.2565520164262045

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1.5088605924375533

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1.4612271445181169

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1.331959455715584

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1.075519715370446

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1.0682534722222259

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1.40430120584229

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1.3366620484077794

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1.3655393492552634

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1.4091481193815703

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1.5193829407093788

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1.1448808016298262

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1.0883101816866407

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1.3734759323877141

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 4333730.421527778

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 8277297.530555556

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 4712535.942361111

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 2973469.9833333334

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 663010.3847222222

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 642851.5590277778

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 5056811.772916666

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 6746516.096594858

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 2401614.4479166665

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 4812310.539583334

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 5926495.989590562

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 812925.0374739764

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 610660.4819444445

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 4526818.866666666

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 754952.5520833334

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1332766.4361111112

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 798304.7944444445

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 752883.1729166667

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 689431.9666666667

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 686949.6333333333

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 746018.6118055555

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1178885.980542043

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1400256.1590277778

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1928321.5666666667

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1458115.9375433726

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 714154.3122831368

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 683112.9847222222

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 972568.4604166667

  **InstanceId:** i-099831e51f7b5cbc1

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-08-27 15:12:38+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.90.40

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-01cc91ab06316eb72

    **GroupName:** prodtabeks-node-20230815201205877700000004

  **Tags:** 
**Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodtabeks-20231207205602416800000001-1ac62308-747d-a404-eed6-604b8a3778e2

    **Key:** eks:cluster-name

    **Value:** prodtabeks

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-ae94369f-e6a5-6e2d-8eb8-238a3f24b1d6

    **Key:** Blueprint

    **Value:** prodtabeks

    **Key:** Name

    **Value:** managed-prodtabeks

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0a30753df7e3648b4

    **Key:** kubernetes.io/cluster/prodtabeks

    **Value:** owned

    **Key:** aws:eks:cluster-name

    **Value:** prodtabeks

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** aws:ec2launchtemplate:version

    **Value:** 5

    **Key:** eks:nodegroup-name

    **Value:** managed-prodtabeks-20231207205602416800000001

    **Key:** k8s.io/cluster-autoscaler/prodtabeks

    **Value:** owned

  **EBSVolumes:** 
**VolumeId:** vol-094a800180897aa01

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 13.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 220.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 468.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 3813.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 24.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 7.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 99.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 208.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 9.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 40.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 7.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1180361.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1189903.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 1185852.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 975058.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 451952.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 436714.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 412878.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 391886.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 389603.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 390788.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 389585.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 388902.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 392443.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 393274.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 483328.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 2977792.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 8904704.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 68927488.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 344064.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 118784.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 4100096.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 2367488.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 233472.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 49152.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 856064.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 12288.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 32768.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 81920.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 10450575872.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 10632857088.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 10557242880.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 10281659904.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 5225084928.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 4988741120.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 5042338304.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 4778312704.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 4942584832.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 4546717696.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 4623163392.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 4430494208.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 4516682752.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 4507771904.0

    **VolumeId:** vol-039055dcce4a41b75

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 100

    **Throughput:** None

    **SizeGiB:** 20

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 183.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 0.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 343942.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 391922.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 666861.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 362527.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 834083.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 744951.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 565743.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 263639.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 123943.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 130154.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 148357.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 151071.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 104566.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 132538.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 749568.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 12288.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 0.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 85666942976.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 94294740992.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 163110387712.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 90737840128.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 212961402880.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 191843430400.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 144148164608.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 66179727360.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 30887514112.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 32893517824.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 37088735232.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 38122037248.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 26509250560.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 33296797696.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 7.495252363305931

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 7.5977857972494185

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 7.586096993037235

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 7.849171283574588

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 5.17233966147254

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 5.0929886988182655

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 4.9691478602857675

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 4.363016250522944

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 4.241745204425002

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 3.919297495679582

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 4.038414235624139

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 3.9040405715885513

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 3.9422744889739905

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 3.941374592662118

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 48064304.66458333

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 49426465.86666667

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 59900000.10625

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 51986001.73263889

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 55637086.69513889

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 52426065.010416664

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 51880324.19513889

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 42778386.132036135

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 44757556.00902778

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 37168969.70069444

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 42778120.51527778

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 39717446.43055555

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 38244387.994444445

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 38872468.86597222

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 21327826.372222222

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 21677173.19722222

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 29004108.561805554

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 26168374.81111111

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 33196081.102083333

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 32226005.86527778

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 26517177.061805554

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 17186808.558026407

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 16094089.352083333

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 13712562.820833333

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 17116461.776388887

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 13990997.673611112

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 15354730.297916668

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 14577736.299305556

  **InstanceId:** i-09d62cbeca18801a3

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-12-13 19:48:25+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.114

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-acbcbe1d-e425-eead-8c92-2ba852e50e75

  **EBSVolumes:** 
**VolumeId:** vol-0b0fab7fd9c7a7e7a

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 299.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 254.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 193.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 10.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 10.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 8.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 2996.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 87.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 5482.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 9896.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1217694.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1419477.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 1048847.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 553661.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 166369.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 121513.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 723659.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1562422.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 608064.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 669511.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 1284263.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 182409.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 122287.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 904701.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 9465856.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 7352320.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 3444736.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 634880.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 16384.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 217088.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 401408.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 61329408.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 1519616.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 113115136.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 643072.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 16384.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 230920192.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 80501535744.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 106030292480.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 48699005440.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 35865822720.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 4355893760.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 943035392.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 43112416256.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 71142901760.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 41346795008.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 43650809344.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 64133725184.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 6009470464.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 929930240.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 53975504384.0

    **VolumeId:** vol-02d4939593067b000

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 8891.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 3626.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 3057.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 2158.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 3661.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 2390.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 5026.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 17461.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 16648.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 4956.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 1181.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1070.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 5356.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 822.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 4881.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 22522.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 120189952.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 90919936.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 144856064.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 55243776.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 90698752.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 22185984.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 105445376.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 540778496.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1806778368.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 195428352.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 9719808.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 8384512.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 183771136.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 5029888.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 225976320.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 2027716608.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 1.6189618756672537

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1.5051735687751677

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1.3569918863412516

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1.2064074246292937

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1.0842326366390003

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1.073179396923098

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1.4850777700298763

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1.781177050846624

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1.1920833484774958

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1.336652779028172

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1.5301423582358928

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1.0200520842302725

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1.001372682709934

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1.3381616652730208

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 7391656.438194444

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 12703285.14573213

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 5741834.379861111

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 3529170.002083333

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 827272.0604166667

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 624646.6756944444

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 4531770.741666666

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 9322499.240277778

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 3899728.3064628216

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 4639147.903472222

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 6035594.293055556

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1021071.0486111111

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 587583.4840277778

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 4458108.131944444

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 783447.5861111111

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 782133.7952810548

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1050136.6743055556

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 717256.9798611111

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 675235.6784722222

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 670297.4166666666

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1018584.8902777778

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 4428374.913194444

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1226022.0986796387

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1372475.2666666666

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 2304347.582638889

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 619253.6055555556

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 608696.1034722222

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 2274807.824305556

  **InstanceId:** i-0df4b0b5455778a5c

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-12-18 23:21:02+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.82

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2:fleet-id

    **Value:** fleet-0c169e17-eeaf-e4ad-06ba-29881f9a6eb7

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** Blueprint

    **Value:** prodinfraeks

  **EBSVolumes:** 
**VolumeId:** vol-09f83917df4bdc758

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 22.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 26.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 588.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 32.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 15.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 3434.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 2199.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 968919.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1034395.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 775250.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 982786.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 186838.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 127094.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 608831.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 938555.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 923232.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 816667.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 1298209.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 149969.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 127674.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 842572.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 532480.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 196608.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 69632.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 184320.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 290816.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 2764800.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 25137152.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 720896.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 823296.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 28413952.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 114688.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 28672.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 26382336.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 68761934848.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 75350899200.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 51541553664.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 77727443456.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 5935560192.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 1031186432.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 30868758016.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 51689397760.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 39755578880.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 48488301568.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 78608782336.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 2827575808.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 1041314816.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 48383097856.0

    **VolumeId:** vol-0e73b6a9bc28ce801

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 85438.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 61489.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 55231.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 45757.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 118367.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 71860.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 54722.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 64064.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 32825.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 73102.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 39265.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 26602.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 23407.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 15751.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 64515.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 43741.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 24113.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 30317.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 25652.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 25336.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1209666560.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 866844672.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 806718464.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 634820608.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 1686400000.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1017676800.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 764705792.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 897658880.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 481853440.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 1015559168.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1283379200.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 758784000.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 674983936.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 168931328.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 2861334528.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1624817664.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 773398528.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 1150312448.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 1472245760.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 271319040.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 1.6363713290184836

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1.4375332584382123

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1.3969756967442146

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1.3776216845580935

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1.1510243078414362

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1.0950428224712325

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1.4580231319891328

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1.7520405715933203

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1.3642569551505157

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1.4403554100637004

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1.4209548178266453

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1.1087233841428523

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1.1233668848714575

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1.4006816766063064

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 8604079.738194445

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 7862065.651388889

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 6639900.675

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 9862012.95763889

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1064609.9493055556

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 626261.7326388889

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 2894007.23125

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 7186704.475

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 4340592.539958305

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 4324817.526388889

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 6486438.429166666

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 702823.1875

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 593205.0993055556

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 4797476.361805555

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 763305.2847222222

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 2086285.3020833333

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 864148.5743055556

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 759459.1715277778

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 712941.60625

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 674825.7125

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 881039.09375

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 2608616.029861111

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1726820.0938151495

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1154247.61875

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1018494.9361111111

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 671416.7541666667

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 665028.4666666667

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1491819.3368055555

  **InstanceId:** i-0855dd4bd2b8d8b06

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2025-02-04 20:19:44+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.90.53

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-01cc91ab06316eb72

    **GroupName:** prodtabeks-node-20230815201205877700000004

  **Tags:** 
**Key:** Name

    **Value:** managed-prodtabeks

    **Key:** aws:ec2launchtemplate:version

    **Value:** 5

    **Key:** Blueprint

    **Value:** prodtabeks

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0a30753df7e3648b4

    **Key:** eks:cluster-name

    **Value:** prodtabeks

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-123e80ae-7baf-4eb4-ac3a-0fa22cf11970

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodtabeks-20231207205602416800000001-1ac62308-747d-a404-eed6-604b8a3778e2

    **Key:** eks:nodegroup-name

    **Value:** managed-prodtabeks-20231207205602416800000001

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/prodtabeks

    **Value:** owned

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:eks:cluster-name

    **Value:** prodtabeks

    **Key:** kubernetes.io/cluster/prodtabeks

    **Value:** owned

  **EBSVolumes:** 
**VolumeId:** vol-071a40f798d53fbb9

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 13214.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 34.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 2568.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 44.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 28.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 894.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 159342.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 347812.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 351381.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 353109.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 350771.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 353745.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 353203.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 503662592.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 1851392.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 507904.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 32497664.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 1503232.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 606208.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 8429568.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 8489097728.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 4449558528.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 4432335360.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 4587788800.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 4482536448.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 4533626368.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 4521496064.0

    **VolumeId:** vol-08bab8d2e2667cbff

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 400

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 311.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 56.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 68.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 27.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 11.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 16.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 85.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 19699.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 6211.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 49.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 48.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 77.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 32.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 69.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 140170.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 145540.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 154376.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 150206.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 139793.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 150512.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 143977.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 149201.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 153046.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 149219.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 140461.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 159752.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 139264.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 157785.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 6873088.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 229376.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 278528.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 110592.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 45056.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 65536.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 348160.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 2664612864.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 796688384.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 299008.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 204800.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 393216.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 163840.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 299008.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 23546724352.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 24861253632.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 27171602432.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 26293448704.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 23647756288.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 26317885440.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 24535891968.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 26270191616.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 26573766656.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 25725931520.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 23576580096.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 28606582784.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 23333720064.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 27608694784.0

    **VolumeId:** vol-0dde3637d9914844c

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 100

    **Throughput:** None

    **SizeGiB:** 20

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 7770.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 1273.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 9.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 5400.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 125957.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 1327.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 8390.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 6177.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 119658.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 127400.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 153090.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 127460.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 139279.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 101240.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 138650.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 217047.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 543154.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 432197.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 848986.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 813355.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 326212.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 687009.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 31825920.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 5214208.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 36864.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 22118400.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 542356480.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 5484544.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 34373632.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 25305088.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 30138081280.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 31939264512.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 38388961280.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 32035147776.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 35030618112.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 25628037120.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 34700201984.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 49726353408.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 137256071168.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 108281470976.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 209582043136.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 202416041984.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 81542569984.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 173071806464.0

    **VolumeId:** vol-04e3159cc31ae219a

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 150

    **Throughput:** None

    **SizeGiB:** 50

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 22.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 36.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 8.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 3679.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 19.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 5.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 3227380.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 3239789.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 3248560.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 3264501.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 3240754.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 3237367.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 3261605.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 3069202.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 3242524.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 3224143.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 3402554.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 3456885.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 3241369.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 3240867.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 24576.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 135168.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 8192.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 147456.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 57344.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 261403648.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 81920.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 4096.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 20480.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 68460711936.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 69255643136.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 69904592896.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 72865411072.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 68872380416.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 68293591040.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 72810717184.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 69761081344.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 74850443264.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 70407446528.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 106121277440.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 120637751296.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 71388655616.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 72166907904.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 7.654529052609757

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 7.495825513222759

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 7.14395282815788

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 7.651326289785735

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 7.581753783344286

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 7.164295174924775

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 7.3836223415717175

    **NetworkIn:** 
**Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 122308733.569161

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 112255441.38611111

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 101261347.27777778

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 136543612.54476058

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 143914847.9826389

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 99814932.56875

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 110106433.39027777

    **NetworkOut:** 
**Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 35998655.93424036

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 41218046.17986111

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 34935390.99513889

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 67592360.25329632

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 76475211.76458333

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 33745948.333333336

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 42717233.246527776

  **InstanceId:** i-020103789a30fb9f5

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2025-01-18 00:13:49+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.56

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-18afa9ae-2194-eb14-8e38-ac0272feff9a

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** Blueprint

    **Value:** prodinfraeks

  **EBSVolumes:** 
**VolumeId:** vol-0cb4332f1cc41f3cd

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 59.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 4.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 6.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 5.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 381.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 241.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 3343.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 5375.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1007264.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 902813.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 940132.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 494683.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 123300.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 121715.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 957107.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1102729.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 1480950.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 927236.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 1409613.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 174833.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 125899.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 961822.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 471040.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 6062080.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 143360.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 389120.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 73728.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 204800.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 528384.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 9805824.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 3837952.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 73728.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 82997248.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 100102144.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 68902686720.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 68900777472.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 68718142464.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 28708774400.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 1062149632.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 1047370240.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 59026938880.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 65456008704.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 52576657920.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 38851259392.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 40990557696.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 5225451520.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 1118795264.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 40783517184.0

    **VolumeId:** vol-05b8355354be25dc8

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 4010.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 37336.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 6312.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 6561.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 6568.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 4033.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 4085.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 11454.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 940.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 26189.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 5169.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 5531.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 5596.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 900.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 901.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 11286.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 21120000.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 675760128.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 86107136.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 101184512.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 101315584.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 21165056.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 21357568.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 136173568.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 5615616.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 857632768.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 186396672.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 205127680.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 207241216.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 5177344.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 5165056.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 738893824.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 1.6015660710506274

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1.435909945366584

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1.5414526281279526

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1.2822650495299455

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1.153729158434547

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1.1395150498459268

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1.5403429214009088

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1.66805917758805

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1.5767382402916383

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1.4246909719912049

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1.5040059983019483

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1.0985949163982993

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1.1399803083738995

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1.2850242432113659

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 8843536.175694445

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 9538974.347222222

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 10289727.179291174

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 3129021.648611111

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1325333.03125

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1264948.7694444444

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 5223259.375694444

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 9633899.049305556

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 5636668.383333334

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 4705350.974305555

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 5025041.046527778

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1565351.351388889

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1190953.8422515637

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 4567232.359027778

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 2006713.1916666667

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1705492.3805555555

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1605219.5156358583

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1617559.0284722222

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1460557.0333333334

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1417163.3972222223

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1690874.0881944445

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 2287300.8875

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 2683219.7055555554

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 2466333.7236111113

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 2422895.9583333335

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1270975.7083333333

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1363766.3884642113

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1740309.4631944445

  **InstanceId:** i-05d537b523c4637cd

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2024-12-13 19:48:25+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.236

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-10b6a8a4-d90d-e436-2c90-0d8a51cd6baf

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

    **Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

  **EBSVolumes:** 
**VolumeId:** vol-0167530aa11ea250a

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 235.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 1057.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 2.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 3.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 1542.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1698.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 345.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 2917.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 3978.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 2422.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1103871.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 639546.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 911563.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 759788.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 169346.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 132708.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 1162102.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 964687.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 1443694.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 1790891.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 1429045.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 151433.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 132154.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 1166042.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 7311360.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 9740288.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 151552.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 249856.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 9809920.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 10379264.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 17825792.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 43667456.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 85975040.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 131072.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 41164800.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 81607094784.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 41989264384.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 60840336384.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 51866166272.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 4420773376.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 1122744832.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 71709657088.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 48049684480.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 50431593472.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 66190100480.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 47272880128.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 2768599040.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 1109691392.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 49048295424.0

    **VolumeId:** vol-016a7c984c2c68829

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 608.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 613.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1566.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 853.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 1697.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 266.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 263.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 31671.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 401.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 807.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 6677504.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 6673408.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 15616000.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 7779328.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 15513600.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1744896.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 1744896.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 3474755584.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 2445312.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 4669440.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 1.5435733197449801

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1.3200284066819086

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1.5025509111225344

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1.3123583246042545

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1.0869236076378956

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1.1304884362375054

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1.575617692589958

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1.673424860056804

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1.4632454553766345

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1.5425602683674267

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1.3513396761454215

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1.1473645813107785

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1.156733779838675

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1.3755597820613743

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 10275184.588194445

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 5561034.459403193

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 7778375.364583333

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 4812881.7125

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 828027.0972897846

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 634152.6770833334

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 7880662.565972222

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 7016838.140277778

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 5322316.699305556

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 6220509.079861111

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 4495635.479861111

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 706775.5343988881

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 600572.776388889

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 4349973.754166666

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 1107103.675

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1050005.1616932685

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 759823.6277777777

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 765352.6083333333

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 683285.7546907575

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 714214.25625

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1025738.7111111111

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1713534.58125

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 2123209.5229166667

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 2679769.2555555557

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1690889.990277778

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 709034.0681028492

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 711845.6020833333

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 2027307.5868055555

  **InstanceId:** i-083b66d68202717e4

  **InstanceType:** m7a.2xlarge

  **State:** running

  **LaunchTime:** 2025-01-21 16:10:07+00:00

  **Pillars:** 
Reliability

    PerformanceEfficiency

    CostOptimization

  **IsOldGeneration:** False

  **PrivateIpAddress:** 10.27.70.167

  **PublicIpAddress:** None

  **KeyName:** None

  **SecurityGroups:** 
**GroupId:** sg-0cec60ae4f58dd68d

    **GroupName:** prodinfraeks-node-20230815201205499900000004

  **Tags:** 
**Key:** aws:ec2launchtemplate:id

    **Value:** lt-0d73139828428362a

    **Key:** k8s.io/cluster-autoscaler/prodinfraeks

    **Value:** owned

    **Key:** eks:cluster-name

    **Value:** prodinfraeks

    **Key:** eks:nodegroup-name

    **Value:** managed-prodinfraeks-20240130164732943200000001

    **Key:** aws:autoscaling:groupName

    **Value:** eks-managed-prodinfraeks-20240130164732943200000001-68c6ada2-684e-7cf6-4f6e-b1a066cb0dce

    **Key:** aws:eks:cluster-name

    **Value:** prodinfraeks

    **Key:** aws:ec2:fleet-id

    **Value:** fleet-a61c1cbd-4e0d-cc2f-06b0-8188f89675cd

    **Key:** kubernetes.io/cluster/prodinfraeks

    **Value:** owned

    **Key:** Blueprint

    **Value:** prodinfraeks

    **Key:** GithubRepo

    **Value:** https://git.tabbank.com/Operations/aws-terraform

    **Key:** k8s.io/cluster-autoscaler/enabled

    **Value:** true

    **Key:** Name

    **Value:** managed-prodinfraeks

    **Key:** aws:ec2launchtemplate:version

    **Value:** 4

  **EBSVolumes:** 
**VolumeId:** vol-026765301ff0c0955

    **Encrypted:** True

    **VolumeType:** gp2

    **Iops:** 225

    **Throughput:** None

    **SizeGiB:** 75

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 462.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 2162.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 1.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 1742.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1210810.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 847117.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 466177.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 604675.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 145600.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 118240.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 444567.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 715386.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 287430.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 182498.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 346790.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 120499.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 120474.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 568457.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 20811776.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 28250112.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 0.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 24576.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 19222528.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 92892066816.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 61429212160.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 28632805888.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 39564716544.0

        **Timestamp:** 2025-02-01T03:42:00+00:00

        **Sum:** 4190449152.0

        **Timestamp:** 2025-02-02T03:42:00+00:00

        **Sum:** 959973376.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 23892738560.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 49024052736.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 11463410176.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 6016545792.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 17074918912.0

        **Timestamp:** 2025-02-08T03:42:00+00:00

        **Sum:** 938515456.0

        **Timestamp:** 2025-02-09T03:42:00+00:00

        **Sum:** 943779840.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 30220726272.0

    **VolumeId:** vol-0e4c6cd1eb4b30200

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 152352.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 66616.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 74008.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 88977.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 51649.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 45035.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 30414.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 29374.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 15385.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 56029.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 56536.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 28583.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 30632.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 39307.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 20572.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 24973.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 13960.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 10045.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 10264.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 34573.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 2193155072.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 995742720.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 1062205440.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 1284157440.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 742689792.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 658114560.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 436408320.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 417189888.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 229197824.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 799800320.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1045667840.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 733601792.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 847646720.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 1240649728.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 665653248.0

        **Timestamp:** 2025-02-04T03:42:00+00:00

        **Sum:** 1082822656.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 563552256.0

        **Timestamp:** 2025-02-06T03:42:00+00:00

        **Sum:** 110514176.0

        **Timestamp:** 2025-02-07T03:42:00+00:00

        **Sum:** 581812224.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 1651273728.0

    **VolumeId:** vol-0decf3f4e52823f2e

    **Encrypted:** True

    **VolumeType:** gp3

    **Iops:** 3000

    **Throughput:** 125

    **SizeGiB:** 100

    **Utilization:** 
**VolumeReadOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 6578.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 6569.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 6569.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 14880.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 13175.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 12414.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 6645.0

      **VolumeWriteOps:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 1495.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 1492.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 1508.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 3791.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 2862.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 102553.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 1536.0

      **VolumeReadBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 34812928.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 34780160.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 34780160.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 190990336.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 69842944.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 114549760.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 35251200.0

      **VolumeWriteBytes:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

        **Sum:** 6934528.0

        **Timestamp:** 2025-01-29T03:42:00+00:00

        **Sum:** 8429568.0

        **Timestamp:** 2025-01-30T03:42:00+00:00

        **Sum:** 8491008.0

        **Timestamp:** 2025-01-31T03:42:00+00:00

        **Sum:** 23449600.0

        **Timestamp:** 2025-02-03T03:42:00+00:00

        **Sum:** 15175680.0

        **Timestamp:** 2025-02-05T03:42:00+00:00

        **Sum:** 1178120192.0

        **Timestamp:** 2025-02-10T03:42:00+00:00

        **Sum:** 8912896.0

  **Utilization:** 
**CPU:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 1.5539560740498795

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 1.4446692659447335

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 1.2622595783519066

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1.379876613802809

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 1.0736645749407547

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 1.07112745373079

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 1.2837379843901127

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1.2908497159732895

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1.2648916198896456

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 1.0876247979545322

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1.2290669408205537

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 1.0700047504478434

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 1.0681955226409943

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 1.2384830609425472

    **NetworkIn:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 6624338.392361111

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 4657244.596527778

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 2669715.146527778

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 3534799.6611111113

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 838748.3729166667

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 639687.1479166667

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 2467783.0520833335

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 6062937.869444445

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 1444646.8277777778

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 919035.1354166666

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 1957697.0201388889

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 630114.3815149409

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 606084.5472222222

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 2559655.701388889

    **NetworkOut:** 
**Timestamp:** 2025-01-28T03:42:00+00:00

      **Average:** 802579.6048611111

      **Timestamp:** 2025-01-29T03:42:00+00:00

      **Average:** 747834.9361111111

      **Timestamp:** 2025-01-30T03:42:00+00:00

      **Average:** 777370.2680555555

      **Timestamp:** 2025-01-31T03:42:00+00:00

      **Average:** 1263684.7256944445

      **Timestamp:** 2025-02-01T03:42:00+00:00

      **Average:** 680357.9444444445

      **Timestamp:** 2025-02-02T03:42:00+00:00

      **Average:** 682489.6569444444

      **Timestamp:** 2025-02-03T03:42:00+00:00

      **Average:** 764814.9472222222

      **Timestamp:** 2025-02-04T03:42:00+00:00

      **Average:** 1093358.620138889

      **Timestamp:** 2025-02-05T03:42:00+00:00

      **Average:** 702700.1451388889

      **Timestamp:** 2025-02-06T03:42:00+00:00

      **Average:** 687436.025

      **Timestamp:** 2025-02-07T03:42:00+00:00

      **Average:** 730538.3159722222

      **Timestamp:** 2025-02-08T03:42:00+00:00

      **Average:** 677931.2592077832

      **Timestamp:** 2025-02-09T03:42:00+00:00

      **Average:** 676649.1409722222

      **Timestamp:** 2025-02-10T03:42:00+00:00

      **Average:** 728027.0493055555

## Lambda

**us-east-2:** 


**us-west-2:** 


## ECS

**us-east-2:** 


**us-west-2:** 


## S3

**Name:** 076812642930-s3-access-logging

**CreationDate:** 2023-03-21 20:19:16+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** cf-templates-9jk5b97iemao-us-east-1

**CreationDate:** 2023-03-21 20:17:11+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** cf-templates-9jk5b97iemao-us-west-2

**CreationDate:** 2024-11-12 13:32:59+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** dataprodaws-tf-backend-s3

**CreationDate:** 2024-11-12 17:37:29+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** True

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** default-repo-tabbank-com

**CreationDate:** 2024-11-12 18:00:27+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** dev-velelro20230604140301715500000001

**CreationDate:** 2024-10-16 04:27:56+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** loki-admin-prodinfraeks-076812642930-us-west-2

**CreationDate:** 2024-11-13 09:12:52+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** loki-chunks-prodinfraeks-076812642930-us-west-2

**CreationDate:** 2024-11-13 09:12:55+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** loki-chunks-prodtabeks-076812642930-us-west-2

**CreationDate:** 2024-11-13 09:12:55+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** Could not retrieve - possibly not set or no permission.

**Name:** loki-ruler-prodinfraeks-076812642930-us-west-2

**CreationDate:** 2024-11-13 09:13:05+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** new-loki-admin-prodtabeks-076812642930-us-west-2

**CreationDate:** 2024-11-13 11:45:53+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** new-loki-chunks-prodtabeks-076812642930-us-west-2

**CreationDate:** 2024-11-06 21:22:47+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** new-loki-ruler-prodtabeks-076812642930-us-west-2

**CreationDate:** 2024-11-13 11:45:53+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** sftp-prod-076812642930-us-west-2

**CreationDate:** 2024-11-10 08:18:03+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** AES256

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** tabprodaws-tf-backend-s3

**CreationDate:** 2024-11-10 10:34:38+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** aws:kms

      **KMSMasterKeyID:** ffa3d45a-d08f-44d0-b224-cfa10c940085

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

**Name:** tabprodaws-tf-backend-s3-back

**CreationDate:** 2024-11-13 22:05:03+00:00

**Pillars:** 
Security

  Reliability

  CostOptimization

**Encryption:** 
**Rules:** 
**ApplyServerSideEncryptionByDefault:** 
**SSEAlgorithm:** aws:kms

      **KMSMasterKeyID:** arn:aws:kms:us-west-2:076812642930:key/ffa3d45a-d08f-44d0-b224-cfa10c940085

    **BucketKeyEnabled:** False

**PublicAccessBlock:** 
**BlockPublicAcls:** True

  **IgnorePublicAcls:** True

  **BlockPublicPolicy:** True

  **RestrictPublicBuckets:** True

## RDS

**us-east-2:** 


**us-west-2:** 
**DBInstanceIdentifier:** argo-workflows-prod

  **Engine:** postgres

  **DBInstanceStatus:** available

  **DBInstanceIdentifier:** srm-prod

  **Engine:** mariadb

  **DBInstanceStatus:** available

## VPC

**us-east-2:** 
**VpcId:** vpc-092df0050b9058744

  **CidrBlock:** 10.0.0.0/16

  **IsDefault:** False

**us-west-2:** 
**VpcId:** vpc-0afc6fba568a2876a

  **CidrBlock:** 10.27.0.0/16

  **IsDefault:** False

## IAM

**Users:** 
**UserName:** data-datapipeline-prod

  **CreateDate:** 2023-11-27 19:21:32+00:00

  **UserName:** data-prod

  **CreateDate:** 2024-01-16 20:26:52+00:00

  **UserName:** devops+nexus@tabbank.com

  **CreateDate:** 2023-06-20 17:16:11+00:00

  **UserName:** githubactionseks

  **CreateDate:** 2023-08-15 16:44:54+00:00

  **UserName:** hd.jensen@tabbank.com

  **CreateDate:** 2023-11-29 17:33:20+00:00

  **UserName:** lending-credit-prod

  **CreateDate:** 2024-01-31 20:23:19+00:00

  **UserName:** loki-platform-monitoring-prodinfraeks

  **CreateDate:** 2023-09-12 20:36:44+00:00

  **UserName:** loki-platform-monitoring-prodtabeks

  **CreateDate:** 2023-12-08 17:20:52+00:00

  **UserName:** mike.ferlin@tabbank.com

  **CreateDate:** 2023-03-23 16:34:54+00:00

  **UserName:** starp-prod

  **CreateDate:** 2023-12-14 17:01:40+00:00

  **UserName:** stewart.foreman@tabbank.com

  **CreateDate:** 2024-09-12 14:13:42+00:00

  **UserName:** tezis-prod

  **CreateDate:** 2024-02-29 16:14:03+00:00

  **UserName:** zack.ward@tabbank.com

  **CreateDate:** 2023-03-23 16:32:48+00:00

  **UserName:** zuntafi-sftp

  **CreateDate:** 2023-10-26 18:54:00+00:00

**Roles:** 
**RoleName:** admin-team-20230802214645900100000001

  **CreateDate:** 2023-08-02 21:46:46+00:00

  **RoleName:** admin-team-20230802224004886100000003

  **CreateDate:** 2023-08-02 22:40:05+00:00

  **RoleName:** admin-team-20230815201205466300000003

  **CreateDate:** 2023-08-15 20:12:05+00:00

  **RoleName:** admin-team-20230815201205607800000002

  **CreateDate:** 2023-08-15 20:12:05+00:00

  **RoleName:** AmazonAppStreamPCAAccess

  **CreateDate:** 2023-03-21 20:34:56+00:00

  **RoleName:** AmazonAppStreamServiceAccess

  **CreateDate:** 2023-03-21 20:34:56+00:00

  **RoleName:** AmazonEKSTFEBSCSIRole-prodinfraeks

  **CreateDate:** 2023-08-15 21:17:40+00:00

  **RoleName:** AmazonEKSTFEBSCSIRole-prodtabeks

  **CreateDate:** 2023-08-15 21:17:40+00:00

  **RoleName:** ApplicationAutoScalingForAmazonAppStreamAccess

  **CreateDate:** 2023-03-21 20:34:56+00:00

  **RoleName:** Assumezuntafi303

  **CreateDate:** 2023-10-27 17:03:18+00:00

  **RoleName:** aws-dlm-lifecycle-tabprodaws-dlm-backup-role

  **CreateDate:** 2023-07-14 22:33:39+00:00

  **RoleName:** AWSReservedSSO_AWS_Admin_2e11b98beffe2b02

  **CreateDate:** 2023-11-30 21:59:23+00:00

  **RoleName:** AWSReservedSSO_AWS_Admin_ViewOnly_b3f854fe3cf2e3ed

  **CreateDate:** 2023-03-27 18:39:54+00:00

  **RoleName:** AWSReservedSSO_AWS_Admin_With_DNS_ca345c95dea6d40f

  **CreateDate:** 2023-11-28 18:55:05+00:00

  **RoleName:** AWSReservedSSO_AWS_Audit_c5abf814ae307da4

  **CreateDate:** 2023-03-27 18:40:09+00:00

  **RoleName:** AWSReservedSSO_AWS_Network_Admin_05340d37635bb19d

  **CreateDate:** 2023-03-27 18:40:24+00:00

  **RoleName:** AWSReservedSSO_AWS_PowerUser_8de7cb4baca5bdda

  **CreateDate:** 2023-03-27 18:40:39+00:00

  **RoleName:** AWSReservedSSO_AWS_Security_Admin_ed87501b2d8e7770

  **CreateDate:** 2023-03-27 18:40:53+00:00

  **RoleName:** AWSServiceRoleForAmazonEKS

  **CreateDate:** 2023-06-04 14:03:21+00:00

  **RoleName:** AWSServiceRoleForAmazonEKSNodegroup

  **CreateDate:** 2023-06-04 14:10:51+00:00

  **RoleName:** AWSServiceRoleForAmazonGuardDuty

  **CreateDate:** 2023-03-08 16:50:36+00:00

  **RoleName:** AWSServiceRoleForAmazonGuardDutyMalwareProtection

  **CreateDate:** 2023-03-08 16:50:36+00:00

  **RoleName:** AWSServiceRoleForApplicationAutoScaling_DynamoDBTable

  **CreateDate:** 2023-08-25 22:24:52+00:00

  **RoleName:** AWSServiceRoleForAutoScaling

  **CreateDate:** 2023-06-04 14:11:12+00:00

  **RoleName:** AWSServiceRoleForCloudFormationStackSetsOrgMember

  **CreateDate:** 2023-11-06 18:55:48+00:00

  **RoleName:** AWSServiceRoleForCloudTrail

  **CreateDate:** 2023-05-17 05:41:35+00:00

  **RoleName:** AWSServiceRoleForCloudWatchEvents

  **CreateDate:** 2023-03-24 12:36:29+00:00

  **RoleName:** AWSServiceRoleForComputeOptimizer

  **CreateDate:** 2025-02-10 23:23:48+00:00

  **RoleName:** AWSServiceRoleForCostOptimizationHub

  **CreateDate:** 2025-02-10 23:23:11+00:00

  **RoleName:** AWSServiceRoleForElasticLoadBalancing

  **CreateDate:** 2023-08-22 19:54:34+00:00

  **RoleName:** AWSServiceRoleForFMS

  **CreateDate:** 2023-02-27 18:25:48+00:00

  **RoleName:** AWSServiceRoleForGlobalAccelerator

  **CreateDate:** 2024-01-30 16:03:45+00:00

  **RoleName:** AWSServiceRoleForInternetMonitor

  **CreateDate:** 2024-05-07 20:19:08+00:00

  **RoleName:** AWSServiceRoleForOrganizations

  **CreateDate:** 2023-03-23 16:11:35+00:00

  **RoleName:** AWSServiceRoleForRDS

  **CreateDate:** 2024-01-29 23:31:40+00:00

  **RoleName:** AWSServiceRoleForSSO

  **CreateDate:** 2023-03-27 14:21:47+00:00

  **RoleName:** AWSServiceRoleForSupport

  **CreateDate:** 2023-02-27 18:25:14+00:00

  **RoleName:** AWSServiceRoleForTrustedAdvisor

  **CreateDate:** 2023-02-27 18:25:14+00:00

  **RoleName:** AWSServiceRoleForVPCTransitGateway

  **CreateDate:** 2023-03-24 12:53:57+00:00

  **RoleName:** Axonius-ReadOnly

  **CreateDate:** 2023-11-06 18:59:21+00:00

  **RoleName:** cc-iam-stack-IamRole-1KJXLW7Y789W

  **CreateDate:** 2023-03-17 19:36:11+00:00

  **RoleName:** cloud303-automation

  **CreateDate:** 2023-02-27 18:30:22+00:00

  **RoleName:** cloud303-billing

  **CreateDate:** 2023-02-27 18:30:22+00:00

  **RoleName:** cloud303-global

  **CreateDate:** 2023-03-07 20:24:32+00:00

  **RoleName:** cloud303-organization

  **CreateDate:** 2023-02-27 18:25:14+00:00

  **RoleName:** cloud303-read-only

  **CreateDate:** 2023-02-27 18:30:22+00:00

  **RoleName:** cloud303-support

  **CreateDate:** 2023-02-27 18:30:22+00:00

  **RoleName:** flowlogs-tab-prod-vpc01

  **CreateDate:** 2023-07-28 22:51:02+00:00

  **RoleName:** iam_for_transfer_20231116210042802500000001

  **CreateDate:** 2023-11-16 21:00:43+00:00

  **RoleName:** managed-prodinfraeks-eks-node-group-20230802224004872400000001

  **CreateDate:** 2023-08-02 22:40:05+00:00

  **RoleName:** managed-prodinfraeks-eks-node-group-20230815201205465700000001

  **CreateDate:** 2023-08-15 20:12:05+00:00

  **RoleName:** managed-prodtabeks-eks-node-group-20230802214645901400000005

  **CreateDate:** 2023-08-02 21:46:46+00:00

  **RoleName:** managed-prodtabeks-eks-node-group-20230815201205607800000003

  **CreateDate:** 2023-08-15 20:12:05+00:00

  **RoleName:** prod-admin-access

  **CreateDate:** 2023-06-04 14:10:49+00:00

  **RoleName:** prod-agocd

  **CreateDate:** 2023-09-18 19:26:48+00:00

  **RoleName:** prod-aws-load-balancer-controller-sa-irsa

  **CreateDate:** 2023-06-04 14:10:58+00:00

  **RoleName:** prod-cert-manager-irsa

  **CreateDate:** 2023-06-04 14:10:58+00:00

  **RoleName:** prod-cluster-role

  **CreateDate:** 2023-06-04 14:03:00+00:00

  **RoleName:** prod-ebs-csi-controller-sa-irsa

  **CreateDate:** 2023-06-04 14:10:58+00:00

  **RoleName:** PROD-PING-role

  **CreateDate:** 2023-05-25 18:38:27+00:00

  **RoleName:** prod-prod

  **CreateDate:** 2023-06-04 14:10:49+00:00

  **RoleName:** prod-team-riker-access

  **CreateDate:** 2023-06-04 14:10:48+00:00

  **RoleName:** prod-team-riker-sa-role

  **CreateDate:** 2023-06-04 14:10:48+00:00

  **RoleName:** prod-velero-irsa

  **CreateDate:** 2023-06-04 14:10:58+00:00

  **RoleName:** prodinfraeks-argocd-server-sa

  **CreateDate:** 2023-09-19 18:54:20+00:00

  **RoleName:** prodinfraeks-cluster-20230802224004885700000002

  **CreateDate:** 2023-08-02 22:40:05+00:00

  **RoleName:** prodinfraeks-cluster-20230815201205466200000002

  **CreateDate:** 2023-08-15 20:12:05+00:00

  **RoleName:** prodtabeks-argocd-server-sa

  **CreateDate:** 2023-10-03 17:55:51+00:00

  **RoleName:** prodtabeks-cluster-20230802214645900900000004

  **CreateDate:** 2023-08-02 21:46:46+00:00

  **RoleName:** prodtabeks-cluster-20230815201206269900000005

  **CreateDate:** 2023-08-15 20:12:06+00:00

  **RoleName:** rds-monitoring-postrgesrole-argo-workflows

  **CreateDate:** 2024-04-23 16:42:44+00:00

  **RoleName:** rds-monitoringmariadb-role

  **CreateDate:** 2024-02-12 16:53:13+00:00

  **RoleName:** stacksets-exec-7b0d43b4fe42531280349120796052f3

  **CreateDate:** 2023-11-06 18:55:55+00:00

  **RoleName:** team-blue-2023080221545232400000000e

  **CreateDate:** 2023-08-02 21:54:52+00:00

  **RoleName:** team-blue-2023080222510013120000000e

  **CreateDate:** 2023-08-02 22:51:00+00:00

  **RoleName:** team-red-2023080221545232730000000f

  **CreateDate:** 2023-08-02 21:54:52+00:00

  **RoleName:** team-red-2023080222510013460000000f

  **CreateDate:** 2023-08-02 22:51:00+00:00

**Policies:** 
**PolicyName:** prodinfraeks-argocd-server-sa

  **CreateDate:** 2023-09-19 18:54:20+00:00

  **PolicyName:** prodtabeks-cluster-ClusterEncryption2023081520122948500000000b

  **CreateDate:** 2023-08-15 20:12:29+00:00

  **PolicyName:** admin-team-2023080222505890670000000d

  **CreateDate:** 2023-08-02 22:50:59+00:00

  **PolicyName:** prodtabeks-cluster-ClusterEncryption2023080221470972380000000b

  **CreateDate:** 2023-08-02 21:47:09+00:00

  **PolicyName:** admin-team-2023080221545102490000000d

  **CreateDate:** 2023-08-02 21:54:51+00:00

  **PolicyName:** KMS_Key_For_Encryption_On_EBS-prodinfraeks

  **CreateDate:** 2023-08-15 20:16:46+00:00

  **PolicyName:** loki-access-permissions-prodinfraeks

  **CreateDate:** 2023-12-08 00:06:03+00:00

  **PolicyName:** admin-team-20230815205108735400000001

  **CreateDate:** 2023-08-15 20:51:09+00:00

  **PolicyName:** prod-lb-irsa

  **CreateDate:** 2023-06-04 14:10:57+00:00

  **PolicyName:** aws-dlm-lifecycle-tabprodaws-dlm-backup-role-policy

  **CreateDate:** 2023-07-14 22:33:39+00:00

  **PolicyName:** KMS_Key_For_Encryption_On_EBS-prodtabeks

  **CreateDate:** 2023-08-15 20:16:46+00:00

  **PolicyName:** prodinfraeks-cluster-ClusterEncryption2023080222403073950000000b

  **CreateDate:** 2023-08-02 22:40:30+00:00

  **PolicyName:** prodinfraeks-cluster-ClusterEncryption2023081520122948460000000b

  **CreateDate:** 2023-08-15 20:12:29+00:00

  **PolicyName:** prod-aws-ebs-csi-driver-irsa

  **CreateDate:** 2023-06-04 14:10:57+00:00

  **PolicyName:** CloudWatchInternetMonitor

  **CreateDate:** 2024-05-08 13:49:02+00:00

  **PolicyName:** prod-velero

  **CreateDate:** 2023-06-04 14:10:57+00:00

  **PolicyName:** prod-cert-manager-irsa

  **CreateDate:** 2023-06-04 14:10:57+00:00

  **PolicyName:** example-policy

  **CreateDate:** 2023-06-20 18:45:32+00:00

  **PolicyName:** TEMP_ALL_KMS

  **CreateDate:** 2023-08-15 20:19:52+00:00

  **PolicyName:** admin-team-20230815204835710700000001

  **CreateDate:** 2023-08-15 20:48:36+00:00

  **PolicyName:** prod-PlatformTeamEKSAccess

  **CreateDate:** 2023-06-04 14:10:48+00:00

  **PolicyName:** loki-access-permissions-prodtabeks

  **CreateDate:** 2023-12-08 00:05:58+00:00
