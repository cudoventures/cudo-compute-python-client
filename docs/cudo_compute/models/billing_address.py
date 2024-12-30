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


class BillingAddress(object):
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
        'name': 'str',
        'phone': 'str',
        'city': 'str',
        'line1': 'str',
        'line2': 'str',
        'state': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'city': 'city',
        'line1': 'line1',
        'line2': 'line2',
        'state': 'state',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, name=None, phone=None, city=None, line1=None, line2=None, state=None, postal_code=None, country=None, _configuration=None):  # noqa: E501
        """BillingAddress - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._phone = None
        self._city = None
        self._line1 = None
        self._line2 = None
        self._state = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if city is not None:
            self.city = city
        if line1 is not None:
            self.line1 = line1
        if line2 is not None:
            self.line2 = line2
        if state is not None:
            self.state = state
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def name(self):
        """Gets the name of this BillingAddress.  # noqa: E501


        :return: The name of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillingAddress.


        :param name: The name of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this BillingAddress.  # noqa: E501


        :return: The phone of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this BillingAddress.


        :param phone: The phone of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def city(self):
        """Gets the city of this BillingAddress.  # noqa: E501


        :return: The city of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this BillingAddress.


        :param city: The city of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def line1(self):
        """Gets the line1 of this BillingAddress.  # noqa: E501


        :return: The line1 of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this BillingAddress.


        :param line1: The line1 of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this BillingAddress.  # noqa: E501


        :return: The line2 of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this BillingAddress.


        :param line2: The line2 of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._line2 = line2

    @property
    def state(self):
        """Gets the state of this BillingAddress.  # noqa: E501


        :return: The state of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BillingAddress.


        :param state: The state of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def postal_code(self):
        """Gets the postal_code of this BillingAddress.  # noqa: E501


        :return: The postal_code of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this BillingAddress.


        :param postal_code: The postal_code of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this BillingAddress.  # noqa: E501


        :return: The country of this BillingAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this BillingAddress.


        :param country: The country of this BillingAddress.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if issubclass(BillingAddress, dict):
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
        if not isinstance(other, BillingAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingAddress):
            return True

        return self.to_dict() != other.to_dict()