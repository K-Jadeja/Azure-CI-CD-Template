# FastAPI Azure Deployment Template (ACI-CICD)

This repository serves as a template for deploying a FastAPI application to **Azure Container Instances** using **GitHub Actions**. The workflow automates building a Docker image, pushing it to **Azure Container Registry**, and deploying it to **Azure Container Instances** with environment variables securely passed through GitHub Secrets.

---

## Features
- **FastAPI application**: A simple FastAPI app with file upload, environment variable checks, and basic routing.
- **GitHub Actions Workflow**: Automates:
  1. Building a Docker image.
  2. Pushing it to Azure Container Registry.
  3. Deploying to Azure Container Instances.
- **Environment Variables**: Securely inject environment variables using GitHub Secrets.
- **Ease of Use**: Just clone the repository, configure the secrets, and push to the `main` branch.

---

## Repository Structure
- **`main.py`**: The FastAPI application.
  - File upload and retrieval endpoints.
  - `/checkenv` endpoint to verify environment variables.
- **`main.yml`**: GitHub Actions workflow to automate deployment.
- **`Dockerfile`**: A generic Dockerfile to containerize the application.

---

## Setup Instructions
## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/fastapi-azure-template.git
cd fastapi-azure-template
```

### 2. Configure GitHub Secrets
Add the following secrets in your repository's **Settings > Secrets and Variables > Actions**:
- **Azure Credentials**:  
  - `AZURE_CREDENTIALS`: Azure Service Principal credentials in JSON format.
    * `az login`
    * ```bash
      az ad sp create-for-rbac --name "<give-service-principle-a-name>" --role contributor \ 
                             --scopes /subscriptions/<subscriptionId>/resourceGroups/<resource-group-name> \
                             --sdk-auth
      ```
    * set up federated credentials for this service principle on azure portal. See [video](https://www.youtube.com/watch?v=fEdHtvBp7Dw&t=267s)
  - `AZURE_RESOURCE_GROUP`: Azure resource group name.
  - `ACR_LOGIN_SERVER`: Azure Container Registry login server.
  - `ACR_USERNAME`: Azure Container Registry username.
  - `ACR_PASSWORD`: Azure Container Registry password.
- **Application Secrets**: Add required application environment variables like:
  - `KEY1`, `KEY2`, `KEY3`, etc.
    ![image](https://github.com/user-attachments/assets/29b388ca-aaea-47fc-aad2-1b99a22ad2bf)

### 3. Push to Main Branch
Once configured, pushing to the `main` branch will trigger the GitHub Actions workflow to:
1. Build and push the Docker image to Azure Container Registry.
2. Deploy the container to Azure Container Instances.

---

## Application Endpoints
- `GET /`: Returns a greeting message.
- `POST /upload/`: Uploads an image and provides a viewable URL.
- `GET /view/{file_id}`: Retrieves an uploaded image.
- `GET /checkenv`: Lists all available environment variables.

---

## Customization
- Modify `main.py` to fit your application needs.
- Update `main.yml` to adjust resource limits (CPU/Memory) or deployment settings.

---

## License
This template is open-sourced under the MIT License. Feel free to modify and distribute.

Happy deploying! 🚀

