import boto3
import asyncio
import aiohttp
import okta
import okta.models as models
import zenpy
from urllib.error import HTTPError
from okta.client import Client as OktaClient
from okta.models import User
from okta.models import UserProfile
from zenpy import Zenpy
from zenpy.lib.api_objects import CustomField, Ticket, Comment

APPROVED_USER_GROUP_ID = [10506817039505, 1900000688113]
first_name_field_id = 4413963262609
last_name_field_id = 8636631843729
email_field_id = 360022958317
organization_field_id = 11522783200529

client = boto3.client('secretsmanager')
zendesk_secret_value = client.get_secret_value(SecretId='Zendesk_API_Key')
okta_secret_value = client.get_secret_value(SecretId='Okta_API_Key')
zendesk_token = zendesk_secret_value['Token']
okta_token = okta_secret_value['Token']

zendesk_creds = {
    "email": "{Your_Email}",
    "token": zendesk_token,
    "subdomain": "{Your_Subdomain}"
}
zendesk_client = Zenpy(**zendesk_creds)
ticket_form = zendesk_client.ticket_forms(id=4414402109457)

config = {
    'orgUrl': '{Your_Okta_Url}',
    'token': okta_token
}
okta_client = OktaClient(config)

tickets = []
for ticket in zendesk_client.search(subject='{Your_Subject}', status='Open'):
    tickets.append(ticket)
    continue

for ticket in tickets:
    if ticket.ticket_form_id != 4414402109457:
        ticket.comment = Comment(body="The type of this ticket is incorrect. Please select 'OKTA - Access' in the form field.", public=True)
        ticket.custom_status_id = 4205178
        zendesk_client.tickets.update(ticket)
    else:
         continue

user_first_name = ""
user_last_name = ""
user_email = ""
user_organization = ""

required_field_ids = [first_name_field_id, last_name_field_id, email_field_id, organization_field_id]
all_required_fields_filled = True

if ticket.custom_fields:
    for field in ticket.custom_fields:
        if field["id"] in required_field_ids:
            if not field["value"] or len(field["value"]) == 0:
                all_required_fields_filled = False
                break

if not all_required_fields_filled:
    ticket.comment = Comment(body="Please make sure that you filled in all the required fields.", public=True)
    ticket.custom_status_id = 4205178
    zendesk_client.tickets.update(ticket)
else:
    for field in ticket.custom_fields:
        if field["id"] == first_name_field_id:
            user_first_name = field["value"]
        elif field["id"] == last_name_field_id:
            user_last_name = field["value"]
        elif field["id"] == email_field_id:
            user_email = field["value"]
        elif field["id"] == organization_field_id:
            user_organization = field["value"]

def groupID(user_id):
    global approved_user
    for identity in zendesk_client.users.groups(user_id):
        if identity.id in APPROVED_USER_GROUP_ID:
            approved_user = identity.name
            return True
    return False

async def main(user_email, ticket, okta_client):
    try:
        async with okta_client:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://{Your_Subdomain}.okta.com/api/v1/users/{user_email}") as resp:
                    user, resp, err = await okta_client.get_user(user_email)
                    print(user, resp, err)
                    
                    if user is not None:
                        await okta_client.reset_password(user_email)
                        ticket.comment = Comment(body="The user already exists. A reset password email has been sent.", public=True)
                        ticket.custom_status_id = 4205198
                        zendesk_client.tickets.update(ticket)
                    else:
                        for ticket in tickets:
                            approved = False
                            for comment in zendesk_client.tickets.comments(ticket):
                                print(comment.author_id)
                                if groupID(comment.author_id):
                                    if "approved" in comment.body.lower():
                                        approved = True
                                        break

                            if approved:
                                user_data = {
                                    "profile": {
                                    "firstName": user_first_name,
                                    "lastName": user_last_name,
                                    "email": user_email,
                                    "login": user_email,
                                    "userType": "customer",
                                    "organization": user_organization
                                    }
                                }
                                print(user_data['profile'])
                                await okta_client.create_user(user_data)
                                ticket.comment = Comment(body="The user has been created.", public=True)
                                ticket.custom_status_id = 4205198
                                zendesk_client.tickets.update(ticket)
                            else:
                                raise Exception(f"Failed to create user: {resp.status} {await resp.text()}")    
    except Exception as e:
        print(f'An error occurred: {e}')

async def run():
    await main(user_email, ticket, okta_client)
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
