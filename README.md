# DevSecOps Pipeline Implementation

This repository demonstrates a comprehensive DevSecOps pipeline implementation using GitHub Actions, including security testing, container scanning, and Kubernetes deployment with policy enforcement.

## Project Structure

```
devsecops-pipeline/
├── .github/
│   └── workflows/
│       └── devsecops-pipeline.yml
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── requirements.txt
│   └── tests/
│       └── test_app.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── gatekeeper/
│       ├── constraint-template.yaml
│       └── constraint.yaml
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── Dockerfile
├── .pylintrc
├── .gitignore
└── README.md
```

## Prerequisites

### Required Accounts & Tools
- GitHub account (public repository)
- Google Cloud Platform account (for Artifact Registry)
- Kubernetes cluster (GKE, Minikube, or kind for local testing)
- Docker installed locally

### Technologies Used
- **CI/CD**: GitHub Actions
- **Application**: Python FastAPI web application
- **Container Registry**: Google Cloud Artifact Registry
- **Orchestration**: Kubernetes
- **Policy Engine**: Open Policy Agent (OPA) Gatekeeper
- **Security Tools**: Various integrated and open-source tools

## Setup Instructions

### 1. GitHub Repository Setup

1. Create a new public GitHub repository
2. Set up the following secrets in your repository settings:
   - `GCP_PROJECT_ID`: Your Google Cloud Project ID
   - `GCP_SA_KEY`: Google Cloud Service Account JSON key
   - `GKE_CLUSTER_NAME`: Your GKE cluster name
   - `GKE_CLUSTER_ZONE`: Your GKE cluster zone

### 2. Google Cloud Setup

1. Create a new GCP project or use an existing one
2. Enable required APIs:
   ```bash
   gcloud services enable artifactregistry.googleapis.com
   gcloud services enable container.googleapis.com
   ```

3. Create Artifact Registry:
   ```bash
   gcloud artifacts repositories create devsecops-repo \
     --repository-format=docker \
     --location=us-central1
   ```

4. Create GKE Cluster:
   ```bash
   gcloud container clusters create devsecops-cluster \
     --zone=us-central1-a \
     --num-nodes=3 \
     --enable-network-policy
   ```

5. Install OPA Gatekeeper:
   ```bash
   kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/release-3.14/deploy/gatekeeper.yaml
   ```

### 3. Service Account Setup

Create a service account with necessary permissions:
```bash
# Create service account
gcloud iam service-accounts create github-actions-sa

# Assign roles
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:github-actions-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:github-actions-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/container.developer"

# Create and download key
gcloud iam service-accounts keys create key.json \
  --iam-account=github-actions-sa@PROJECT_ID.iam.gserviceaccount.com
```

## Pipeline Features

The DevSecOps pipeline includes the following features:

1. **Code Quality**
   - Pylint for code quality checks
   - YAPF for code formatting
   - Unit testing with pytest

2. **Security Testing**
   - Bandit for Python security scanning
   - Safety for dependency vulnerability checking
   - CodeQL for advanced security analysis
   - GitLeaks for secret scanning
   - Trivy for container vulnerability scanning

3. **Container Management**
   - Docker image building
   - Container vulnerability scanning
   - Secure container registry storage

4. **Kubernetes Deployment**
   - Automated deployment to GKE
   - OPA Gatekeeper policy enforcement
   - Resource limits and security contexts

5. **Infrastructure Security**
   - Terraform configuration scanning
   - Infrastructure as Code security checks

## Testing the Pipeline

### Success Case Testing
1. Start with clean, secure code
2. Push to main branch
3. Verify all pipeline steps pass
4. Confirm successful deployment to Kubernetes

### Failure Case Testing

Test each failure scenario:
1. **Linting Failure**: Introduce code quality issues
2. **Secret Scan Failure**: Add fake API keys
3. **SAST Failure**: Add vulnerable code patterns
4. **Container Scan Failure**: Use vulnerable dependencies
5. **Registry Policy Failure**: Use unauthorized container registry
6. **IaC Security Failure**: Add insecure Terraform configurations

## Security Features

- GitHub security features enabled
- Dependabot alerts configured
- Security scan results uploaded to GitHub
- Container registry restrictions enforced
- Kubernetes security policies active

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
