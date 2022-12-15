# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookstore.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0f\x62ookstore.proto"`\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x15\n\x05genre\x18\x04 \x01(\x0e\x32\x06.Genre\x12\x14\n\x0cpublish_year\x18\x05 \x01(\x05"g\n\rInventoryItem\x12\x18\n\x10inventory_number\x18\x01 \x01(\x05\x12\x15\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x05.BookH\x00\x12\x17\n\x06status\x18\x03 \x01(\x0e\x32\x07.StatusB\x0c\n\nbook_oneof"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04ISBN\x18\x01 \x01(\t"m\n\x11\x43reateBookRequest\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x15\n\x05genre\x18\x04 \x01(\x0e\x32\x06.Genre\x12\x14\n\x0cpublish_year\x18\x05 \x01(\x05"3\n\x12\x43reateBookResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04ISBN\x18\x02 \x01(\t*,\n\x05Genre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\t\n\x05NOVEL\x10\x01\x12\x0b\n\x07\x46\x41NTACY\x10\x02*"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x32p\n\x10InventoryService\x12#\n\x07GetBook\x12\x0f.GetBookRequest\x1a\x05.Book"\x00\x12\x37\n\nCreateBook\x12\x12.CreateBookRequest\x1a\x13.CreateBookResponse"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "bookstore_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _GENRE._serialized_start = 418
    _GENRE._serialized_end = 462
    _STATUS._serialized_start = 464
    _STATUS._serialized_end = 498
    _BOOK._serialized_start = 19
    _BOOK._serialized_end = 115
    _INVENTORYITEM._serialized_start = 117
    _INVENTORYITEM._serialized_end = 220
    _GETBOOKREQUEST._serialized_start = 222
    _GETBOOKREQUEST._serialized_end = 252
    _CREATEBOOKREQUEST._serialized_start = 254
    _CREATEBOOKREQUEST._serialized_end = 363
    _CREATEBOOKRESPONSE._serialized_start = 365
    _CREATEBOOKRESPONSE._serialized_end = 416
    _INVENTORYSERVICE._serialized_start = 500
    _INVENTORYSERVICE._serialized_end = 612
# @@protoc_insertion_point(module_scope)
