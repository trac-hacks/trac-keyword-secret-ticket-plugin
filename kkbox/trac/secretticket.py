from trac.ticket.model import Ticket
from trac.core import Component, implements, TracError
from trac.perm import IPermissionPolicy

class KKBOXSecretTicketsPolicy(Component):
    implements(IPermissionPolicy)

    def __init__(self):
        config = self.env.config
        self.sensitive_keyword = config.get('kkbox', 'sensitive_keyword').strip()

    def check_permission(self, action, user, resource, perm):
        while resource:
            if 'ticket' == resource.realm:
                break
            resource = resource.parent

        if resource and 'ticket' == resource.realm and resource.id:
            return self.check_ticket_access(perm, resource)

    def check_ticket_access(self, perm, res):
        if not self.sensitive_keyword:
            return None

        try:
            ticket = Ticket(self.env, res.id)
            keywords = [k.strip() for k in ticket['keywords'].split(',')]
            if self.sensitive_keyword in keywords:
                cc_list = [cc.strip() for cc in ticket['cc'].split(',')]

                if perm.username == ticket['reporter'] or \
                   perm.username == ticket['owner'] or \
                   perm.username in cc_list:
                    return None
                else:
                    return False
        except TracError as e:
            self.log.error(e.message)
            return None
