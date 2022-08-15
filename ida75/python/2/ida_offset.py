# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: offset
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_offset
else:
    import _ida_offset

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

SWIG_PYTHON_LEGACY_BOOL = _ida_offset.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func


def get_default_reftype(*args):
    r"""


    Get default reference type depending on the segment.
    
    get_default_reftype(ea) -> reftype_t
        @param ea (C++: ea_t)
        @return: one of  REF_OFF8 , REF_OFF16 , REF_OFF32
    """
    return _ida_offset.get_default_reftype(*args)

def op_offset_ex(*args):
    r"""


    Convert operand to a reference. To delete an offset, use
    'clr_op_type()' function.
    
    op_offset_ex(ea, n, ri) -> bool
        @param ea: linear address. if 'ea' has unexplored bytes, try to
                   convert them to   no segment: fail   16bit segment: to
                   16bit word data   32bit segment: to dword (C++: ea_t)
        @param n: number of operand (may be ORed with  OPND_OUTER )   0: first
                  1: second   2: third   OPND_MASK : all operands (C++: int)
        @param ri: reference information (C++: const  refinfo_t  *)
        @return: success
    """
    return _ida_offset.op_offset_ex(*args)

def op_offset(*args):
    r"""


    See 'op_offset_ex()'
    
    op_offset(ea, n, type, target=BADADDR, base=0, tdelta=0) -> bool
        @param ea (C++: ea_t)
        @param n (C++: int)
        @param type (C++: reftype_t)
        @param target (C++: ea_t)
        @param base (C++: ea_t)
        @param tdelta (C++: adiff_t)
    """
    return _ida_offset.op_offset(*args)

def op_plain_offset(*args):
    r"""


    Convert operand to a reference with the default reference type.
    
    op_plain_offset(ea, n, base) -> bool
        @param ea (C++: ea_t)
        @param n (C++: int)
        @param base (C++: ea_t)
    """
    return _ida_offset.op_plain_offset(*args)

def get_offbase(*args):
    r"""


    Get offset base value
    
    get_offbase(ea, n) -> ea_t
        @param ea: linear address (C++: ea_t)
        @param n: number of operand (C++: int)
        @return: offset base or  BADADDR
    """
    return _ida_offset.get_offbase(*args)

def get_offset_expression(*args):
    r"""


    Get offset expression (in the form "offset name+displ"). This function
    uses offset translation function (\ph{translate}) if your IDP module
    has such a function. Translation function is used to map linear
    addresses in the program (only for offsets).Example: suppose we have
    instruction at linear address 0x00011000: \v{mov ax, [bx+7422h]} and
    at ds:7422h: \v{array dw ...} We want to represent the second operand
    with an offset expression, so then we call: \v{
    get_offset_expresion(0x001100, 1, 0x001102, 0x7422, buf); | | | | | |
    | | | +output buffer | | | +value of offset expression | | +address
    offset value in the instruction | +the second operand +address of
    instruction } and the function will return a colored string: \v{offset
    array}
    
    get_offset_expression(ea, n, _from, offset, getn_flags=0) -> str
        @param ea: start of instruction or data with the offset expression
                   (C++: ea_t)
        @param n: number of operand (may be ORed with  OPND_OUTER )   0: first
                  operand   1: second operand (C++: int)
        @param _from: linear address of instruction operand or data referring
                      to the name. This address will be used to get fixup
                      information, so it should point to exact position of
                      operand in the instruction. (C++: ea_t)
        @param offset: value of operand or its part. The function will return
                       text representation of this value as offset expression.
                       (C++: adiff_t)
        @param getn_flags: combination of:   GETN_APPZERO : meaningful only if
                           the name refers to a structure. appends the struct
                           field name if the field offset is zero
                           GETN_NODUMMY : do not generate dummy names for the
                           expression but pretend they already exist (useful
                           to verify that the offset expression can be
                           represented) (C++: int)
        @retval: 0 - can't convert to offset expression
        @retval: 1 - ok, a simple offset expression
        @retval: 2 - ok, a complex offset expression
    """
    return _ida_offset.get_offset_expression(*args)

def get_offset_expr(*args):
    r"""


    See 'get_offset_expression()'
    
    get_offset_expr(ea, n, ri, _from, offset, getn_flags=0) -> str
        @param ea (C++: ea_t)
        @param n (C++: int)
        @param ri (C++: const  refinfo_t  &)
        @param _from (C++: ea_t)
        @param offset (C++: adiff_t)
        @param getn_flags (C++: int)
    """
    return _ida_offset.get_offset_expr(*args)

