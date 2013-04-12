#
# Copyright (C) 2012-2013 KKBOX Technologies Limited
# Copyright (C) 2012-2013 Gasol Wu <gasol.wu@gmail.com>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from trac.ticket.model import Ticket
from trac.core import Component, implements, TracError, ExtensionPoint
from trac.perm import IPermissionPolicy, IPermissionGroupProvider, PermissionSystem

class KeywordSecretTicketPolicy(Component):
    implements(IPermissionPolicy)
    group_providers = ExtensionPoint(IPermissionGroupProvider)

    def __init__(self):
        config = self.env.config
        self.sensitive_keyword = config.get('kkbox', 'sensitive_keyword').strip()
        self.insensitive_group = set([g.strip() for g in config.get('kkbox', 'insensitive_group').split(',')])

    def check_permission(self, action, user, resource, perm):
        if 'TICKET_VIEW' != action:
            return None

        while resource:
            if 'ticket' == resource.realm:
                break
            resource = resource.parent

        if resource and \
           'ticket' == resource.realm and \
           resource.id:
            return self.check_ticket_access(perm, resource)

    def check_ticket_access(self, perm, res):
        try:
            ticket = Ticket(self.env, res.id)
            has_relationship = self._has_relationship(ticket, perm.username)

            groups = self._get_groups(perm.username)
            if self.insensitive_group & groups and \
               not has_relationship:
                return False

            keywords = [keyword.strip() for keyword in ticket['keywords'].split(',')]
            if self.sensitive_keyword and \
               self.sensitive_keyword in keywords and \
               not has_relationship:
                return False
        except TracError as e:
            self.log.error(e.message)

        return None

    def _has_relationship(self, ticket, username):
        username = username.lower()
        cc_list = [cc.strip().lower() for cc in ticket['cc'].split(',')]

        return username == ticket['reporter'].lower() or \
               username == ticket['owner'].lower() or \
               username in cc_list

    def _get_groups(self, user):
        groups = set([user])
        for provider in self.group_providers:
            for group in provider.get_permission_groups(user):
                groups.add(group)

        perms = PermissionSystem(self.env).get_all_permissions()
        repeat = True
        while repeat:
            repeat = False
            for subject, action in perms:
                if subject in groups and not action.isupper() and action not in groups:
                    groups.add(action)
                    repeat = True

        return groups
