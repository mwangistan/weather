from rest_framework import status

class TranslateError:
    """ Maps external API errors to internal representation
    """
    def __init__(self):
        self.errors = {
            1006: ("No location found matching the city", status.HTTP_400_BAD_REQUEST),
        }

    def handle(self, err_code):
        if err_code in self.errors:
            return self.errors[err_code]
        return ("Error processing your request. Please contact an administrator", status.HTTP_500_INTERNAL_SERVER_ERROR)