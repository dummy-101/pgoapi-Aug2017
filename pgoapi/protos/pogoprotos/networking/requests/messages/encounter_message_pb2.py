# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/encounter_message.proto

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
    name='pogoprotos/networking/requests/messages/encounter_message.proto',
    package='pogoprotos.networking.requests.messages',
    syntax='proto3',
    serialized_pb=_b(
        '\n?pogoprotos/networking/requests/messages/encounter_message.proto\x12\'pogoprotos.networking.requests.messages\"s\n\x10\x45ncounterMessage\x12\x14\n\x0c\x65ncounter_id\x18\x01 \x01(\x06\x12\x16\n\x0espawn_point_id\x18\x02 \x01(\t\x12\x17\n\x0fplayer_latitude\x18\x03 \x01(\x01\x12\x18\n\x10player_longitude\x18\x04 \x01(\x01\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ENCOUNTERMESSAGE = _descriptor.Descriptor(
    name='EncounterMessage',
    full_name='pogoprotos.networking.requests.messages.EncounterMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='encounter_id',
            full_name=
            'pogoprotos.networking.requests.messages.EncounterMessage.encounter_id',
            index=0,
            number=1,
            type=6,
            cpp_type=4,
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
            name='spawn_point_id',
            full_name=
            'pogoprotos.networking.requests.messages.EncounterMessage.spawn_point_id',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='player_latitude',
            full_name=
            'pogoprotos.networking.requests.messages.EncounterMessage.player_latitude',
            index=2,
            number=3,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='player_longitude',
            full_name=
            'pogoprotos.networking.requests.messages.EncounterMessage.player_longitude',
            index=3,
            number=4,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    serialized_start=108,
    serialized_end=223, )

DESCRIPTOR.message_types_by_name['EncounterMessage'] = _ENCOUNTERMESSAGE

EncounterMessage = _reflection.GeneratedProtocolMessageType(
    'EncounterMessage',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_ENCOUNTERMESSAGE,
        __module__=
        'pogoprotos.networking.requests.messages.encounter_message_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.EncounterMessage)
    ))
_sym_db.RegisterMessage(EncounterMessage)

# @@protoc_insertion_point(module_scope)
