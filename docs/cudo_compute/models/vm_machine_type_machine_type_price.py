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


class VMMachineTypeMachineTypePrice(object):
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
        'vcpu_price_hr': 'Decimal',
        'memory_gib_price_hr': 'Decimal',
        'gpu_price_hr': 'Decimal',
        'commitment_term': 'CommitmentTerm'
    }

    attribute_map = {
        'vcpu_price_hr': 'vcpuPriceHr',
        'memory_gib_price_hr': 'memoryGibPriceHr',
        'gpu_price_hr': 'gpuPriceHr',
        'commitment_term': 'commitmentTerm'
    }

    def __init__(self, vcpu_price_hr=None, memory_gib_price_hr=None, gpu_price_hr=None, commitment_term=None, _configuration=None):  # noqa: E501
        """VMMachineTypeMachineTypePrice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vcpu_price_hr = None
        self._memory_gib_price_hr = None
        self._gpu_price_hr = None
        self._commitment_term = None
        self.discriminator = None

        self.vcpu_price_hr = vcpu_price_hr
        self.memory_gib_price_hr = memory_gib_price_hr
        self.gpu_price_hr = gpu_price_hr
        self.commitment_term = commitment_term

    @property
    def vcpu_price_hr(self):
        """Gets the vcpu_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501


        :return: The vcpu_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501
        :rtype: Decimal
        """
        return self._vcpu_price_hr

    @vcpu_price_hr.setter
    def vcpu_price_hr(self, vcpu_price_hr):
        """Sets the vcpu_price_hr of this VMMachineTypeMachineTypePrice.


        :param vcpu_price_hr: The vcpu_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and vcpu_price_hr is None:
            raise ValueError("Invalid value for `vcpu_price_hr`, must not be `None`")  # noqa: E501

        self._vcpu_price_hr = vcpu_price_hr

    @property
    def memory_gib_price_hr(self):
        """Gets the memory_gib_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501


        :return: The memory_gib_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501
        :rtype: Decimal
        """
        return self._memory_gib_price_hr

    @memory_gib_price_hr.setter
    def memory_gib_price_hr(self, memory_gib_price_hr):
        """Sets the memory_gib_price_hr of this VMMachineTypeMachineTypePrice.


        :param memory_gib_price_hr: The memory_gib_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and memory_gib_price_hr is None:
            raise ValueError("Invalid value for `memory_gib_price_hr`, must not be `None`")  # noqa: E501

        self._memory_gib_price_hr = memory_gib_price_hr

    @property
    def gpu_price_hr(self):
        """Gets the gpu_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501


        :return: The gpu_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501
        :rtype: Decimal
        """
        return self._gpu_price_hr

    @gpu_price_hr.setter
    def gpu_price_hr(self, gpu_price_hr):
        """Sets the gpu_price_hr of this VMMachineTypeMachineTypePrice.


        :param gpu_price_hr: The gpu_price_hr of this VMMachineTypeMachineTypePrice.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and gpu_price_hr is None:
            raise ValueError("Invalid value for `gpu_price_hr`, must not be `None`")  # noqa: E501

        self._gpu_price_hr = gpu_price_hr

    @property
    def commitment_term(self):
        """Gets the commitment_term of this VMMachineTypeMachineTypePrice.  # noqa: E501


        :return: The commitment_term of this VMMachineTypeMachineTypePrice.  # noqa: E501
        :rtype: CommitmentTerm
        """
        return self._commitment_term

    @commitment_term.setter
    def commitment_term(self, commitment_term):
        """Sets the commitment_term of this VMMachineTypeMachineTypePrice.


        :param commitment_term: The commitment_term of this VMMachineTypeMachineTypePrice.  # noqa: E501
        :type: CommitmentTerm
        """
        if self._configuration.client_side_validation and commitment_term is None:
            raise ValueError("Invalid value for `commitment_term`, must not be `None`")  # noqa: E501

        self._commitment_term = commitment_term

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
        if issubclass(VMMachineTypeMachineTypePrice, dict):
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
        if not isinstance(other, VMMachineTypeMachineTypePrice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VMMachineTypeMachineTypePrice):
            return True

        return self.to_dict() != other.to_dict()