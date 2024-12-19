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


class CpuTopology(object):
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
        'sockets': 'int',
        'cores': 'int',
        'threads': 'int'
    }

    attribute_map = {
        'sockets': 'sockets',
        'cores': 'cores',
        'threads': 'threads'
    }

    def __init__(self, sockets=None, cores=None, threads=None, _configuration=None):  # noqa: E501
        """CpuTopology - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sockets = None
        self._cores = None
        self._threads = None
        self.discriminator = None

        if sockets is not None:
            self.sockets = sockets
        if cores is not None:
            self.cores = cores
        if threads is not None:
            self.threads = threads

    @property
    def sockets(self):
        """Gets the sockets of this CpuTopology.  # noqa: E501


        :return: The sockets of this CpuTopology.  # noqa: E501
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        """Sets the sockets of this CpuTopology.


        :param sockets: The sockets of this CpuTopology.  # noqa: E501
        :type: int
        """

        self._sockets = sockets

    @property
    def cores(self):
        """Gets the cores of this CpuTopology.  # noqa: E501


        :return: The cores of this CpuTopology.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this CpuTopology.


        :param cores: The cores of this CpuTopology.  # noqa: E501
        :type: int
        """

        self._cores = cores

    @property
    def threads(self):
        """Gets the threads of this CpuTopology.  # noqa: E501


        :return: The threads of this CpuTopology.  # noqa: E501
        :rtype: int
        """
        return self._threads

    @threads.setter
    def threads(self, threads):
        """Sets the threads of this CpuTopology.


        :param threads: The threads of this CpuTopology.  # noqa: E501
        :type: int
        """

        self._threads = threads

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
        if issubclass(CpuTopology, dict):
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
        if not isinstance(other, CpuTopology):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CpuTopology):
            return True

        return self.to_dict() != other.to_dict()
