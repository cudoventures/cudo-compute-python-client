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


class DataCenterCategory(object):
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
        'count_vm_available': 'int',
        'id': 'str',
        'min_price_hr': 'Decimal',
        'renewable_energy': 'bool'
    }

    attribute_map = {
        'count_vm_available': 'countVmAvailable',
        'id': 'id',
        'min_price_hr': 'minPriceHr',
        'renewable_energy': 'renewableEnergy'
    }

    def __init__(self, count_vm_available=None, id=None, min_price_hr=None, renewable_energy=None, _configuration=None):  # noqa: E501
        """DataCenterCategory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count_vm_available = None
        self._id = None
        self._min_price_hr = None
        self._renewable_energy = None
        self.discriminator = None

        self.count_vm_available = count_vm_available
        self.id = id
        self.min_price_hr = min_price_hr
        self.renewable_energy = renewable_energy

    @property
    def count_vm_available(self):
        """Gets the count_vm_available of this DataCenterCategory.  # noqa: E501


        :return: The count_vm_available of this DataCenterCategory.  # noqa: E501
        :rtype: int
        """
        return self._count_vm_available

    @count_vm_available.setter
    def count_vm_available(self, count_vm_available):
        """Sets the count_vm_available of this DataCenterCategory.


        :param count_vm_available: The count_vm_available of this DataCenterCategory.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_vm_available is None:
            raise ValueError("Invalid value for `count_vm_available`, must not be `None`")  # noqa: E501

        self._count_vm_available = count_vm_available

    @property
    def id(self):
        """Gets the id of this DataCenterCategory.  # noqa: E501


        :return: The id of this DataCenterCategory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataCenterCategory.


        :param id: The id of this DataCenterCategory.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def min_price_hr(self):
        """Gets the min_price_hr of this DataCenterCategory.  # noqa: E501


        :return: The min_price_hr of this DataCenterCategory.  # noqa: E501
        :rtype: Decimal
        """
        return self._min_price_hr

    @min_price_hr.setter
    def min_price_hr(self, min_price_hr):
        """Sets the min_price_hr of this DataCenterCategory.


        :param min_price_hr: The min_price_hr of this DataCenterCategory.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and min_price_hr is None:
            raise ValueError("Invalid value for `min_price_hr`, must not be `None`")  # noqa: E501

        self._min_price_hr = min_price_hr

    @property
    def renewable_energy(self):
        """Gets the renewable_energy of this DataCenterCategory.  # noqa: E501


        :return: The renewable_energy of this DataCenterCategory.  # noqa: E501
        :rtype: bool
        """
        return self._renewable_energy

    @renewable_energy.setter
    def renewable_energy(self, renewable_energy):
        """Sets the renewable_energy of this DataCenterCategory.


        :param renewable_energy: The renewable_energy of this DataCenterCategory.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and renewable_energy is None:
            raise ValueError("Invalid value for `renewable_energy`, must not be `None`")  # noqa: E501

        self._renewable_energy = renewable_energy

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
        if issubclass(DataCenterCategory, dict):
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
        if not isinstance(other, DataCenterCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataCenterCategory):
            return True

        return self.to_dict() != other.to_dict()