# README

## Options to acquire Azure DevOps Work Item data
1. Azure DevOps REST API
2. Azure DevOps Python SDK
3. Azure DevOps CLI
4. Azure DevOps PowerShell
5. Azure DevOps Node.js SDK
6. Azure DevOps OData REST API

## How to run the Python script
```
python main.py
```

## How to compile the main.cs file
```
."C:\Program Files\Microsoft Visual Studio\2022\Enterprise\MSBuild\Current\Bin\Roslyn\csc.exe" .\main.cs
```

## How to install the azure devops python sdk
[Azure DevOps Python SDK](https://docs.microsoft.com/en-us/azure/devops/integrate/quickstarts/client-library?view=azure-devops&tabs=python)

## Run OData Query
1. Install the vscode-odata extension in VSCode
2. Modify and run main.odata

## Run VSCode as Administrator
```
python -m ensurepip
python -m pip install --upgrade pip
python -m pip install azure-devops
python -m pip install --upgrade azure-devops
python -m pip install requests
python -m pip install dotenv
```

## Resources
[Azure DevOps Work Item REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items?view=azure-devops-rest-7.0)

[Azure DevOps Work Item OData REST API](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/odataquery-connect?view=azure-devops)

[Azure DevOps Analytics Quick Reference](https://learn.microsoft.com/en-us/azure/devops/report/extend-analytics/quick-ref?view=azure-devops)

[Azure DevOps Analytics Data Model](https://learn.microsoft.com/en-us/azure/devops/report/extend-analytics/data-model-analytics-service?view=azure-devops)

[Grant Permissions to use Azure DevOps Analytics](https://learn.microsoft.com/en-us/azure/devops/report/powerbi/analytics-security?view=azure-devops&tabs=preview-page)

[Terraform Tutorial for Azure](https://developer.hashicorp.com/terraform/tutorials/azure-get-started/azure-build)

[Management Reports in Azure DevOps (Video)](https://www.youtube.com/watch?v=gqUFAAByPfU&t=8s)

[Management Reports in Azure DevOps (GitHub repo)](https://github.com/vinijmoura/Azure-DevOps)

## Community Blogs
[Vinicius Moura](https://vinijmoura.medium.com/)

## Credits
Dot ENV. As I searched for a pacakge to read the .env file, I found this article and thought it was a good idea to use the approach. Simple. No need to install any package. Also, makes complete sense. [Dusted](https://dusted.codes/dotenv-in-dotnet)