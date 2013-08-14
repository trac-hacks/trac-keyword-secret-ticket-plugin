Adds ticket security policy based on keyword.

Install
=======

    python setup.py bdist_egg
    cp dist/TracKeywordSecretTicketsPlugin-1.0.2-py2.7.egg <path-of-trac-env>/plugins/

Usage
=====

In components part:

    [components]
    keywordsecretticket.policy.keywordsecretticketpolicy = enabled

In trac part:

    [trac]
    permission_policies = KeywordSecretTicketPolicy, ...

In kkbox part:

    [kkbox]
    insensitive_group = intern,outsourcing
    sensitive_keyword = secret

License
=======

3-clause BSD license.  Read COPYING.
