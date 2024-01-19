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


class VMDataCenter(object):
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
        'disk_pool_pricing': 'list[DiskStoragePriceHr]',
        'id': 'str',
        'ipv4_price_hr': 'Decimal',
        'network_pricing': 'list[NetworkPriceHr]',
        'region_id': 'str',
        'renewable_energy': 'bool',
        'supplier_name': 'str'
    }

    attribute_map = {
        'disk_pool_pricing': 'diskPoolPricing',
        'id': 'id',
        'ipv4_price_hr': 'ipv4PriceHr',
        'network_pricing': 'networkPricing',
        'region_id': 'regionId',
        'renewable_energy': 'renewableEnergy',
        'supplier_name': 'supplierName'
    }

    def __init__(self, disk_pool_pricing=None, id=None, ipv4_price_hr=None, network_pricing=None, region_id=None, renewable_energy=None, supplier_name=None, _configuration=None):  # noqa: E501
        """VMDataCenter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._disk_pool_pricing = None
        self._id = None
        self._ipv4_price_hr = None
        self._network_pricing = None
        self._region_id = None
        self._renewable_energy = None
        self._supplier_name = None
        self.discriminator = None

        if disk_pool_pricing is not None:
            self.disk_pool_pricing = disk_pool_pricing
        self.id = id
        if ipv4_price_hr is not None:
            self.ipv4_price_hr = ipv4_price_hr
        if network_pricing is not None:
            self.network_pricing = network_pricing
        self.region_id = region_id
        self.renewable_energy = renewable_energy
        self.supplier_name = supplier_name

    @property
    def disk_pool_pricing(self):
        """Gets the disk_pool_pricing of this VMDataCenter.  # noqa: E501


        :return: The disk_pool_pricing of this VMDataCenter.  # noqa: E501
        :rtype: list[DiskStoragePriceHr]
        """
        return self._disk_pool_pricing

    @disk_pool_pricing.setter
    def disk_pool_pricing(self, disk_pool_pricing):
        """Sets the disk_pool_pricing of this VMDataCenter.


        :param disk_pool_pricing: The disk_pool_pricing of this VMDataCenter.  # noqa: E501
        :type: list[DiskStoragePriceHr]
        """

        self._disk_pool_pricing = disk_pool_pricing

    @property
    def id(self):
        """Gets the id of this VMDataCenter.  # noqa: E501


        :return: The id of this VMDataCenter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VMDataCenter.


        :param id: The id of this VMDataCenter.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ipv4_price_hr(self):
        """Gets the ipv4_price_hr of this VMDataCenter.  # noqa: E501


        :return: The ipv4_price_hr of this VMDataCenter.  # noqa: E501
        :rtype: Decimal
        """
        return self._ipv4_price_hr

    @ipv4_price_hr.setter
    def ipv4_price_hr(self, ipv4_price_hr):
        """Sets the ipv4_price_hr of this VMDataCenter.


        :param ipv4_price_hr: The ipv4_price_hr of this VMDataCenter.  # noqa: E501
        :type: Decimal
        """

        self._ipv4_price_hr = ipv4_price_hr

    @property
    def network_pricing(self):
        """Gets the network_pricing of this VMDataCenter.  # noqa: E501


        :return: The network_pricing of this VMDataCenter.  # noqa: E501
        :rtype: list[NetworkPriceHr]
        """
        return self._network_pricing

    @network_pricing.setter
    def network_pricing(self, network_pricing):
        """Sets the network_pricing of this VMDataCenter.


        :param network_pricing: The network_pricing of this VMDataCenter.  # noqa: E501
        :type: list[NetworkPriceHr]
        """

        self._network_pricing = network_pricing

    @property
    def region_id(self):
        """Gets the region_id of this VMDataCenter.  # noqa: E501


        :return: The region_id of this VMDataCenter.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this VMDataCenter.


        :param region_id: The region_id of this VMDataCenter.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def renewable_energy(self):
        """Gets the renewable_energy of this VMDataCenter.  # noqa: E501


        :return: The renewable_energy of this VMDataCenter.  # noqa: E501
        :rtype: bool
        """
        return self._renewable_energy

    @renewable_energy.setter
    def renewable_energy(self, renewable_energy):
        """Sets the renewable_energy of this VMDataCenter.


        :param renewable_energy: The renewable_energy of this VMDataCenter.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and renewable_energy is None:
            raise ValueError("Invalid value for `renewable_energy`, must not be `None`")  # noqa: E501

        self._renewable_energy = renewable_energy

    @property
    def supplier_name(self):
        """Gets the supplier_name of this VMDataCenter.  # noqa: E501


        :return: The supplier_name of this VMDataCenter.  # noqa: E501
        :rtype: str
        """
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, supplier_name):
        """Sets the supplier_name of this VMDataCenter.


        :param supplier_name: The supplier_name of this VMDataCenter.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and supplier_name is None:
            raise ValueError("Invalid value for `supplier_name`, must not be `None`")  # noqa: E501

        self._supplier_name = supplier_name

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
        if issubclass(VMDataCenter, dict):
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
        if not isinstance(other, VMDataCenter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VMDataCenter):
            return True

        return self.to_dict() != other.to_dict()
