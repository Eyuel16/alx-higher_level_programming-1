#!/usr/bin/python3
class LockedClass:
    """
    prevent the user from dynamicallly creating new instance attributes,
    except  if the new instance attribute is called first_name.

    >>> a = LockedClass()
    >>> a.first_name = "Amanuel"
    >>> a.first_name
    Amanuel

    >>> a.last_name = 'Ng'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
