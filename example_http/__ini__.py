"""
This function responds to
GET https://<your-function>.azurewebsites.net/api/HttpExample?name=Severin
"""
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    if not name:
        try:
            body = req.get_json()
            name = body.get("name")
        except:
            pass

    if name:
        return func.HttpResponse(f"Hello {name}!", status_code=200)
    else:
        return func.HttpResponse(
            "Please provide a name in query or body",
            status_code=400
        )