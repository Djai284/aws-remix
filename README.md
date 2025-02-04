# AWS Remix

AWS Remix is a fun, powerful CLI tool designed for cloud consultants, DevOps engineers, and architects. It scans your AWS account, gathers detailed information about your cloud resources, and outputs a comprehensive, AI-friendly document that can be used for a variety of purposes—from feeding into LLMs for architecture insights to generating reports for improvements and best practices.

## Features

- **Comprehensive AWS Resource Mapping:** Retrieves detailed information from services like EC2, Lambda, S3, RDS, ECS, VPC, IAM, and more.
- **Multiple Output Formats:** Generate output in JSON, YAML, or Markdown—perfect for automated processing or human review.
- **AI-Optimized Summaries:** Organizes your account data into well-defined sections, making it easier for large language models (LLMs) to understand your architecture.
- **Modular & Extensible:** Easily add new services or custom output formats to fit your consulting needs.
- **Fun & Informative:** AWS Remix turns your AWS environment into a “remixed” view that helps you see the big picture.

## Use Cases

AWS Remix is an ideal tool for:
- **Cloud Consulting:** Quickly understand what’s happening in an AWS account. Generate comprehensive reports that highlight architecture strengths, weaknesses, and recommendations for improvements.
- **LLM-Enhanced Architecture Reviews:** Feed the output into LLMs (like GPT-4) to gain insights on potential updates, improvements, and best practices.
- **Application Architecture Analysis:** Determine the purpose of the architecture, how resources are interconnected, and what improvements can be made to optimize performance and cost.
- **Migration & New Feature Scoping:** Use the detailed resource map to plan migrations, implement new features, or re-architect parts of your AWS environment.
- **Best Practice Audits:** Quickly identify non-compliant configurations and areas for security and cost optimization.

## Prerequisites

- **Python 3.7+**
- **AWS Credentials:** Make sure your AWS credentials are configured (via environment variables, AWS CLI profiles, or IAM roles) with read-only permissions (e.g., `AWSReadOnlyAccess`).
- **AWS Permissions:** The tool uses AWS API calls to gather resource details—ensure your credentials have the necessary permissions.

## Installation

Clone the repository and install the package locally:

```bash
git clone https://github.com/yourusername/aws-remix.git
cd aws-remix
pip install .
```
Alternatively, if the package is available on PyPI:
```bash
pip install aws-remix
```

## Usage

Run AWS Remix from the command line with your preferred options:
```bash
aws-remix [OPTIONS]
```

### Options
- `--region`: Specify the AWS region to scan (default: us-east-1).
- `--output-format`: Choose the output format: json, yaml, or md (default: json).
- `--verbose`: Enable verbose logging for additional process details.
- `--help`: Display the help message.

### Example Commands
- Generate JSON Output in the Default Region:
```bash
aws-remix --output-format json
```
- Scan a Specific Region and Output YAML:
```bash
aws-remix --region us-west-2 --output-format yaml
```
- Enable Verbose Mode for Debugging:
```bash
aws-remix --verbose
```

## Expected Output
AWS Remix produces a detailed document summarizing your AWS account. Below are sample outputs for each format.

### JSON Output Example
```json
{
  "AccountOverview": {
    "AccountID": "123456789012",
    "AccountAlias": "cloud-consult-prod",
    "RegionsInUse": ["us-east-1", "us-west-2"],
    "ResourceCounts": {
      "EC2Instances": 12,
      "LambdaFunctions": 4,
      "S3Buckets": 3,
      "RDSInstances": 2,
      "ECSClusters": 1,
      "LoadBalancers": 2,
      "VPCs": 1
    }
  },
  "ComputeResources": {
    "EC2Instances": [
      {
        "InstanceID": "i-0123456789abcdef0",
        "InstanceType": "m5.large",
        "State": "running",
        "AvailabilityZone": "us-east-1a",
        "VPC": "vpc-1234abcd",
        "Subnet": "subnet-5678efgh",
        "SecurityGroups": ["sg-111aaa", "sg-222bbb"],
        "Tags": {
          "Name": "WebServer",
          "Environment": "Production"
        }
      }
    ],
    "LambdaFunctions": [
      {
        "FunctionName": "ThumbnailGenerator",
        "Runtime": "python3.8",
        "MemorySize": 256,
        "Timeout": 15,
        "Triggers": ["S3 (new video upload)"],
        "IAMRole": "arn:aws:iam::123456789012:role/LambdaExecutionRole",
        "Tags": {
          "Environment": "Production"
        }
      }
    ]
  },
  // ... additional sections for Storage, Networking, IAM, etc.
}
```

### YAML Output Example
```yaml
AccountOverview:
  AccountID: "123456789012"
  AccountAlias: cloud-consult-prod
  RegionsInUse:
    - us-east-1
    - us-west-2
  ResourceCounts:
    EC2Instances: 12
    LambdaFunctions: 4
    S3Buckets: 3
    RDSInstances: 2
    ECSClusters: 1
    LoadBalancers: 2
    VPCs: 1
ComputeResources:
  EC2Instances:
    - InstanceID: i-0123456789abcdef0
      InstanceType: m5.large
      State: running
      AvailabilityZone: us-east-1a
      VPC: vpc-1234abcd
      Subnet: subnet-5678efgh
      SecurityGroups:
        - sg-111aaa
        - sg-222bbb
      Tags:
        Name: WebServer
        Environment: Production
  LambdaFunctions:
    - FunctionName: ThumbnailGenerator
      Runtime: python3.8
      MemorySize: 256
      Timeout: 15
      Triggers:
        - "S3 (new video upload)"
      IAMRole: arn:aws:iam::123456789012:role/LambdaExecutionRole
      Tags:
        Environment: Production
# ... additional sections for Storage, Networking, IAM, etc.
```

### Markdown Output Example
```markdown
# AWS Account Overview

## Account Overview
- **Account ID:** 123456789012
- **Account Alias:** cloud-consult-prod
- **Regions In Use:** us-east-1, us-west-2
- **Resource Counts:**
  - EC2 Instances: 12
  - Lambda Functions: 4
  - S3 Buckets: 3
  - RDS Instances: 2
  - ECS Clusters: 1
  - Load Balancers: 2
  - VPCs: 1

## Compute Resources

### EC2 Instances
- **InstanceID:** i-0123456789abcdef0  
  **Type:** m5.large  
  **State:** running  
  **Availability Zone:** us-east-1a  
  **VPC:** vpc-1234abcd  
  **Subnet:** subnet-5678efgh  
  **Security Groups:** sg-111aaa, sg-222bbb  
  **Tags:**  
  - Name: WebServer  
  - Environment: Production

### Lambda Functions
- **Function Name:** ThumbnailGenerator  
  **Runtime:** python3.8  
  **Memory:** 256 MB  
  **Timeout:** 15 seconds  
  **Triggers:** S3 (new video upload)  
  **IAM Role:** arn:aws:iam::123456789012:role/LambdaExecutionRole  
  **Tags:**  
  - Environment: Production

<!-- Additional sections for Storage, Networking, IAM, etc. -->
```

## Contributing
We welcome contributions from the community! Whether it's new features, bug fixes, or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Support
For questions, feature requests, or support, please open an issue on the GitHub repository or contact dhananjai284@gmail.com.

---

AWS Remix transforms your AWS account into an easily understandable, structured report—making it a valuable asset for cloud consulting, architecture reviews, migrations, and continuous improvement initiatives. Enjoy remixing your cloud!
