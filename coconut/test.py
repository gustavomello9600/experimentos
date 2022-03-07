#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4e72f0b2

# Compiled with Coconut version 1.4.3 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get("__coconut__")
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules["__coconut__"]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

@_coconut_tco
@_coconut_mark_as_match
def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):
        numbers = _coconut.iter(_coconut_match_to_args[0])
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(numbers, _coconut.slice(None, 1)))
        if (_coconut.len(_coconut_match_temp_0) == 1) and (not _coconut_match_to_kwargs):
            p = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
        _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def sieve( (|p|) :: numbers ) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
        _coconut_match_err.pattern = 'def sieve( (|p|) :: numbers ) ='
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: (_coconut_func() for _coconut_func in (lambda: p,)), lambda: sieve(filter(lambda n: n % p != 0, numbers)))))
primes = (_coconut_forward_compose(count, sieve))(2)

(_coconut_forward_compose(enumerate, list, print))(_coconut_igetitem(primes, _coconut.slice(None, 100)))
