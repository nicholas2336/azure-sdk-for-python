# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.confluent import ConfluentManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-confluent
# USAGE
    python validations_validate_organizations_v2.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ConfluentManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.validations.validate_organization_v2(
        resource_group_name="myResourceGroup",
        organization_name="myOrganization",
        body={
            "location": "West US",
            "properties": {
                "offerDetail": {
                    "id": "string",
                    "planId": "string",
                    "planName": "string",
                    "privateOfferId": "string",
                    "privateOfferIds": ["string"],
                    "publisherId": "string",
                    "termUnit": "string",
                },
                "userDetail": {
                    "aadEmail": "abc@microsoft.com",
                    "emailAddress": "abc@microsoft.com",
                    "firstName": "string",
                    "lastName": "string",
                    "userPrincipalName": "abc@microsoft.com",
                },
            },
            "tags": {"Environment": "Dev"},
        },
    )
    print(response)


# x-ms-original-file: specification/confluent/resource-manager/Microsoft.Confluent/stable/2023-08-22/examples/Validations_ValidateOrganizationsV2.json
if __name__ == "__main__":
    main()
