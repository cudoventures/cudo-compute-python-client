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


class NetworkPriceHr(object):
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
        'price_hr': 'Decimal',
        'size': 'VRouterSize'
    }

    attribute_map = {
        'price_hr': 'priceHr',
        'size': 'size'
    }

    def __init__(self, price_hr=None, size=None, _configuration=None):  # noqa: E501
        """NetworkPriceHr - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._price_hr = None
        self._size = None
        self.discriminator = None

        if price_hr is not None:
            self.price_hr = price_hr
        if size is not None:
            self.size = size

    @property
    def price_hr(self):
        """Gets the price_hr of this NetworkPriceHr.  # noqa: E501


        :return: The price_hr of this NetworkPriceHr.  # noqa: E501
        :rtype: Decimal
        """
        return self._price_hr

    @price_hr.setter
    def price_hr(self, price_hr):
        """Sets the price_hr of this NetworkPriceHr.


        :param price_hr: The price_hr of this NetworkPriceHr.  # noqa: E501
        :type: Decimal
        """

        self._price_hr = price_hr

    @property
    def size(self):
        """Gets the size of this NetworkPriceHr.  # noqa: E501


        :return: The size of this NetworkPriceHr.  # noqa: E501
        :rtype: VRouterSize
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NetworkPriceHr.


        :param size: The size of this NetworkPriceHr.  # noqa: E501
        :type: VRouterSize
        """

        self._size = size

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
        if issubclass(NetworkPriceHr, dict):
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
        if not isinstance(other, NetworkPriceHr):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkPriceHr):
            return True

        return self.to_dict() != other.to_dict()
