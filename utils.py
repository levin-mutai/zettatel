from .app import Client


def api_exist():
    api = Client.get_api_key()

    if api.json()['response']['code'] == "253":
        try:

            res = Client.create_api_key()
            if res.json()["response"]["status"] == 'error':
                raise ValueError(res.json()["response"]["msg"])

            else:
                res = Client.get_api_key()
                return res.json()['response']['apikeyList']['apikey']

        except Exception as err:
            return str(err)

    else:
        return api.json()['response']['apikeyList']['apikey']
