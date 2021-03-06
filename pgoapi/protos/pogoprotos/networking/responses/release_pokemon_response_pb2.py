# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/release_pokemon_response.proto

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
    name='pogoprotos/networking/responses/release_pokemon_response.proto',
    package='pogoprotos.networking.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\n>pogoprotos/networking/responses/release_pokemon_response.proto\x12\x1fpogoprotos.networking.responses\"\xf9\x01\n\x16ReleasePokemonResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.ReleasePokemonResponse.Result\x12\x15\n\rcandy_awarded\x18\x02 \x01(\x05\"x\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x14\n\x10POKEMON_DEPLOYED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\x18\n\x14\x45RROR_POKEMON_IS_EGG\x10\x04\x12\x1a\n\x16\x45RROR_POKEMON_IS_BUDDY\x10\x05\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_RELEASEPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
    name='Result',
    full_name='pogoprotos.networking.responses.ReleasePokemonResponse.Result',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='SUCCESS', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='POKEMON_DEPLOYED',
            index=2,
            number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='FAILED', index=3, number=3, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_POKEMON_IS_EGG',
            index=4,
            number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_POKEMON_IS_BUDDY',
            index=5,
            number=5,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=229,
    serialized_end=349, )
_sym_db.RegisterEnumDescriptor(_RELEASEPOKEMONRESPONSE_RESULT)

_RELEASEPOKEMONRESPONSE = _descriptor.Descriptor(
    name='ReleasePokemonResponse',
    full_name='pogoprotos.networking.responses.ReleasePokemonResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='result',
            full_name=
            'pogoprotos.networking.responses.ReleasePokemonResponse.result',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='candy_awarded',
            full_name=
            'pogoprotos.networking.responses.ReleasePokemonResponse.candy_awarded',
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _RELEASEPOKEMONRESPONSE_RESULT,
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=100,
    serialized_end=349, )

_RELEASEPOKEMONRESPONSE.fields_by_name[
    'result'].enum_type = _RELEASEPOKEMONRESPONSE_RESULT
_RELEASEPOKEMONRESPONSE_RESULT.containing_type = _RELEASEPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name[
    'ReleasePokemonResponse'] = _RELEASEPOKEMONRESPONSE

ReleasePokemonResponse = _reflection.GeneratedProtocolMessageType(
    'ReleasePokemonResponse',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_RELEASEPOKEMONRESPONSE,
        __module__=
        'pogoprotos.networking.responses.release_pokemon_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.ReleasePokemonResponse)
    ))
_sym_db.RegisterMessage(ReleasePokemonResponse)

# @@protoc_insertion_point(module_scope)
