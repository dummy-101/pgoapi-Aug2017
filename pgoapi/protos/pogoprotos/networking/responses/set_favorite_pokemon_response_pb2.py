# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/set_favorite_pokemon_response.proto

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
    name='pogoprotos/networking/responses/set_favorite_pokemon_response.proto',
    package='pogoprotos.networking.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\nCpogoprotos/networking/responses/set_favorite_pokemon_response.proto\x12\x1fpogoprotos.networking.responses\"\xc9\x01\n\x1aSetFavoritePokemonResponse\x12R\n\x06result\x18\x01 \x01(\x0e\x32\x42.pogoprotos.networking.responses.SetFavoritePokemonResponse.Result\"W\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1b\n\x17\x45RROR_POKEMON_NOT_FOUND\x10\x02\x12\x18\n\x14\x45RROR_POKEMON_IS_EGG\x10\x03\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SETFAVORITEPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
    name='Result',
    full_name=
    'pogoprotos.networking.responses.SetFavoritePokemonResponse.Result',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='SUCCESS', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_POKEMON_NOT_FOUND',
            index=2,
            number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_POKEMON_IS_EGG',
            index=3,
            number=3,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=219,
    serialized_end=306, )
_sym_db.RegisterEnumDescriptor(_SETFAVORITEPOKEMONRESPONSE_RESULT)

_SETFAVORITEPOKEMONRESPONSE = _descriptor.Descriptor(
    name='SetFavoritePokemonResponse',
    full_name='pogoprotos.networking.responses.SetFavoritePokemonResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='result',
            full_name=
            'pogoprotos.networking.responses.SetFavoritePokemonResponse.result',
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _SETFAVORITEPOKEMONRESPONSE_RESULT,
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=105,
    serialized_end=306, )

_SETFAVORITEPOKEMONRESPONSE.fields_by_name[
    'result'].enum_type = _SETFAVORITEPOKEMONRESPONSE_RESULT
_SETFAVORITEPOKEMONRESPONSE_RESULT.containing_type = _SETFAVORITEPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name[
    'SetFavoritePokemonResponse'] = _SETFAVORITEPOKEMONRESPONSE

SetFavoritePokemonResponse = _reflection.GeneratedProtocolMessageType(
    'SetFavoritePokemonResponse',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_SETFAVORITEPOKEMONRESPONSE,
        __module__=
        'pogoprotos.networking.responses.set_favorite_pokemon_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SetFavoritePokemonResponse)
    ))
_sym_db.RegisterMessage(SetFavoritePokemonResponse)

# @@protoc_insertion_point(module_scope)
