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


class ListBillingAccountInvoicesResponse(object):
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
        'invoices': 'list[Invoice]',
        'has_more': 'bool'
    }

    attribute_map = {
        'invoices': 'invoices',
        'has_more': 'hasMore'
    }

    def __init__(self, invoices=None, has_more=None, _configuration=None):  # noqa: E501
        """ListBillingAccountInvoicesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._invoices = None
        self._has_more = None
        self.discriminator = None

        self.invoices = invoices
        self.has_more = has_more

    @property
    def invoices(self):
        """Gets the invoices of this ListBillingAccountInvoicesResponse.  # noqa: E501


        :return: The invoices of this ListBillingAccountInvoicesResponse.  # noqa: E501
        :rtype: list[Invoice]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this ListBillingAccountInvoicesResponse.


        :param invoices: The invoices of this ListBillingAccountInvoicesResponse.  # noqa: E501
        :type: list[Invoice]
        """
        if self._configuration.client_side_validation and invoices is None:
            raise ValueError("Invalid value for `invoices`, must not be `None`")  # noqa: E501

        self._invoices = invoices

    @property
    def has_more(self):
        """Gets the has_more of this ListBillingAccountInvoicesResponse.  # noqa: E501


        :return: The has_more of this ListBillingAccountInvoicesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this ListBillingAccountInvoicesResponse.


        :param has_more: The has_more of this ListBillingAccountInvoicesResponse.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")  # noqa: E501

        self._has_more = has_more

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
        if issubclass(ListBillingAccountInvoicesResponse, dict):
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
        if not isinstance(other, ListBillingAccountInvoicesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListBillingAccountInvoicesResponse):
            return True

        return self.to_dict() != other.to_dict()
