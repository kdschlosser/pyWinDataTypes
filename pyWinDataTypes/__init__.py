# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

from ctypes.wintypes import (
    VARIANT_BOOL,
    RECT,
    SMALL_RECT,
    _COORD as COORD,
    POINT,
    POINTL,
    SIZEL,
    SIZE,
    FILETIME,
    MSG,
    MAX_PATH,
    WIN32_FIND_DATAA,
    WIN32_FIND_DATAW,
)


from ctypes import (
    POINTER,
    CFUNCTYPE,
    WINFUNCTYPE,
    Structure,
    sizeof,
    c_void_p,
    c_ulonglong,
    c_ulong,
    c_long,
    c_longlong,
    c_byte,
    c_double,
    c_float,
    c_int,
    c_wchar_p,
    c_char_p,
    c_short,
    c_uint,
    c_ushort,
    c_wchar,
    c_char,
    c_size_t,
    c_ssize_t,
    c_int8,
    c_int16,
    c_int32,
    c_int64,
    c_uint8,
    c_uint16,
    c_uint32,
    c_uint64
)
if sizeof(c_long) == sizeof(c_void_p):
    UINT_PTR = c_ulong
    LONG_PTR = c_long
    ULONG_PTR = c_ulong
elif sizeof(c_longlong) == sizeof(c_void_p):
    UINT_PTR = c_ulonglong
    LONG_PTR = c_longlong
    ULONG_PTR = c_ulonglong
else:
    UINT_PTR = c_ulong
    LONG_PTR = c_long
    ULONG_PTR = c_ulong

HANDLE = c_void_p
BOOL = c_long
BYTE = c_byte
CHAR = c_char
DWORD = c_ulong
DOUBLE = c_double
FLOAT = c_float
INT = c_int
LARGE_INTEGER = c_longlong
LONG = c_long
LONGLONG = c_longlong
LPCOLESTR = c_wchar_p
LPCSTR = c_char_p
LPCVOID = c_void_p
LPCWSTR = c_wchar_p
LPOLESTR = c_wchar_p
LPSTR = c_char_p
LPVOID = c_void_p
LPWSTR = c_wchar_p
OLESTR = c_wchar_p
SHORT = c_short
ULARGE_INTEGER = c_ulonglong
ULONG = c_ulong
ULONGLONG = c_ulonglong
WCHAR = c_wchar
WORD = c_ushort
USHORT = c_ushort
SIZE_T = c_size_t
SSIZE_T = c_ssize_t
INT8 = c_int8
INT16 = c_int16
INT32 = c_int32
INT64 = c_int64
UINT = c_uint
UINT8 = c_uint8
UINT16 = c_uint16
UINT32 = c_uint32
UINT64 = c_uint64


