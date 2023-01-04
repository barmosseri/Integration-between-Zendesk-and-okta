![Okta 2 Zendesk](https://i.ibb.co/cQyr7Kf/Zendesk2-Okta.jpg)

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
