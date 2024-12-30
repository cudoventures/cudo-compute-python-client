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


class ListDataCenterMachineTypePricesResponse(object):
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
        'prices': 'list[ListDataCenterMachineTypePricesResponseMachineTypePrice]'
    }

    attribute_map = {
        'prices': 'prices'
    }

    def __init__(self, prices=None, _configuration=None):  # noqa: E501
        """ListDataCenterMachineTypePricesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._prices = None
        self.discriminator = None

        self.prices = prices

    @property
    def prices(self):
        """Gets the prices of this ListDataCenterMachineTypePricesResponse.  # noqa: E501


        :return: The prices of this ListDataCenterMachineTypePricesResponse.  # noqa: E501
        :rtype: list[ListDataCenterMachineTypePricesResponseMachineTypePrice]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this ListDataCenterMachineTypePricesResponse.


        :param prices: The prices of this ListDataCenterMachineTypePricesResponse.  # noqa: E501
        :type: list[ListDataCenterMachineTypePricesResponseMachineTypePrice]
        """
        if self._configuration.client_side_validation and prices is None:
            raise ValueError("Invalid value for `prices`, must not be `None`")  # noqa: E501

        self._prices = prices

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
        if issubclass(ListDataCenterMachineTypePricesResponse, dict):
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
        if not isinstance(other, ListDataCenterMachineTypePricesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListDataCenterMachineTypePricesResponse):
            return True

        return self.to_dict() != other.to_dict()