from messages.utils import send_request


class API:

    def get_api_key(self):

        url = f"https://portal.zettatel.com/SMSApi/apikey/read?userid={self.userid}&password={self.password}&output={self.output}"

        return send_request(url, "GET")

    def create_api_key(self):

        response = send_request(
            "https://portal.zettatel.com/SMSApi/apikey/create",
            "POST",
            {'userid': self.userid, 'password': self.password, 'output': self.output})

        return response
