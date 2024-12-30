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


class NetworkResult(object):
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
        'project_id': 'str',
        'id': 'str',
        'data_center_id': 'str',
        'ip_range': 'str',
        'gateway': 'str',
        'internal_ip_address': 'str',
        'external_ip_address': 'str',
        'state': 'NetworkState',
        'create_time': 'datetime'
    }

    attribute_map = {
        'project_id': 'projectId',
        'id': 'id',
        'data_center_id': 'dataCenterId',
        'ip_range': 'ipRange',
        'gateway': 'gateway',
        'internal_ip_address': 'internalIpAddress',
        'external_ip_address': 'externalIpAddress',
        'state': 'state',
        'create_time': 'createTime'
    }

    def __init__(self, project_id=None, id=None, data_center_id=None, ip_range=None, gateway=None, internal_ip_address=None, external_ip_address=None, state=None, create_time=None, _configuration=None):  # noqa: E501
        """NetworkResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project_id = None
        self._id = None
        self._data_center_id = None
        self._ip_range = None
        self._gateway = None
        self._internal_ip_address = None
        self._external_ip_address = None
        self._state = None
        self._create_time = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if id is not None:
            self.id = id
        if data_center_id is not None:
            self.data_center_id = data_center_id
        if ip_range is not None:
            self.ip_range = ip_range
        if gateway is not None:
            self.gateway = gateway
        if internal_ip_address is not None:
            self.internal_ip_address = internal_ip_address
        if external_ip_address is not None:
            self.external_ip_address = external_ip_address
        if state is not None:
            self.state = state
        if create_time is not None:
            self.create_time = create_time

    @property
    def project_id(self):
        """Gets the project_id of this NetworkResult.  # noqa: E501


        :return: The project_id of this NetworkResult.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NetworkResult.


        :param project_id: The project_id of this NetworkResult.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def id(self):
        """Gets the id of this NetworkResult.  # noqa: E501


        :return: The id of this NetworkResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkResult.


        :param id: The id of this NetworkResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def data_center_id(self):
        """Gets the data_center_id of this NetworkResult.  # noqa: E501


        :return: The data_center_id of this NetworkResult.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this NetworkResult.


        :param data_center_id: The data_center_id of this NetworkResult.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def ip_range(self):
        """Gets the ip_range of this NetworkResult.  # noqa: E501


        :return: The ip_range of this NetworkResult.  # noqa: E501
        :rtype: str
        """
        return self._ip_range

    @ip_range.setter
    def ip_range(self, ip_range):
        """Sets the ip_range of this NetworkResult.


        :param ip_range: The ip_range of this NetworkResult.  # noqa: E501
        :type: str
        """

        self._ip_range = ip_range

    @property
    def gateway(self):
        """Gets the gateway of this NetworkResult.  # noqa: E501


        :return: The gateway of this NetworkResult.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this NetworkResult.


        :param gateway: The gateway of this NetworkResult.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def internal_ip_address(self):
        """Gets the internal_ip_address of this NetworkResult.  # noqa: E501


        :return: The internal_ip_address of this NetworkResult.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip_address

    @internal_ip_address.setter
    def internal_ip_address(self, internal_ip_address):
        """Sets the internal_ip_address of this NetworkResult.


        :param internal_ip_address: The internal_ip_address of this NetworkResult.  # noqa: E501
        :type: str
        """

        self._internal_ip_address = internal_ip_address

    @property
    def external_ip_address(self):
        """Gets the external_ip_address of this NetworkResult.  # noqa: E501


        :return: The external_ip_address of this NetworkResult.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_address

    @external_ip_address.setter
    def external_ip_address(self, external_ip_address):
        """Sets the external_ip_address of this NetworkResult.


        :param external_ip_address: The external_ip_address of this NetworkResult.  # noqa: E501
        :type: str
        """

        self._external_ip_address = external_ip_address

    @property
    def state(self):
        """Gets the state of this NetworkResult.  # noqa: E501


        :return: The state of this NetworkResult.  # noqa: E501
        :rtype: NetworkState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NetworkResult.


        :param state: The state of this NetworkResult.  # noqa: E501
        :type: NetworkState
        """

        self._state = state

    @property
    def create_time(self):
        """Gets the create_time of this NetworkResult.  # noqa: E501


        :return: The create_time of this NetworkResult.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this NetworkResult.


        :param create_time: The create_time of this NetworkResult.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

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
        if issubclass(NetworkResult, dict):
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
        if not isinstance(other, NetworkResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkResult):
            return True

        return self.to_dict() != other.to_dict()