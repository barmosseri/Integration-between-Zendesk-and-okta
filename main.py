import boto3
import os
from zendesk import Zendesk
from okta.models.user import User
from okta.client import Client

APPROVED_USER_GROUP_ID = [1234, 5678]
secrets_client = boto3.client('secretsmanager')
zendesk_token_secret = secrets_client.get_secret_value(SecretId='ZENDESK_TOKEN')
zendesk_token = zendesk_token_secret['SecretString']
okta_token_secret = secrets_client.get_secret_value(SecretId='OKTA_TOKEN')
okta_token = okta_token_secret['SecretString']

os.environ['ZENDESK_TOKEN'] = zendesk_token
os.environ['OKTA_TOKEN'] = okta_token
zendesk_client = Zendesk(os.environ['ZENDESK_TOKEN'])
okta_client = Client(os.environ['OKTA_TOKEN'])

tickets = zendesk_client.search(query='subject:create a new user').get('results')
for ticket in tickets:
    # Extract the custom fields
    first_name = ticket['custom_fields'][FIRST_NAME_FIELD_ID]
    last_name = ticket['custom_fields'][LAST_NAME_FIELD_ID]
    email = ticket['custom_fields'][EMAIL_FIELD_ID]
    organization = ticket['custom_fields'][ORGANIZATION_FIELD_ID]
    if not all(val for val in [first_name, last_name, email, organization]):
        zendesk_client.tickets.create_comment(ticket['id'], {'body': 'There are missing details in the ticket.', 'public': True})
        continue
		
	approved = False
    comments = zendesk_client.tickets.comments(ticket['id']).get('comments')
    if comment['is_public'] == False and comment['author_id'] in APPROVED_USER_GROUP_ID and comment['body'].strip().lower() == 'Approved':
    approved = True
    break
    
    if approved:
        first_name = ticket['custom_fields'][FIRST_NAME_FIELD_ID]
        last_name = ticket['custom_fields'][LAST_NAME_FIELD_ID]
        email = ticket['custom_fields'][EMAIL_FIELD_ID]
        organization = ticket['custom_fields'][ORGANIZATION_FIELD_ID]
        # Create the user in Okta
        user = User(profile={'firstName': first_name, 'lastName': last_name, 'email': email, 'organization': organization}, status='ACTIVE'))
        okta_client.users.create(user)
        zendesk_client.tickets.create_comment(ticket['id'], {'body': 'The user has been created.', 'public': True})
		zendesk_client.tickets.update(id=ticket['id'], status='solved')
    else:
        zendesk_client.tickets.create_comment(ticket['id'], {'body': 'The request wasn't approved', 'public': True})
		zendesk_client.tickets.update(id=ticket['id'], status='on-hold')
    
if __name__ == "__main__":
