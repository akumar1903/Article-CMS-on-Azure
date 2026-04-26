# Write-up Template

# Deployment Analysis: VM vs Azure App Service

## Analyze, Choose, and Justify the Appropriate Resource Option

### Option 1: Azure Virtual Machine

A Virtual Machine provides full infrastructure control. It would allow manual installation of Python, Flask, Gunicorn, Nginx, ODBC drivers, custom networking rules, and monitoring agents.

**Cost:** A VM can become more expensive over time because it runs continuously and requires separate management for storage, monitoring, backup, and security. Even if traffic is low, compute costs continue unless the VM is stopped.

**Scalability:** Scaling a VM requires additional configuration, such as creating more VMs, configuring a load balancer, and managing deployment consistency across instances.

**Availability:** High availability requires extra setup, such as availability zones, VM scale sets, backups, and recovery planning.

**Workflow:** Deployment and maintenance are more manual. The team must manage OS patching, runtime updates, web server configuration, SSL certificates, and application restarts.

### Option 2: Azure App Service

Azure App Service is a managed Platform-as-a-Service option designed for web applications. It supports Python Flask apps and integrates easily with Azure SQL Database, Azure Blob Storage, Microsoft Entra ID authentication, and logging.

**Cost:** App Service is more cost-effective for this project because it avoids VM administration overhead and provides managed hosting. The app can run on a basic or standard tier depending on requirements.

**Scalability:** App Service supports simple vertical and horizontal scaling through the Azure Portal. It can scale without manually configuring load balancers or additional servers.

**Availability:** App Service provides built-in availability features, managed infrastructure, HTTPS support, and easier recovery compared with a single VM deployment.

**Workflow:** Deployment is simpler using Azure CLI or GitHub/Azure DevOps pipelines. Application settings can be managed through environment variables, and logs can be viewed through Log Stream or stored under App Service logs.

## Decision

I chose **Azure App Service** for deploying the CMS application.

## Justification

Azure App Service is the better fit because this CMS app is a standard Flask web application that does not require deep operating-system-level customization. It needs reliable hosting, integration with Azure SQL Database, Azure Blob Storage for images, Microsoft authentication, and application logging. App Service supports these needs with less operational overhead than a VM.

A VM would provide more control, but that control is not necessary for this project. It would also require more manual work for patching, scaling, monitoring, security, and web server management. App Service allows the project to focus on application functionality rather than infrastructure maintenance.

## Assess App Changes That Would Change the Decision

I would reconsider using a VM if the application required significant OS-level customization or infrastructure control. Examples include:

- Custom background services or long-running worker processes that cannot run well in App Service
- Special networking requirements, such as complex private routing or custom firewall appliances
- Custom software or drivers that are not supported in App Service
- Requirement to control the operating system, patching schedule, or web server configuration directly
- Heavy compute processing, batch jobs, or workloads better suited for dedicated infrastructure
- Legacy dependencies that require a specific OS configuration
- Application architecture requiring multiple custom services installed on the same host

If the CMS app grew into a more complex platform with custom services, private networking, specialized dependencies, and heavy background processing, then a VM or container-based architecture could become more appropriate. For the current Flask CMS application, Azure App Service remains the best choice. 