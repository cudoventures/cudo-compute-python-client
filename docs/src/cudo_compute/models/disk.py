# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from src.cudo_compute.configuration import Configuration


class Disk(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'create_time': 'datetime',
        'data_center_id': 'str',
        'disk_state': 'DiskState',
        'disk_type': 'DiskType',
        'id': 'str',
        'private_image_id': 'str',
        'project_id': 'str',
        'public_image_id': 'str',
        'size_gib': 'int',
        'storage_class': 'DiskStorageClass',
        'vm_id': 'str'
    }

    attribute_map = {
        'create_time': 'createTime',
        'data_center_id': 'dataCenterId',
        'disk_state': 'diskState',
        'disk_type': 'diskType',
        'id': 'id',
        'private_image_id': 'privateImageId',
        'project_id': 'projectId',
        'public_image_id': 'publicImageId',
        'size_gib': 'sizeGib',
        'storage_class': 'storageClass',
        'vm_id': 'vmId'
    }

    def __init__(self, create_time=None, data_center_id=None, disk_state=None, disk_type=None, id=None, private_image_id=None, project_id=None, public_image_id=None, size_gib=None, storage_class=None, vm_id=None, _configuration=None):  # noqa: E501
        """Disk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._data_center_id = None
        self._disk_state = None
        self._disk_type = None
        self._id = None
        self._private_image_id = None
        self._project_id = None
        self._public_image_id = None
        self._size_gib = None
        self._storage_class = None
        self._vm_id = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if data_center_id is not None:
            self.data_center_id = data_center_id
        if disk_state is not None:
            self.disk_state = disk_state
        if disk_type is not None:
            self.disk_type = disk_type
        if id is not None:
            self.id = id
        if private_image_id is not None:
            self.private_image_id = private_image_id
        if project_id is not None:
            self.project_id = project_id
        if public_image_id is not None:
            self.public_image_id = public_image_id
        self.size_gib = size_gib
        if storage_class is not None:
            self.storage_class = storage_class
        if vm_id is not None:
            self.vm_id = vm_id

    @property
    def create_time(self):
        """Gets the create_time of this Disk.  # noqa: E501


        :return: The create_time of this Disk.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Disk.


        :param create_time: The create_time of this Disk.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def data_center_id(self):
        """Gets the data_center_id of this Disk.  # noqa: E501


        :return: The data_center_id of this Disk.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this Disk.


        :param data_center_id: The data_center_id of this Disk.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def disk_state(self):
        """Gets the disk_state of this Disk.  # noqa: E501


        :return: The disk_state of this Disk.  # noqa: E501
        :rtype: DiskState
        """
        return self._disk_state

    @disk_state.setter
    def disk_state(self, disk_state):
        """Sets the disk_state of this Disk.


        :param disk_state: The disk_state of this Disk.  # noqa: E501
        :type: DiskState
        """

        self._disk_state = disk_state

    @property
    def disk_type(self):
        """Gets the disk_type of this Disk.  # noqa: E501


        :return: The disk_type of this Disk.  # noqa: E501
        :rtype: DiskType
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this Disk.


        :param disk_type: The disk_type of this Disk.  # noqa: E501
        :type: DiskType
        """

        self._disk_type = disk_type

    @property
    def id(self):
        """Gets the id of this Disk.  # noqa: E501


        :return: The id of this Disk.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Disk.


        :param id: The id of this Disk.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def private_image_id(self):
        """Gets the private_image_id of this Disk.  # noqa: E501


        :return: The private_image_id of this Disk.  # noqa: E501
        :rtype: str
        """
        return self._private_image_id

    @private_image_id.setter
    def private_image_id(self, private_image_id):
        """Sets the private_image_id of this Disk.


        :param private_image_id: The private_image_id of this Disk.  # noqa: E501
        :type: str
        """

        self._private_image_id = private_image_id

    @property
    def project_id(self):
        """Gets the project_id of this Disk.  # noqa: E501


        :return: The project_id of this Disk.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Disk.


        :param project_id: The project_id of this Disk.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def public_image_id(self):
        """Gets the public_image_id of this Disk.  # noqa: E501


        :return: The public_image_id of this Disk.  # noqa: E501
        :rtype: str
        """
        return self._public_image_id

    @public_image_id.setter
    def public_image_id(self, public_image_id):
        """Sets the public_image_id of this Disk.


        :param public_image_id: The public_image_id of this Disk.  # noqa: E501
        :type: str
        """

        self._public_image_id = public_image_id

    @property
    def size_gib(self):
        """Gets the size_gib of this Disk.  # noqa: E501


        :return: The size_gib of this Disk.  # noqa: E501
        :rtype: int
        """
        return self._size_gib

    @size_gib.setter
    def size_gib(self, size_gib):
        """Sets the size_gib of this Disk.


        :param size_gib: The size_gib of this Disk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and size_gib is None:
            raise ValueError("Invalid value for `size_gib`, must not be `None`")  # noqa: E501

        self._size_gib = size_gib

    @property
    def storage_class(self):
        """Gets the storage_class of this Disk.  # noqa: E501


        :return: The storage_class of this Disk.  # noqa: E501
        :rtype: DiskStorageClass
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this Disk.


        :param storage_class: The storage_class of this Disk.  # noqa: E501
        :type: DiskStorageClass
        """

        self._storage_class = storage_class

    @property
    def vm_id(self):
        """Gets the vm_id of this Disk.  # noqa: E501


        :return: The vm_id of this Disk.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this Disk.


        :param vm_id: The vm_id of this Disk.  # noqa: E501
        :type: str
        """

        self._vm_id = vm_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Disk, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Disk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Disk):
            return True

        return self.to_dict() != other.to_dict()
