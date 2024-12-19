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


class UpdateBillingAccountBody(object):
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
        'billing_account': 'UpdateBillingAccountBodyBillingAccount',
        'update_mask': 'str'
    }

    attribute_map = {
        'billing_account': 'billingAccount',
        'update_mask': 'updateMask'
    }

    def __init__(self, billing_account=None, update_mask=None, _configuration=None):  # noqa: E501
        """UpdateBillingAccountBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billing_account = None
        self._update_mask = None
        self.discriminator = None

        if billing_account is not None:
            self.billing_account = billing_account
        self.update_mask = update_mask

    @property
    def billing_account(self):
        """Gets the billing_account of this UpdateBillingAccountBody.  # noqa: E501


        :return: The billing_account of this UpdateBillingAccountBody.  # noqa: E501
        :rtype: UpdateBillingAccountBodyBillingAccount
        """
        return self._billing_account

    @billing_account.setter
    def billing_account(self, billing_account):
        """Sets the billing_account of this UpdateBillingAccountBody.


        :param billing_account: The billing_account of this UpdateBillingAccountBody.  # noqa: E501
        :type: UpdateBillingAccountBodyBillingAccount
        """

        self._billing_account = billing_account

    @property
    def update_mask(self):
        """Gets the update_mask of this UpdateBillingAccountBody.  # noqa: E501


        :return: The update_mask of this UpdateBillingAccountBody.  # noqa: E501
        :rtype: str
        """
        return self._update_mask

    @update_mask.setter
    def update_mask(self, update_mask):
        """Sets the update_mask of this UpdateBillingAccountBody.


        :param update_mask: The update_mask of this UpdateBillingAccountBody.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and update_mask is None:
            raise ValueError("Invalid value for `update_mask`, must not be `None`")  # noqa: E501

        self._update_mask = update_mask

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
        if issubclass(UpdateBillingAccountBody, dict):
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
        if not isinstance(other, UpdateBillingAccountBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateBillingAccountBody):
            return True

        return self.to_dict() != other.to_dict()
