# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_player_profile_response.proto

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

from pogoprotos.data import player_badge_pb2 as pogoprotos_dot_data_dot_player__badge__pb2
from pogoprotos.data.badge import awarded_gym_badge_pb2 as pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/networking/responses/get_player_profile_response.proto',
    package='pogoprotos.networking.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\nApogoprotos/networking/responses/get_player_profile_response.proto\x12\x1fpogoprotos.networking.responses\x1a\"pogoprotos/data/player_badge.proto\x1a-pogoprotos/data/badge/awarded_gym_badge.proto\"\x80\x03\n\x18GetPlayerProfileResponse\x12P\n\x06result\x18\x01 \x01(\x0e\x32@.pogoprotos.networking.responses.GetPlayerProfileResponse.Result\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12,\n\x06\x62\x61\x64ges\x18\x03 \x03(\x0b\x32\x1c.pogoprotos.data.PlayerBadge\x12W\n\ngym_badges\x18\x04 \x01(\x0b\x32\x43.pogoprotos.networking.responses.GetPlayerProfileResponse.GymBadges\x1aU\n\tGymBadges\x12\x39\n\tgym_badge\x18\x01 \x03(\x0b\x32&.pogoprotos.data.badge.AwardedGymBadge\x12\r\n\x05total\x18\x02 \x01(\x05\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3'
    ),
    dependencies=[
        pogoprotos_dot_data_dot_player__badge__pb2.DESCRIPTOR,
        pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2.DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GETPLAYERPROFILERESPONSE_RESULT = _descriptor.EnumDescriptor(
    name='Result',
    full_name='pogoprotos.networking.responses.GetPlayerProfileResponse.Result',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='SUCCESS', index=1, number=1, options=None, type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=538,
    serialized_end=570, )
_sym_db.RegisterEnumDescriptor(_GETPLAYERPROFILERESPONSE_RESULT)

_GETPLAYERPROFILERESPONSE_GYMBADGES = _descriptor.Descriptor(
    name='GymBadges',
    full_name=
    'pogoprotos.networking.responses.GetPlayerProfileResponse.GymBadges',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='gym_badge',
            full_name=
            'pogoprotos.networking.responses.GetPlayerProfileResponse.GymBadges.gym_badge',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='total',
            full_name=
            'pogoprotos.networking.responses.GetPlayerProfileResponse.GymBadges.total',
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
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=451,
    serialized_end=536, )

_GETPLAYERPROFILERESPONSE = _descriptor.Descriptor(
    name='GetPlayerProfileResponse',
    full_name='pogoprotos.networking.responses.GetPlayerProfileResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='result',
            full_name=
            'pogoprotos.networking.responses.GetPlayerProfileResponse.result',
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
            name='start_time',
            full_name=
            'pogoprotos.networking.responses.GetPlayerProfileResponse.start_time',
            index=1,
            number=2,
            type=3,
            cpp_type=2,
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
            name='badges',
            full_name=
            'pogoprotos.networking.responses.GetPlayerProfileResponse.badges',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='gym_badges',
            full_name=
            'pogoprotos.networking.responses.GetPlayerProfileResponse.gym_badges',
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[
        _GETPLAYERPROFILERESPONSE_GYMBADGES,
    ],
    enum_types=[
        _GETPLAYERPROFILERESPONSE_RESULT,
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=186,
    serialized_end=570, )

_GETPLAYERPROFILERESPONSE_GYMBADGES.fields_by_name[
    'gym_badge'].message_type = pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2._AWARDEDGYMBADGE
_GETPLAYERPROFILERESPONSE_GYMBADGES.containing_type = _GETPLAYERPROFILERESPONSE
_GETPLAYERPROFILERESPONSE.fields_by_name[
    'result'].enum_type = _GETPLAYERPROFILERESPONSE_RESULT
_GETPLAYERPROFILERESPONSE.fields_by_name[
    'badges'].message_type = pogoprotos_dot_data_dot_player__badge__pb2._PLAYERBADGE
_GETPLAYERPROFILERESPONSE.fields_by_name[
    'gym_badges'].message_type = _GETPLAYERPROFILERESPONSE_GYMBADGES
_GETPLAYERPROFILERESPONSE_RESULT.containing_type = _GETPLAYERPROFILERESPONSE
DESCRIPTOR.message_types_by_name[
    'GetPlayerProfileResponse'] = _GETPLAYERPROFILERESPONSE

GetPlayerProfileResponse = _reflection.GeneratedProtocolMessageType(
    'GetPlayerProfileResponse',
    (_message.Message, ),
    dict(
        GymBadges=_reflection.GeneratedProtocolMessageType(
            'GymBadges',
            (_message.Message, ),
            dict(
                DESCRIPTOR=_GETPLAYERPROFILERESPONSE_GYMBADGES,
                __module__=
                'pogoprotos.networking.responses.get_player_profile_response_pb2'
                # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetPlayerProfileResponse.GymBadges)
            )),
        DESCRIPTOR=_GETPLAYERPROFILERESPONSE,
        __module__=
        'pogoprotos.networking.responses.get_player_profile_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetPlayerProfileResponse)
    ))
_sym_db.RegisterMessage(GetPlayerProfileResponse)
_sym_db.RegisterMessage(GetPlayerProfileResponse.GymBadges)

# @@protoc_insertion_point(module_scope)
