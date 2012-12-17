from trac.core import Component, implements
from trac.perm import IPermissionRequestor

class KKBOXSecretTicketsPolicy(Component):
    implements(IPermissionRequestor)

    def get_permission_actions(self):
        return ['SECRET_VIEW']
