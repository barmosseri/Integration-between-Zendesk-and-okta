![Okta 2 Zendesk](https://i.ibb.co/cQyr7Kf/Zendesk2-Okta.jpg)

Project Status: Active – The project has reached a stable, usable state and is being actively developed.(https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

# Zendesk 2 Okta

This script used to automate the process of creating users in Okta based on tickets in Zendesk. It allows only certain approved users to approve the creation of a user, and uses custom fields on the ticket to determine the details for the user to be created in Okta. It also updates the ticket with comments indicating the status of the user creation process and, if successful, marks the ticket as solved.

# Full information
This automation designed to automate the process of creating a new user in the Okta identity management service based on information provided in a Zendesk ticket. First, imports the necessary libraries and sets up the necessary client objects for accessing the Secrets Manager, Zendesk, and Okta services. It then retrieves the required API keys and access tokens from Secrets Manager and stores them in environment variables. Next, the automation send queries to Zendesk for tickets with the subject "create a new user" and iterates over the results. For each ticket, it checks the ticket's status and a custom field to see if it should be processed. If the ticket has a status of "pending", "on-hold", or "solved", or if the custom field does not match "OKTA - Access", the script moves on to the next ticket. If the ticket meets the necessary criteria, the script retrieves the first name, last name, email, and organization from the ticket's custom fields. If any of these fields are empty, the script adds a comment to the ticket stating that there are missing details and sets the status to "pending". If all of the necessary details are present, the script checks if the user already exists in Okta. If the user does exist, it sends a reset password email to the user and updates the ticket's status to "solved". If the user does not exist, the script checks for an approval from a member of the APPROVED_USER_GROUP_ID in the ticket's comments. If the ticket is approved, the script creates the user in Okta and adds a comment to the ticket stating that the user has been created. If the ticket is not approved, the script adds a comment to the ticket stating that the request has not been approved and sets the ticket's status to "pending".

## Requirements

* [boto3](https://pypi.org/project/boto3)
* [asyncio](https://pypi.org/project/asyncio)
* [aiohttp](https://pypi.org/project/aiohttp)
* [okta](https://pypi.org/project/okta) 
* [zenpy](https://pypi.org/project/zenpy)

## Support

* Email: barmosseri@gmail.com
* Linkedin: https://www.linkedin.com/in/barmosseri/

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
