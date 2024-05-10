# Deal_Project_API
Deal API
Overview
The Deal API is a backend API built using Django and MongoDB that allows users to manage financial transactions (deals) consisting of one or more projects. Each project has associated details such as fair market value (FMV) and tax credit transfer rate.
----------------------------------------------------------------------------------------------------------
Features
Create, edit, and delete deals
Add projects to deals and calculate tax credit transfer amounts
Retrieve tax credit transfer amounts for deals and project
--------------------------------------------------------------------------------------------------------
Usage
Creating a Project:
Endpoint: /create-project/
Method: POST
Request Body: JSON object with project details (name, FMV, tax_credit_transfer_rate)
Creating a Deal:
Endpoint: /create-deal/
Method: POST
Request Body: JSON object with deal details (name, project_name, FMV, tax_credit_transfer_rate)
Getting Tax Credit Transfer Amount for a Deal:
Endpoint: /deal-tax-credit-transfer/<deal_name>/
Method: GET
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