def can_be_off32(*args):
    r"""


    Does the specified address contain a valid OFF32 value?. For symbols
    in special segments the displacement is not taken into account. If
    yes, then the target address of OFF32 will be returned. If not, then
    'BADADDR' is returned.
    
    can_be_off32(ea) -> ea_t
        @param ea (C++: ea_t)
    """
    return _ida_offset.can_be_off32(*args)

def calc_offset_base(*args):
    r"""


    Try to calculate the offset base This function takes into account the
    fixup information, current ds and cs values.
    
    calc_offset_base(ea, n) -> ea_t
        @param ea: the referencing instruction/data address (C++: ea_t)
        @param n: operand number   0: first operand   1: other operand (C++:
                  int)
        @return: output base address or  BADADDR
    """
    return _ida_offset.calc_offset_base(*args)

def calc_probable_base_by_value(*args):
    r"""


    Try to calculate the offset base. 2 bases are checked: current ds and
    cs. If fails, return 'BADADDR'
    
    calc_probable_base_by_value(ea, off) -> ea_t
        @param ea (C++: ea_t)
        @param off (C++: uval_t)
    """
    return _ida_offset.calc_probable_base_by_value(*args)

def calc_reference_data(*args):
    r"""


    Calculate the target and base addresses of an offset expression. The
    calculated target and base addresses are returned in the locations
    pointed by 'base' and 'target'. In case 'ri.base' is 'BADADDR' , the
    function calculates the offset base address from the referencing
    instruction/data address. The target address is copied from ri.target.
    If ri.target is 'BADADDR' then the target is calculated using the base
    address and 'opval'. This function also checks if 'opval' matches the
    full value of the reference and takes in account the memory-mapping.
    
    calc_reference_data(target, base, _from, ri, opval) -> bool
        @param target: output target address (C++: ea_t *)
        @param base: output base address (C++: ea_t *)
        @param _from: the referencing instruction/data address (C++: ea_t)
        @param ri: reference info block from the database (C++: const
                   refinfo_t  &)
        @param opval: operand value (usually  op_t::value  or  op_t::addr )
                      (C++: adiff_t)
        @return: success
    """
    return _ida_offset.calc_reference_data(*args)

def add_refinfo_dref(*args):
    r"""


    Add xrefs for a reference from the given instruction (\insn_t{ea}).
    This function creates a cross references to the target and the base.
    'insn_t::add_off_drefs()' calls this function to create xrefs for
    'offset' operand.
    
    add_refinfo_dref(insn, _from, ri, opval, type, opoff) -> ea_t
        @param insn: the referencing instruction  - an ida_ua.insn_t, or an
                     address (C++: const insn_t &)
        @param _from: the referencing instruction/data address (C++: ea_t)
        @param ri: reference info block from the database (C++: const
                   refinfo_t  &)
        @param opval: operand value (usually  op_t::value  or  op_t::addr )
                      (C++: adiff_t)
        @param type: type of xref (C++: dref_t)
        @param opoff: offset of the operand from the start of instruction
                      (C++: int)
        @return: the target address of the reference
    """
    return _ida_offset.add_refinfo_dref(*args)

def calc_target(*args):
    r"""


    Calculates the target, using the provided 'refinfo_t' .
    
    calc_target(_from, opval, ri) -> ea_t
        @param _from (C++: ea_t)
        @param opval (C++: adiff_t)
        @param ri (C++: const  refinfo_t  &)
    

    calc_target(_from, ea, n, opval) -> ea_t
        @param _from (C++: ea_t)
        ea: ea_t
        n: int
        @param opval (C++: adiff_t)
    """
    return _ida_offset.calc_target(*args)

def calc_basevalue(*args):
    r"""


    Calculate the value of the reference base.
    
    calc_basevalue(target, base) -> ea_t
        @param target (C++: ea_t)
        @param base (C++: ea_t)
    """
    return _ida_offset.calc_basevalue(*args)

if _BC695:
    calc_reference_basevalue=calc_basevalue
    calc_reference_target=calc_target
    def set_offset(ea, n, base):
        import ida_idaapi
        otype = get_default_reftype(ea)
        return op_offset(ea, n, otype, ida_idaapi.BADADDR, base) > 0



