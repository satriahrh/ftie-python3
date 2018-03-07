class ValidationError(Exception):
    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super(ValidationError, self).__init__(message)

        # Now for your custom code...
        self.errors = errors


class DiscoveryError(Exception):
    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super(DiscoveryError, self).__init__(message)

        # Now for your custom code...
        self.errors = errors
