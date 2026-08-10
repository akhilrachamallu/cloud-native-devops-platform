# Cloud-Native DevOps Platform

An end-to-end cloud-native DevOps project demonstrating application development,
containerization, CI/CD, Infrastructure as Code, Kubernetes orchestration,
cloud deployment, security scanning, monitoring, and centralized logging.

## Project Status

🚧 Under Development

## Architecture

The platform will eventually implement:

Developer
→ GitHub
→ GitHub Actions
→ Testing
→ SonarQube
→ Trivy
→ Docker
→ AWS ECR
→ Kubernetes / AWS EKS
→ Monitoring

## Technology Stack

### Application
- React
- FastAPI
- PostgreSQL

### DevOps
- Git
- GitHub
- GitHub Actions
- Docker
- Kubernetes
- Helm
- Terraform

### AWS
- Amazon ECR
- Amazon EKS
- Amazon RDS
- Amazon VPC
- IAM
- CloudWatch

### Security
- SonarQube
- Trivy
- Kubernetes Secrets
- AWS Secrets Manager

### Monitoring
- Prometheus
- Grafana
- Loki

## Repository Structure

```text
cloud-native-devops-platform/
├── backend/
├── frontend/
├── database/
├── docker/
├── k8s/
├── helm/
├── terraform/
├── monitoring/
├── scripts/
├── docs/
└── .github/
    └── workflows/