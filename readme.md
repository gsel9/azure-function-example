# NOTE:
- Fails due to no storage account
- Should prolly configure access to storage account via Functions by assigning a role to the Function resource

https://learn.microsoft.com/en-gb/azure/azure-functions/functions-develop-vs-code?tabs=node-v4%2Cpython-v2%2Cisolated-process%2Cquick-create&pivots=programming-language-python

https://learn.microsoft.com/en-us/azure/azure-functions/scenario-scheduled-tasks?pivots=programming-language-python&tabs=linux

1. Create rg
2. Create function
3. Create storage account
4. Assign identities:
    - function is storage reader and writer