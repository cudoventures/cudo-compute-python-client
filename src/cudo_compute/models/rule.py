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


class Rule(object):
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
        'icmp_type': 'str',
        'id': 'str',
        'ip_range_cidr': 'str',
        'ports': 'str',
        'protocol': 'Protocol',
        'rule_type': 'RuleType'
    }

    attribute_map = {
        'icmp_type': 'icmpType',
        'id': 'id',
        'ip_range_cidr': 'ipRangeCidr',
        'ports': 'ports',
        'protocol': 'protocol',
        'rule_type': 'ruleType'
    }

    def __init__(self, icmp_type=None, id=None, ip_range_cidr=None, ports=None, protocol=None, rule_type=None, _configuration=None):  # noqa: E501
        """Rule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._icmp_type = None
        self._id = None
        self._ip_range_cidr = None
        self._ports = None
        self._protocol = None
        self._rule_type = None
        self.discriminator = None

        if icmp_type is not None:
            self.icmp_type = icmp_type
        if id is not None:
            self.id = id
        if ip_range_cidr is not None:
            self.ip_range_cidr = ip_range_cidr
        if ports is not None:
            self.ports = ports
        if protocol is not None:
            self.protocol = protocol
        if rule_type is not None:
            self.rule_type = rule_type

    @property
    def icmp_type(self):
        """Gets the icmp_type of this Rule.  # noqa: E501


        :return: The icmp_type of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._icmp_type

    @icmp_type.setter
    def icmp_type(self, icmp_type):
        """Sets the icmp_type of this Rule.


        :param icmp_type: The icmp_type of this Rule.  # noqa: E501
        :type: str
        """

        self._icmp_type = icmp_type

    @property
    def id(self):
        """Gets the id of this Rule.  # noqa: E501


        :return: The id of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rule.


        :param id: The id of this Rule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ip_range_cidr(self):
        """Gets the ip_range_cidr of this Rule.  # noqa: E501


        :return: The ip_range_cidr of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._ip_range_cidr

    @ip_range_cidr.setter
    def ip_range_cidr(self, ip_range_cidr):
        """Sets the ip_range_cidr of this Rule.


        :param ip_range_cidr: The ip_range_cidr of this Rule.  # noqa: E501
        :type: str
        """

        self._ip_range_cidr = ip_range_cidr

    @property
    def ports(self):
        """Gets the ports of this Rule.  # noqa: E501


        :return: The ports of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Rule.


        :param ports: The ports of this Rule.  # noqa: E501
        :type: str
        """

        self._ports = ports

    @property
    def protocol(self):
        """Gets the protocol of this Rule.  # noqa: E501


        :return: The protocol of this Rule.  # noqa: E501
        :rtype: Protocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Rule.


        :param protocol: The protocol of this Rule.  # noqa: E501
        :type: Protocol
        """

        self._protocol = protocol

    @property
    def rule_type(self):
        """Gets the rule_type of this Rule.  # noqa: E501


        :return: The rule_type of this Rule.  # noqa: E501
        :rtype: RuleType
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this Rule.


        :param rule_type: The rule_type of this Rule.  # noqa: E501
        :type: RuleType
        """

        self._rule_type = rule_type

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
        if issubclass(Rule, dict):
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
        if not isinstance(other, Rule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rule):
            return True

        return self.to_dict() != other.to_dict()
