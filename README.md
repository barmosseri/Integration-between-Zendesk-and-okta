![Okta 2 Zendesk](https://i.ibb.co/cQyr7Kf/Zendesk2-Okta.jpg)

Project Status: Active – The project has reached a stable, usable state and is being actively developed.
![https://www.repostatus.org/#wip](https://user-images.githubusercontent.com/76659584/211010037-f264dc21-57db-4158-b3b6-768ddf93db06.png)

# Zendesk 2 Okta

Automate the process of creating users in Okta based on tickets in Zendesk. It allows only certain approved users to approve the creation of a user, and uses custom fields on the ticket to determine the details for the user to be created in Okta. It also updates the ticket with comments indicating the status of the user creation process and, if successful, marks the ticket as solved.

# Full information
A sophisticated automation solution that streamlines the process of ticket validation and management by connecting to various web services. The script begins by leveraging the AWS Secrets Manager to securely retrieve API tokens for Zendesk and Okta, which are then used to authenticate and establish a connection with the respective APIs. This allows the script to interact with and perform actions on the Zendesk and Okta platforms.
The script then employs the Zendesk API to search for open tickets with a specified subject, and subsequently reviews each ticket's form type. If the form type is not in compliance with the established standards, the script updates the ticket status and adds a comment to the ticket, providing detailed information on the issue and how it can be resolved. Additionally, the script verifies that all required fields on the form have been filled in and, if not, updates the ticket status and adds a comment accordingly.
Furthermore, the script utilizes the Okta API to confirm that the user requesting the ticket is part of an approved group, and retrieves the user's information from Okta for further validation. The script then verifies that the user is authorized to access the requested service, and if not, the script updates the ticket status and adds a comment to the ticket, providing detailed information on the issue and how it can be resolved.
In summary, this script provides a comprehensive and automated solution for the validation and management of tickets on Zendesk, while also verifying the user's status and authorization on Okta. This ensures that only authorized and compliant tickets are processed, improving the efficiency and security of the ticket management process.

## Requirements

* [boto3](https://pypi.org/project/boto3)
* [asyncio](https://pypi.org/project/asyncio)
* [aiohttp](https://pypi.org/project/aiohttp)
* [okta](https://pypi.org/project/okta) 
* [zenpy](https://pypi.org/project/zenpy)

## Support

* Email: barmosseri@gmail.com
* Linkedin: https://www.linkedin.com/in/barmosseri

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
