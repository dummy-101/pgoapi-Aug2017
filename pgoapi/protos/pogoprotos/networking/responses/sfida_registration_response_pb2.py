# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/sfida_registration_response.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (
    lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/networking/responses/sfida_registration_response.proto',
    package='pogoprotos.networking.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\nApogoprotos/networking/responses/sfida_registration_response.proto\x12\x1fpogoprotos.networking.responses\"1\n\x19SfidaRegistrationResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\x0c\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SFIDAREGISTRATIONRESPONSE = _descriptor.Descriptor(
    name='SfidaRegistrationResponse',
    full_name='pogoprotos.networking.responses.SfidaRegistrationResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='access_token',
            full_name=
            'pogoprotos.networking.responses.SfidaRegistrationResponse.access_token',
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=102,
    serialized_end=151, )

DESCRIPTOR.message_types_by_name[
    'SfidaRegistrationResponse'] = _SFIDAREGISTRATIONRESPONSE

SfidaRegistrationResponse = _reflection.GeneratedProtocolMessageType(
    'SfidaRegistrationResponse',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_SFIDAREGISTRATIONRESPONSE,
        __module__=
        'pogoprotos.networking.responses.sfida_registration_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SfidaRegistrationResponse)
    ))
_sym_db.RegisterMessage(SfidaRegistrationResponse)

# @@protoc_insertion_point(module_scope)
