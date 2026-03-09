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
        return func.HttpResponse(f"Hello, {name}!")
    else:
        return func.HttpResponse(
            "Hello! Pass a name in the query string.",
            status_code=200
        )
