# Options to acquire Azure DevOps Work Item data
# 1. Azure DevOps REST API
# 2. Azure DevOps Python SDK
# 3. Azure DevOps CLI
# 4. Azure DevOps PowerShell
# 5. Azure DevOps Node.js SDK
# 6. Azure DevOps OData REST API

# Azure DevOps Work Item REST API
# https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items?view=azure-devops-rest-7.0

# Azure DevOps Work Item OData REST API
# https://learn.microsoft.com/en-us/azure/devops/report/powerbi/odataquery-connect?view=azure-devops

# Azure DevOps Analytics Quick Reference
# https://learn.microsoft.com/en-us/azure/devops/report/extend-analytics/quick-ref?view=azure-devops

import requests
import json
import os
import sys

import dotenv

from dotenv import dotenv_values

# Load the environment variables from the .env file
config = dotenv_values(".env")

# print(config)

from dotenv import load_dotenv
load_dotenv()

 # Get the environment variables
personal_access_token = os.getenv('AZURE_DEVOPS_PERSONAL_ACCESS_TOKEN')
organization_url = os.getenv('AZURE_DEVOPS_ORGANIZATION_URL')
project_name = os.getenv('AZURE_DEVOPS_PROJECT_NAME')
team_name = os.getenv('AZURE_DEVOPS_TEAM_NAME')
work_item_type = os.getenv('AZURE_DEVOPS_WORK_ITEM_TYPE')
work_item_state = os.getenv('AZURE_DEVOPS_WORK_ITEM_STATE')
work_item_area_path = os.getenv('AZURE_DEVOPS_WORK_ITEM_AREA_PATH')
work_item_iteration_path = os.getenv('AZURE_DEVOPS_WORK_ITEM_ITERATION_PATH')

def emit(msg, *args):
    try:
        print(msg % args)
    except:
        print("there was an error somewhere")

def print_work_item(work_item):
    try:
        x = "{0}".format(work_item.fields["System.AssignedTo"])
        y = x.replace("'", "\"")
        z = json.loads(y)
        
        emit(
            "{0}:{1}:{2}:{3}:{4}".format(
                work_item.id,
                work_item.fields["System.Title"],
                work_item.fields["System.AreaPath"],
                work_item.fields["System.State"],
                z["displayName"]
                )
            )
    except:
        print("there was an error somewhere")

def query_azure_devops_org_project_workitems(type=work_item_type, state=work_item_state, project=project_name, team=team_name, iteration=work_item_iteration_path, tags=None, assigned_to=None, top=1000, skip=0, orderby='State,Changed Date', fields='System.Id,System.Title,System.State,System.AssignedTo,System.Tags,System.WorkItemType,System.AreaPath,System.IterationPath,System.ChangedDate,System.CreatedDate,System.CreatedBy,System.ChangedBy'):
    from azure.devops.connection import Connection
    from msrest.authentication import BasicAuthentication
    from azure.devops.v5_1.work_item_tracking.models import Wiql
    import pprint

    # print (organization_url)

    # Create a connection to the org
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)

    # Get a client (the "core" client provides access to projects, teams, etc)
    core_client = connection.clients.get_core_client()

    # Get a client (the "work item tracking" client provides access to work items)
    wit_client = connection.clients.get_work_item_tracking_client()
    
    # OPTION 1
    # Get the list of work items
    desired_ids = range(2000, 2010)
    work_items = wit_client.get_work_items(ids=desired_ids, error_policy="omit", expand="all")

    print(work_items)

    # OPTION 2
    # Use the Wiql class to build a query
    query="""
        select [System.Id],
            [System.NodeName],
            [System.WorkItemType],
            [System.Title],
            [System.State],
            [System.AreaPath],
            [System.IterationPath],
            [System.Tags],
            [System.AssignedTo]
        from WorkItems
        where [System.WorkItemType] = '""" + work_item_type + """' and [System.AreaPath] = '""" + work_item_area_path + """' and [System.IterationPath] = '""" + work_item_iteration_path + """' and [System.State] = '""" + work_item_state + """'
        order by [System.ChangedDate] desc"""
    
    print(query)

    wiql = Wiql(
        query=query
    )

    wiql_results = wit_client.query_by_wiql(wiql, top=30).work_items

    print(wiql_results)
    
    # emit("Results: {0}".format(len(wiql_results)))

    if wiql_results:
        work_items = (
            wit_client.get_work_item(int(res.id)) for res in wiql_results
        )
        for work_item in work_items:
            print_work_item(work_item)
        return work_items
    else:
        return None

if __name__ == "__main__":
    query_azure_devops_org_project_workitems()

# How to run the script
# python main.py

# How to install the azure devops python sdk
# https://docs.microsoft.com/en-us/azure/devops/integrate/quickstarts/client-library?view=azure-devops&tabs=python

# Run VSCode as Administrator
# python -m ensurepip
# python -m pip install --upgrade pip
# python -m pip install azure-devops
# python -m pip install --upgrade azure-devops
# python -m pip install requests
# python -m pip install dotenv
