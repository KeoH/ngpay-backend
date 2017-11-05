
class OperationManagerMixin(object):

    def get_refunds(self):
        return self.refunds.all()

    def has_refunds(self):
        return self.get_refunds().count() > 0

    def get_captures(self):
        return self.captures.all()

    def has_captures(self):
        return self.get_captures().count() > 0

    def get_authorizations(self):
        return self.authorizations.all()

    def has_authorizations(self):
        return self.get_authorizations().count() > 0

    def get_auth_and_capture(self):
        return self.authorizations_and_captures.all()

    def has_auth_and_capture(self):
        return self.get_auth_and_capture().count() > 0

    def get_voids(self):
        return self.voids.all()

    def has_voids(self):
        return self.get_voids().count() > 0