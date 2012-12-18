from trac.ticket.model import Ticket
from trac.core import Component, implements, TracError
from trac.perm import IPermissionPolicy

class KKBOXSecretTicketsPolicy(Component):
    implements(IPermissionRequestor, IPermissionPolicy)

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
        try:
            ticket = Ticket(self.env, res.id)
            has_relationship = self._has_relationship(ticket, perm.username)

            keywords = [keyword.strip() for keyword in ticket['keywords'].split(',')]
            if self.sensitive_keyword and \
               self.sensitive_keyword in keywords:
                return has_relationship
        except TracError as e:
            self.log.error(e.message)

        return None

    def _has_relationship(self, ticket, username):
        cc_list = [cc.strip() for cc in ticket['cc'].split(',')]

        return username == ticket['reporter'] or \
               username == ticket['owner'] or \
               username in cc_list
