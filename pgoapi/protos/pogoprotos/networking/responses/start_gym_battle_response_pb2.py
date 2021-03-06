# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/start_gym_battle_response.proto

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

from pogoprotos.data.battle import battle_log_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__log__pb2
from pogoprotos.data.battle import battle_participant_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2
from pogoprotos.data.battle import battle_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/networking/responses/start_gym_battle_response.proto',
    package='pogoprotos.networking.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\n?pogoprotos/networking/responses/start_gym_battle_response.proto\x12\x1fpogoprotos.networking.responses\x1a\'pogoprotos/data/battle/battle_log.proto\x1a/pogoprotos/data/battle/battle_participant.proto\x1a#pogoprotos/data/battle/battle.proto\"\xb8\x06\n\x16StartGymBattleResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.StartGymBattleResponse.Result\x12!\n\x19\x62\x61ttle_start_timestamp_ms\x18\x02 \x01(\x03\x12\x1f\n\x17\x62\x61ttle_end_timestamp_ms\x18\x03 \x01(\x03\x12\x11\n\tbattle_id\x18\x04 \x01(\t\x12;\n\x08\x64\x65\x66\x65nder\x18\x05 \x01(\x0b\x32).pogoprotos.data.battle.BattleParticipant\x12\x35\n\nbattle_log\x18\x06 \x01(\x0b\x32!.pogoprotos.data.battle.BattleLog\x12;\n\x08\x61ttacker\x18\x07 \x01(\x0b\x32).pogoprotos.data.battle.BattleParticipant\x12.\n\x06\x62\x61ttle\x18\x08 \x01(\x0b\x32\x1e.pogoprotos.data.battle.Battle\"\x95\x03\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x17\n\x13\x45RROR_GYM_NOT_FOUND\x10\x02\x12\x15\n\x11\x45RROR_GYM_NEUTRAL\x10\x03\x12\x18\n\x14\x45RROR_GYM_WRONG_TEAM\x10\x04\x12\x13\n\x0f\x45RROR_GYM_EMPTY\x10\x05\x12\x1a\n\x16\x45RROR_INVALID_DEFENDER\x10\x06\x12)\n%ERROR_TRAINING_INVALID_ATTACKER_COUNT\x10\x07\x12\x1d\n\x19\x45RROR_ALL_POKEMON_FAINTED\x10\x08\x12\x1a\n\x16\x45RROR_TOO_MANY_BATTLES\x10\t\x12\x1a\n\x16\x45RROR_TOO_MANY_PLAYERS\x10\n\x12\x1c\n\x18\x45RROR_GYM_BATTLE_LOCKOUT\x10\x0b\x12$\n ERROR_PLAYER_BELOW_MINIMUM_LEVEL\x10\x0c\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\r\x12\x1a\n\x16\x45RROR_POI_INACCESSIBLE\x10\x0e\x62\x06proto3'
    ),
    dependencies=[
        pogoprotos_dot_data_dot_battle_dot_battle__log__pb2.DESCRIPTOR,
        pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2.DESCRIPTOR,
        pogoprotos_dot_data_dot_battle_dot_battle__pb2.DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_STARTGYMBATTLERESPONSE_RESULT = _descriptor.EnumDescriptor(
    name='Result',
    full_name='pogoprotos.networking.responses.StartGymBattleResponse.Result',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='SUCCESS', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_GYM_NOT_FOUND',
            index=2,
            number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_GYM_NEUTRAL',
            index=3,
            number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_GYM_WRONG_TEAM',
            index=4,
            number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_GYM_EMPTY', index=5, number=5, options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_INVALID_DEFENDER',
            index=6,
            number=6,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_TRAINING_INVALID_ATTACKER_COUNT',
            index=7,
            number=7,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_ALL_POKEMON_FAINTED',
            index=8,
            number=8,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_TOO_MANY_BATTLES',
            index=9,
            number=9,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_TOO_MANY_PLAYERS',
            index=10,
            number=10,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_GYM_BATTLE_LOCKOUT',
            index=11,
            number=11,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_PLAYER_BELOW_MINIMUM_LEVEL',
            index=12,
            number=12,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_NOT_IN_RANGE',
            index=13,
            number=13,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_POI_INACCESSIBLE',
            index=14,
            number=14,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=647,
    serialized_end=1052, )
_sym_db.RegisterEnumDescriptor(_STARTGYMBATTLERESPONSE_RESULT)

_STARTGYMBATTLERESPONSE = _descriptor.Descriptor(
    name='StartGymBattleResponse',
    full_name='pogoprotos.networking.responses.StartGymBattleResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='result',
            full_name=
            'pogoprotos.networking.responses.StartGymBattleResponse.result',
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
            name='battle_start_timestamp_ms',
            full_name=
            'pogoprotos.networking.responses.StartGymBattleResponse.battle_start_timestamp_ms',
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
            name='battle_end_timestamp_ms',
            full_name=
            'pogoprotos.networking.responses.StartGymBattleResponse.battle_end_timestamp_ms',
            index=2,
            number=3,
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
            name='battle_id',
            full_name=
            'pogoprotos.networking.responses.StartGymBattleResponse.battle_id',
            index=3,
            number=4,
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
            name='defender',
            full_name=
            'pogoprotos.networking.responses.StartGymBattleResponse.defender',
            index=4,
            number=5,
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
        _descriptor.FieldDescriptor(
            name='battle_log',
            full_name=
            'pogoprotos.networking.responses.StartGymBattleResponse.battle_log',
            index=5,
            number=6,
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
        _descriptor.FieldDescriptor(
            name='attacker',
            full_name=
            'pogoprotos.networking.responses.StartGymBattleResponse.attacker',
            index=6,
            number=7,
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
        _descriptor.FieldDescriptor(
            name='battle',
            full_name=
            'pogoprotos.networking.responses.StartGymBattleResponse.battle',
            index=7,
            number=8,
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
    nested_types=[],
    enum_types=[
        _STARTGYMBATTLERESPONSE_RESULT,
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=228,
    serialized_end=1052, )

_STARTGYMBATTLERESPONSE.fields_by_name[
    'result'].enum_type = _STARTGYMBATTLERESPONSE_RESULT
_STARTGYMBATTLERESPONSE.fields_by_name[
    'defender'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2._BATTLEPARTICIPANT
_STARTGYMBATTLERESPONSE.fields_by_name[
    'battle_log'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__log__pb2._BATTLELOG
_STARTGYMBATTLERESPONSE.fields_by_name[
    'attacker'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2._BATTLEPARTICIPANT
_STARTGYMBATTLERESPONSE.fields_by_name[
    'battle'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pb2._BATTLE
_STARTGYMBATTLERESPONSE_RESULT.containing_type = _STARTGYMBATTLERESPONSE
DESCRIPTOR.message_types_by_name[
    'StartGymBattleResponse'] = _STARTGYMBATTLERESPONSE

StartGymBattleResponse = _reflection.GeneratedProtocolMessageType(
    'StartGymBattleResponse',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_STARTGYMBATTLERESPONSE,
        __module__=
        'pogoprotos.networking.responses.start_gym_battle_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartGymBattleResponse)
    ))
_sym_db.RegisterMessage(StartGymBattleResponse)

# @@protoc_insertion_point(module_scope)
