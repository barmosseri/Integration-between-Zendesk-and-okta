![Integration-between-Zendesk-and-okta]([https://files.readme.io/8ba3f14-onify-blueprints-logo.png](https://i.ibb.co/cQyr7Kf/Zendesk2-Okta.jpg))

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
![Test suite](https://github.com/onify/blueprint-zendesk-create-update-ticket/workflows/Test%20suite/badge.svg)

# Onify Blueprint: Create and update ticket in Zendesk

[Zendesk](https://zendesk.com/) is one of the most used ticketing and customer success solutions. In this Blueprint we show how to first create a new ticket and then update the same ticket using a BPMN process in Onify. Everyting is done through [Zendesk REST API](https://developer.zendesk.com/api-reference/).

![Onify Blueprint: Create and update ticket in Zendesk](blueprint.jpg "Flow")

## Requirements

* [Onify Hub](https://github.com/onify/install)
* [Camunda Modeler](https://camunda.com/download/modeler/)
* [Zendesk](https://zendesk.com/) 

## Included

* 1 x Flows

## Setup

### Deploy

1. Open flow/bpmn in Camunda Modeler
2. Change settings/vars the the `Define Zendesk settings` task
4. Click `Deploy current diagram` and follow the steps

### Run 

To test and run the flow, click `Start Current Diagram`

## Support

* Community/forum: https://support.onify.co/discuss
* Documentation: https://support.onify.co/docs
* Support and SLA: https://support.onify.co/docs/get-support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.






















This script used to automate the process of creating users in Okta based on tickets in Zendesk. It allows only certain approved users to approve the creation of a user, and uses custom fields on the ticket to determine the details for the user to be created in Okta. It also updates the ticket with comments indicating the status of the user creation process and, if successful, marks the ticket as solved.

More informative:
This automation designed to automate the process of creating a new user in the Okta identity management service based on information provided in a Zendesk ticket.
First, imports the necessary libraries and sets up the necessary client objects for accessing the Secrets Manager, Zendesk, and Okta services. It then retrieves the required API keys and access tokens from Secrets Manager and stores them in environment variables.
Next, the automation send queries to Zendesk for tickets with the subject "create a new user" and iterates over the results. For each ticket, it checks the ticket's status and a custom field to see if it should be processed. If the ticket has a status of "pending", "on-hold", or "solved", or if the custom field does not match "OKTA - Access", the script moves on to the next ticket.
If the ticket meets the necessary criteria, the script retrieves the first name, last name, email, and organization from the ticket's custom fields. If any of these fields are empty, the script adds a comment to the ticket stating that there are missing details and sets the status to "pending".
If all of the necessary details are present, the script checks if the user already exists in Okta. If the user does exist, it sends a reset password email to the user and updates the ticket's status to "solved". If the user does not exist, the script checks for an approval from a member of the APPROVED_USER_GROUP_ID in the ticket's comments. If the ticket is approved, the script creates the user in Okta and adds a comment to the ticket stating that the user has been created. If the ticket is not approved, the script adds a comment to the ticket stating that the request has not been approved and sets the ticket's status to "pending".
