from django import template

from provider.scope import check
from ..constants import SCOPES

register = template.Library()


@register.filter
def scopes(scope):
    """
    Returns a list of scope names as defined in
    :attr:`oauth2_provider.constants.SCOPES` for a given scope integer.

    This function is almost same as `provider.templatetags.scopes` except ordering of scope.
    """
    return [
        name
        for (value, name) in SCOPES
        if check(value, scope)
    ]
