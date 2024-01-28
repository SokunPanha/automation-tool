import re


class ErrorHandling:
    @staticmethod
    def validate_profile_name(profile_name):
        # Check if profile_name contains only alphanumeric characters and underscores
        return bool(re.match("^[a-zA-Z0-9_]*$", profile_name))

    @staticmethod
    def validate_email(email):
        # Check if email is in a valid format
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    @staticmethod
    def response_msg(message, data=None):
        if data is not None:
            return {"data": data, "response": [True, message]}
        else:
            return {"data": None, "response": [False, message]}