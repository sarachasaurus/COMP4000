# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='users.proto',
  package='users',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0busers.proto\x12\x05users\"M\n\x11\x43reateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x14\n\x0c\x63onfirmation\x18\x03 \x01(\t\"\"\n\x0f\x43reateUserReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"6\n\x10LoginUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"0\n\x0eLoginUserReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05token\x18\x02 \x01(\t\"4\n\x11\x44\x65leteUserRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"\"\n\x0f\x44\x65leteUserReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"8\n\x15UpdatePasswordRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"&\n\x13UpdatePasswordReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xdf\x01\n\x05Users\x12G\n\x11\x43reateUserAccount\x12\x18.users.CreateUserRequest\x1a\x16.users.CreateUserReply\"\x00\x12\x44\n\x10LoginUserAccount\x12\x17.users.LoginUserRequest\x1a\x15.users.LoginUserReply\"\x00\x12G\n\x11\x44\x65leteUserAccount\x12\x18.users.DeleteUserRequest\x1a\x16.users.DeleteUserReply\"\x00\x62\x06proto3'
)




_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='users.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='users.CreateUserRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='users.CreateUserRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confirmation', full_name='users.CreateUserRequest.confirmation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=99,
)


_CREATEUSERREPLY = _descriptor.Descriptor(
  name='CreateUserReply',
  full_name='users.CreateUserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='users.CreateUserReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=135,
)


_LOGINUSERREQUEST = _descriptor.Descriptor(
  name='LoginUserRequest',
  full_name='users.LoginUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='users.LoginUserRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='users.LoginUserRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=191,
)


_LOGINUSERREPLY = _descriptor.Descriptor(
  name='LoginUserReply',
  full_name='users.LoginUserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='users.LoginUserReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='users.LoginUserReply.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=241,
)


_DELETEUSERREQUEST = _descriptor.Descriptor(
  name='DeleteUserRequest',
  full_name='users.DeleteUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='users.DeleteUserRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='users.DeleteUserRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=295,
)


_DELETEUSERREPLY = _descriptor.Descriptor(
  name='DeleteUserReply',
  full_name='users.DeleteUserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='users.DeleteUserReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=331,
)


_UPDATEPASSWORDREQUEST = _descriptor.Descriptor(
  name='UpdatePasswordRequest',
  full_name='users.UpdatePasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='users.UpdatePasswordRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='users.UpdatePasswordRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=389,
)


_UPDATEPASSWORDREPLY = _descriptor.Descriptor(
  name='UpdatePasswordReply',
  full_name='users.UpdatePasswordReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='users.UpdatePasswordReply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=429,
)

DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserReply'] = _CREATEUSERREPLY
DESCRIPTOR.message_types_by_name['LoginUserRequest'] = _LOGINUSERREQUEST
DESCRIPTOR.message_types_by_name['LoginUserReply'] = _LOGINUSERREPLY
DESCRIPTOR.message_types_by_name['DeleteUserRequest'] = _DELETEUSERREQUEST
DESCRIPTOR.message_types_by_name['DeleteUserReply'] = _DELETEUSERREPLY
DESCRIPTOR.message_types_by_name['UpdatePasswordRequest'] = _UPDATEPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['UpdatePasswordReply'] = _UPDATEPASSWORDREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserReply = _reflection.GeneratedProtocolMessageType('CreateUserReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREPLY,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.CreateUserReply)
  })
_sym_db.RegisterMessage(CreateUserReply)

LoginUserRequest = _reflection.GeneratedProtocolMessageType('LoginUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.LoginUserRequest)
  })
_sym_db.RegisterMessage(LoginUserRequest)

LoginUserReply = _reflection.GeneratedProtocolMessageType('LoginUserReply', (_message.Message,), {
  'DESCRIPTOR' : _LOGINUSERREPLY,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.LoginUserReply)
  })
_sym_db.RegisterMessage(LoginUserReply)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.DeleteUserRequest)
  })
_sym_db.RegisterMessage(DeleteUserRequest)

DeleteUserReply = _reflection.GeneratedProtocolMessageType('DeleteUserReply', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREPLY,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.DeleteUserReply)
  })
_sym_db.RegisterMessage(DeleteUserReply)

UpdatePasswordRequest = _reflection.GeneratedProtocolMessageType('UpdatePasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPASSWORDREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.UpdatePasswordRequest)
  })
_sym_db.RegisterMessage(UpdatePasswordRequest)

UpdatePasswordReply = _reflection.GeneratedProtocolMessageType('UpdatePasswordReply', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPASSWORDREPLY,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.UpdatePasswordReply)
  })
_sym_db.RegisterMessage(UpdatePasswordReply)



_USERS = _descriptor.ServiceDescriptor(
  name='Users',
  full_name='users.Users',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=432,
  serialized_end=655,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUserAccount',
    full_name='users.Users.CreateUserAccount',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_CREATEUSERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='LoginUserAccount',
    full_name='users.Users.LoginUserAccount',
    index=1,
    containing_service=None,
    input_type=_LOGINUSERREQUEST,
    output_type=_LOGINUSERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteUserAccount',
    full_name='users.Users.DeleteUserAccount',
    index=2,
    containing_service=None,
    input_type=_DELETEUSERREQUEST,
    output_type=_DELETEUSERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERS)

DESCRIPTOR.services_by_name['Users'] = _USERS

# @@protoc_insertion_point(module_scope)