ATOM = WORD
BOOLEAN = BYTE
CALLBACK = CFUNCTYPE
CCHAR = CHAR
COLORREF = DWORD
DWORDLONG = UINT64
DWORD_PTR = ULONG_PTR
DWORD32 = UINT32
DWORD64 = UINT64
HACCEL = HANDLE
HALF_PTR = INT
HBITMAP = HANDLE
HBRUSH = HANDLE
HCOLORSPACE = HANDLE
HCONV = HANDLE
HCONVLIST = HANDLE
HICON = HANDLE
HSTR = HANDLE
HTASK = HANDLE
HCURSOR = HICON
HDC = HANDLE
HDDEDATA = HANDLE
HDESK = HANDLE
HDROP = HANDLE
HDWP = HANDLE
HENHMETAFILE = HANDLE
HFILE = INT
HFONT = HANDLE
HGDIOBJ = HANDLE
HGLOBAL = HANDLE
HHOOK = HANDLE
HINSTANCE = HANDLE
HKEY = HANDLE
HKL = HANDLE
HLOCAL = HANDLE
HMENU = HANDLE
HMETAFILE = HANDLE
HMODULE = HINSTANCE
HMONITOR = HANDLE
HPALETTE = HANDLE
HPEN = HANDLE
HRESULT = LONG
HRGN = HANDLE
HRSRC = HANDLE
HSZ = HANDLE
HWINSTA = HANDLE
HWND = HANDLE
INT_PTR = INT64
LANGID = WORD
LCID = DWORD
LCTYPE = DWORD
LGRPID = DWORD
LONG32 = INT32
LONG64 = INT64
LPARAM = LONG_PTR
LPBOOL = POINTER(BOOL)
LPBYTE = POINTER(BYTE)
LPCOLORREF = POINTER(COLORREF)
LPCTSTR = LPCWSTR
LPDWORD = POINTER(DWORD)
LPHANDLE = POINTER(HANDLE)
LPINT = POINTER(INT)
LPLONG = POINTER(LONG)
LPTSTR = LPWSTR
LPWORD = POINTER(WORD)
LRESULT = LONG_PTR
PBOOL = POINTER(BOOL)
PBOOLEAN = POINTER(BOOLEAN)
PBYTE = POINTER(BYTE)
PCHAR = POINTER(CHAR)
PCSTR = POINTER(CHAR)
PCTSTR = LPCWSTR
PCWSTR = POINTER(WCHAR)
PDWORD = POINTER(DWORD)
PDWORDLONG = POINTER(DWORDLONG)
PDWORD_PTR = POINTER(DWORD_PTR)
PDWORD32 = POINTER(DWORD32)
PDWORD64 = POINTER(DWORD64)
PFLOAT = POINTER(FLOAT)
PHALF_PTR = POINTER(HALF_PTR)
PHANDLE = POINTER(HANDLE)
PHKEY = POINTER(HKEY)
PINT = POINTER(INT)
PINT_PTR = POINTER(INT_PTR)
PINT8 = POINTER(INT8)
PINT16 = POINTER(INT16)
PINT32 = POINTER(INT32)
PINT64 = POINTER(INT64)
PLCID = POINTER(LCID)
PLONG = POINTER(LONG)
PLONGLONG = POINTER(LONGLONG)
PLONG_PTR = POINTER(LONG_PTR)
PLONG32 = POINTER(LONG32)
PLONG64 = POINTER(LONG64)
POINTER_32 = POINTER
POINTER_64 = POINTER
POINTER_SIGNED = POINTER
POINTER_UNSIGNED = POINTER
PSHORT = POINTER(SHORT)
PSIZE_T = POINTER(SIZE_T)
PSSIZE_T = POINTER(SSIZE_T)
PSTR = POINTER(CHAR)
TBYTE = WCHAR
TCHAR = WCHAR
PTBYTE = POINTER(TBYTE)
PTCHAR = POINTER(TCHAR)
PTSTR = LPWSTR
UCHAR = UINT
UHALF_PTR = UINT
PUCHAR = POINTER(UCHAR)
PUHALF_PTR = POINTER(UHALF_PTR)
PUINT = POINTER(UINT)
PUINT_PTR = POINTER(UINT_PTR)
PUINT8 = POINTER(UINT8)
PUINT16 = POINTER(UINT16)
PUINT32 = POINTER(UINT32)
PUINT64 = POINTER(UINT64)
PULONG = POINTER(ULONG)
PULONGLONG = POINTER(ULONGLONG)
PULONG_PTR = POINTER(ULONG_PTR)
ULONG32 = UINT
ULONG64 = UINT64
PULONG32 = POINTER(ULONG32)
PULONG64 = POINTER(ULONG64)
PUSHORT = POINTER(USHORT)
PVOID = LPVOID
PWCHAR = POINTER(WCHAR)
PWORD = POINTER(WORD)
PWSTR = POINTER(WCHAR)
QWORD = UINT64
SC_HANDLE = HANDLE
SC_LOCK = LPVOID
SERVICE_STATUS_HANDLE = HANDLE


class _UNICODE_STRING(Structure):
    _fields_ = [
        ('Length', USHORT),
        ('MaximumLength', USHORT),
        ('Buffer', PWSTR)
    ]


UNICODE_STRING = _UNICODE_STRING
PUNICODE_STRING = POINTER(UNICODE_STRING)
PCUNICODE_STRING = POINTER(UNICODE_STRING)
USN = LONGLONG
VOID = None
WINAPI = WINFUNCTYPE
WPARAM = UINT_PTR
NULL = None
