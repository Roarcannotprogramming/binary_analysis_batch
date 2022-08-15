# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: strlist
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_strlist
else:
    import _ida_strlist

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """
    Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass
    """
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """
    Meta class to enforce nondynamic attributes (no new attributes) for a class
    """
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

SWIG_PYTHON_LEGACY_BOOL = _ida_strlist.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

class strwinsetup_t(object):
    r"""
    Proxy of C++ strwinsetup_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> strwinsetup_t
        """
        _ida_strlist.strwinsetup_t_swiginit(self, _ida_strlist.new_strwinsetup_t(*args))
    minlen = property(_ida_strlist.strwinsetup_t_minlen_get, _ida_strlist.strwinsetup_t_minlen_set)
    display_only_existing_strings = property(_ida_strlist.strwinsetup_t_display_only_existing_strings_get, _ida_strlist.strwinsetup_t_display_only_existing_strings_set)
    only_7bit = property(_ida_strlist.strwinsetup_t_only_7bit_get, _ida_strlist.strwinsetup_t_only_7bit_set)
    ignore_heads = property(_ida_strlist.strwinsetup_t_ignore_heads_get, _ida_strlist.strwinsetup_t_ignore_heads_set)

    def is_initialized(self, *args):
        r"""
        is_initialized(self) -> bool
        """
        return _ida_strlist.strwinsetup_t_is_initialized(self, *args)

    def _get_strtypes(self, *args):
        r"""
        _get_strtypes(self) -> PyObject *
        """
        return _ida_strlist.strwinsetup_t__get_strtypes(self, *args)

    def _set_strtypes(self, *args):
        r"""


        _set_strtypes(self, py_t) -> PyObject *
            py_t: PyObject *
        """
        return _ida_strlist.strwinsetup_t__set_strtypes(self, *args)

    strtypes = property(_get_strtypes, _set_strtypes)

    __swig_destroy__ = _ida_strlist.delete_strwinsetup_t

# Register strwinsetup_t in _ida_strlist:
_ida_strlist.strwinsetup_t_swigregister(strwinsetup_t)

class string_info_t(object):
    r"""
    Proxy of C++ string_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ea = property(_ida_strlist.string_info_t_ea_get, _ida_strlist.string_info_t_ea_set)
    length = property(_ida_strlist.string_info_t_length_get, _ida_strlist.string_info_t_length_set)
    type = property(_ida_strlist.string_info_t_type_get, _ida_strlist.string_info_t_type_set)

    def __init__(self, *args):
        r"""


        __init__(self) -> string_info_t
            _ea: ea_t
        """
        _ida_strlist.string_info_t_swiginit(self, _ida_strlist.new_string_info_t(*args))

    def __lt__(self, *args):
        r"""


        __lt__(self, r) -> bool
            r: string_info_t const &
        """
        return _ida_strlist.string_info_t___lt__(self, *args)
    __swig_destroy__ = _ida_strlist.delete_string_info_t

# Register string_info_t in _ida_strlist:
_ida_strlist.string_info_t_swigregister(string_info_t)


def get_strlist_options(*args):
    r"""


    Get access to the static string list options.
    """
    return _ida_strlist.get_strlist_options(*args)

def build_strlist(*args):
    r"""


    Build the string list. You should initialize options before this call
    using the restore_config() or setup_strings_window() methods.
    """
    return _ida_strlist.build_strlist(*args)

def clear_strlist(*args):
    r"""


    Clear the string list.
    """
    return _ida_strlist.clear_strlist(*args)

def get_strlist_qty(*args):
    r"""


    Get number of elements in the string list.
    """
    return _ida_strlist.get_strlist_qty(*args)

def get_strlist_item(*args):
    r"""


    Get nth element of the string list (n=0.. 'get_strlist_qty()' -1)
    
    get_strlist_item(si, n) -> bool
        @param si (C++: string_info_t  *)
        @param n (C++: size_t)
    """
    return _ida_strlist.get_strlist_item(*args)

if _BC695:
    def refresh_strlist(*args):
        build_strlist()



