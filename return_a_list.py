# works

# python AWS-Lambda-Function 
# to return only a list from a dynamoDB query using string set SS

"""
Example Table format/setup": sample tabled called "NAME_OF_YOUR_TABLE"
json view of item below (actual example to work with this starter code)


DynamoDB -> Items: NAME_OF_YOUR_TABLE -> Item editor

{
  "NAME_OF_PRIMARY_KEY_FIELD": {
    "N": "0"
  },
  "NAME_OF_FIELD_YOU_WANT_RETURNED": {
    "SS": [
      "string1, string2, etc, etc"
    ]
  }
}

"""

import boto3
from boto3.dynamodb.conditions import Key
import json


# helper function
def return_list_from_String_Set_SS(table_name,
                                   dynamodb_client, 
                                   field_you_want_returned, 
                                   primary_key_PK, 
                                   PK_query_attribute_type, 
                                   PK_query_data_type, 
                                   PK_query_text):

    response = dynamodb_client.query(
        TableName = table_name,
        # "ProjectionExpression" is fields/columns that you want returned
        ProjectionExpression = field_you_want_returned ,   
        KeyConditionExpression = f'{primary_key_PK} = :PK_query',
        ExpressionAttributeValues = {
            ':PK_query': {PK_query_data_type: PK_query_text}
        }
    )

    # go into dictionary to get just the desired list
    query_list = response['Items'][0][field_you_want_returned][PK_query_attribute_type]

    return query_list


def lambda_handler(event, context):

    # Creating the DynamoDB Client
    dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

    ##################################
    # Create Variables for your Query 
    ##################################
    table_name = "NAME_OF_YOUR_TABLE"
    field_you_want_returned = "NAME_OF_FIELD_YOU_WANT_RETURNED"
    # 'SS' for string set (list), or 'NS' for number set (list)
    PK_query_attribute_type = 'SS' 
    primary_key_PK = 'NAME_OF_PRIMARY_KEY_FIELD'
    # 'N' for number 'S' for string, etc. 
    PK_query_data_type = 'N'
    # All queries should be strings in python. e.g. int 2 should be: str "2"
    PK_query_text = "0" #'YOUR_SPECIFIC_QUERY_HERE'

    ##########################################################
    # Run the helper function to get the list from your query 
    ##########################################################
    output = return_list_from_String_Set_SS(table_name,                                            
                                            dynamodb_client, 
                                            field_you_want_returned, 
                                            primary_key_PK, 
                                            PK_query_attribute_type, 
                                            PK_query_data_type, 
                                            PK_query_text)

    return output

    # return {
    #     'statusCode': 200,
    #     'body1': output
    # }
