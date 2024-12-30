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


class DataCenterRevenueResource(object):
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
        'resource_type': 'str',
        'resource_id': 'str',
        'quantity': 'Decimal',
        'unit': 'str',
        'revenue_usd': 'Decimal'
    }

    attribute_map = {
        'resource_type': 'resourceType',
        'resource_id': 'resourceId',
        'quantity': 'quantity',
        'unit': 'unit',
        'revenue_usd': 'revenueUsd'
    }

    def __init__(self, resource_type=None, resource_id=None, quantity=None, unit=None, revenue_usd=None, _configuration=None):  # noqa: E501
        """DataCenterRevenueResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_type = None
        self._resource_id = None
        self._quantity = None
        self._unit = None
        self._revenue_usd = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id
        self.quantity = quantity
        self.unit = unit
        self.revenue_usd = revenue_usd

    @property
    def resource_type(self):
        """Gets the resource_type of this DataCenterRevenueResource.  # noqa: E501


        :return: The resource_type of this DataCenterRevenueResource.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DataCenterRevenueResource.


        :param resource_type: The resource_type of this DataCenterRevenueResource.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this DataCenterRevenueResource.  # noqa: E501


        :return: The resource_id of this DataCenterRevenueResource.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this DataCenterRevenueResource.


        :param resource_id: The resource_id of this DataCenterRevenueResource.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501

        self._resource_id = resource_id

    @property
    def quantity(self):
        """Gets the quantity of this DataCenterRevenueResource.  # noqa: E501


        :return: The quantity of this DataCenterRevenueResource.  # noqa: E501
        :rtype: Decimal
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this DataCenterRevenueResource.


        :param quantity: The quantity of this DataCenterRevenueResource.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def unit(self):
        """Gets the unit of this DataCenterRevenueResource.  # noqa: E501


        :return: The unit of this DataCenterRevenueResource.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DataCenterRevenueResource.


        :param unit: The unit of this DataCenterRevenueResource.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def revenue_usd(self):
        """Gets the revenue_usd of this DataCenterRevenueResource.  # noqa: E501


        :return: The revenue_usd of this DataCenterRevenueResource.  # noqa: E501
        :rtype: Decimal
        """
        return self._revenue_usd

    @revenue_usd.setter
    def revenue_usd(self, revenue_usd):
        """Sets the revenue_usd of this DataCenterRevenueResource.


        :param revenue_usd: The revenue_usd of this DataCenterRevenueResource.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and revenue_usd is None:
            raise ValueError("Invalid value for `revenue_usd`, must not be `None`")  # noqa: E501

        self._revenue_usd = revenue_usd

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
        if issubclass(DataCenterRevenueResource, dict):
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
        if not isinstance(other, DataCenterRevenueResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataCenterRevenueResource):
            return True

        return self.to_dict() != other.to_dict()
