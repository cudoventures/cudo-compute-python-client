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


class VMNIC(object):
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
        'network_id': 'str',
        'external_ip_address': 'str',
        'internal_ip_address': 'str',
        'network_address': 'str',
        'security_group_ids': 'list[str]'
    }

    attribute_map = {
        'network_id': 'networkId',
        'external_ip_address': 'externalIpAddress',
        'internal_ip_address': 'internalIpAddress',
        'network_address': 'networkAddress',
        'security_group_ids': 'securityGroupIds'
    }

    def __init__(self, network_id=None, external_ip_address=None, internal_ip_address=None, network_address=None, security_group_ids=None, _configuration=None):  # noqa: E501
        """VMNIC - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._network_id = None
        self._external_ip_address = None
        self._internal_ip_address = None
        self._network_address = None
        self._security_group_ids = None
        self.discriminator = None

        if network_id is not None:
            self.network_id = network_id
        if external_ip_address is not None:
            self.external_ip_address = external_ip_address
        if internal_ip_address is not None:
            self.internal_ip_address = internal_ip_address
        if network_address is not None:
            self.network_address = network_address
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids

    @property
    def network_id(self):
        """Gets the network_id of this VMNIC.  # noqa: E501


        :return: The network_id of this VMNIC.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this VMNIC.


        :param network_id: The network_id of this VMNIC.  # noqa: E501
        :type: str
        """

        self._network_id = network_id

    @property
    def external_ip_address(self):
        """Gets the external_ip_address of this VMNIC.  # noqa: E501


        :return: The external_ip_address of this VMNIC.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_address

    @external_ip_address.setter
    def external_ip_address(self, external_ip_address):
        """Sets the external_ip_address of this VMNIC.


        :param external_ip_address: The external_ip_address of this VMNIC.  # noqa: E501
        :type: str
        """

        self._external_ip_address = external_ip_address

    @property
    def internal_ip_address(self):
        """Gets the internal_ip_address of this VMNIC.  # noqa: E501


        :return: The internal_ip_address of this VMNIC.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip_address

    @internal_ip_address.setter
    def internal_ip_address(self, internal_ip_address):
        """Sets the internal_ip_address of this VMNIC.


        :param internal_ip_address: The internal_ip_address of this VMNIC.  # noqa: E501
        :type: str
        """

        self._internal_ip_address = internal_ip_address

    @property
    def network_address(self):
        """Gets the network_address of this VMNIC.  # noqa: E501


        :return: The network_address of this VMNIC.  # noqa: E501
        :rtype: str
        """
        return self._network_address

    @network_address.setter
    def network_address(self, network_address):
        """Sets the network_address of this VMNIC.


        :param network_address: The network_address of this VMNIC.  # noqa: E501
        :type: str
        """

        self._network_address = network_address

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this VMNIC.  # noqa: E501


        :return: The security_group_ids of this VMNIC.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this VMNIC.


        :param security_group_ids: The security_group_ids of this VMNIC.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

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
        if issubclass(VMNIC, dict):
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
        if not isinstance(other, VMNIC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VMNIC):
            return True

        return self.to_dict() != other.to_dict()
