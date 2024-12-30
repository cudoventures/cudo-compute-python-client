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


class GetMachineTypeResponse(object):
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
        'data_center_id': 'str',
        'machine_type': 'str',
        'cpu_models': 'list[str]',
        'gpu_models': 'list[str]',
        'min_vcpu_price_hr': 'Decimal',
        'max_vcpu_price_hr': 'Decimal',
        'min_memory_gib_price_hr': 'Decimal',
        'max_memory_gib_price_hr': 'Decimal',
        'min_gpu_price_hr': 'Decimal',
        'max_gpu_price_hr': 'Decimal',
        'min_vcpu_per_memory_gib': 'float',
        'max_vcpu_per_memory_gib': 'float',
        'min_vcpu_per_gpu': 'float',
        'max_vcpu_per_gpu': 'float',
        'count_clusters': 'int',
        'count_hosts': 'int',
        'count_hosts_active': 'int',
        'count_hosts_inactive': 'int',
        'min_vcpu': 'float',
        'min_memory_gib': 'float'
    }

    attribute_map = {
        'data_center_id': 'dataCenterId',
        'machine_type': 'machineType',
        'cpu_models': 'cpuModels',
        'gpu_models': 'gpuModels',
        'min_vcpu_price_hr': 'minVcpuPriceHr',
        'max_vcpu_price_hr': 'maxVcpuPriceHr',
        'min_memory_gib_price_hr': 'minMemoryGibPriceHr',
        'max_memory_gib_price_hr': 'maxMemoryGibPriceHr',
        'min_gpu_price_hr': 'minGpuPriceHr',
        'max_gpu_price_hr': 'maxGpuPriceHr',
        'min_vcpu_per_memory_gib': 'minVcpuPerMemoryGib',
        'max_vcpu_per_memory_gib': 'maxVcpuPerMemoryGib',
        'min_vcpu_per_gpu': 'minVcpuPerGpu',
        'max_vcpu_per_gpu': 'maxVcpuPerGpu',
        'count_clusters': 'countClusters',
        'count_hosts': 'countHosts',
        'count_hosts_active': 'countHostsActive',
        'count_hosts_inactive': 'countHostsInactive',
        'min_vcpu': 'minVcpu',
        'min_memory_gib': 'minMemoryGib'
    }

    def __init__(self, data_center_id=None, machine_type=None, cpu_models=None, gpu_models=None, min_vcpu_price_hr=None, max_vcpu_price_hr=None, min_memory_gib_price_hr=None, max_memory_gib_price_hr=None, min_gpu_price_hr=None, max_gpu_price_hr=None, min_vcpu_per_memory_gib=None, max_vcpu_per_memory_gib=None, min_vcpu_per_gpu=None, max_vcpu_per_gpu=None, count_clusters=None, count_hosts=None, count_hosts_active=None, count_hosts_inactive=None, min_vcpu=None, min_memory_gib=None, _configuration=None):  # noqa: E501
        """GetMachineTypeResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_center_id = None
        self._machine_type = None
        self._cpu_models = None
        self._gpu_models = None
        self._min_vcpu_price_hr = None
        self._max_vcpu_price_hr = None
        self._min_memory_gib_price_hr = None
        self._max_memory_gib_price_hr = None
        self._min_gpu_price_hr = None
        self._max_gpu_price_hr = None
        self._min_vcpu_per_memory_gib = None
        self._max_vcpu_per_memory_gib = None
        self._min_vcpu_per_gpu = None
        self._max_vcpu_per_gpu = None
        self._count_clusters = None
        self._count_hosts = None
        self._count_hosts_active = None
        self._count_hosts_inactive = None
        self._min_vcpu = None
        self._min_memory_gib = None
        self.discriminator = None

        self.data_center_id = data_center_id
        self.machine_type = machine_type
        self.cpu_models = cpu_models
        self.gpu_models = gpu_models
        self.min_vcpu_price_hr = min_vcpu_price_hr
        self.max_vcpu_price_hr = max_vcpu_price_hr
        self.min_memory_gib_price_hr = min_memory_gib_price_hr
        self.max_memory_gib_price_hr = max_memory_gib_price_hr
        self.min_gpu_price_hr = min_gpu_price_hr
        self.max_gpu_price_hr = max_gpu_price_hr
        self.min_vcpu_per_memory_gib = min_vcpu_per_memory_gib
        self.max_vcpu_per_memory_gib = max_vcpu_per_memory_gib
        self.min_vcpu_per_gpu = min_vcpu_per_gpu
        self.max_vcpu_per_gpu = max_vcpu_per_gpu
        self.count_clusters = count_clusters
        self.count_hosts = count_hosts
        self.count_hosts_active = count_hosts_active
        self.count_hosts_inactive = count_hosts_inactive
        self.min_vcpu = min_vcpu
        self.min_memory_gib = min_memory_gib

    @property
    def data_center_id(self):
        """Gets the data_center_id of this GetMachineTypeResponse.  # noqa: E501


        :return: The data_center_id of this GetMachineTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this GetMachineTypeResponse.


        :param data_center_id: The data_center_id of this GetMachineTypeResponse.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and data_center_id is None:
            raise ValueError("Invalid value for `data_center_id`, must not be `None`")  # noqa: E501

        self._data_center_id = data_center_id

    @property
    def machine_type(self):
        """Gets the machine_type of this GetMachineTypeResponse.  # noqa: E501


        :return: The machine_type of this GetMachineTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this GetMachineTypeResponse.


        :param machine_type: The machine_type of this GetMachineTypeResponse.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and machine_type is None:
            raise ValueError("Invalid value for `machine_type`, must not be `None`")  # noqa: E501

        self._machine_type = machine_type

    @property
    def cpu_models(self):
        """Gets the cpu_models of this GetMachineTypeResponse.  # noqa: E501


        :return: The cpu_models of this GetMachineTypeResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._cpu_models

    @cpu_models.setter
    def cpu_models(self, cpu_models):
        """Sets the cpu_models of this GetMachineTypeResponse.


        :param cpu_models: The cpu_models of this GetMachineTypeResponse.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and cpu_models is None:
            raise ValueError("Invalid value for `cpu_models`, must not be `None`")  # noqa: E501

        self._cpu_models = cpu_models

    @property
    def gpu_models(self):
        """Gets the gpu_models of this GetMachineTypeResponse.  # noqa: E501


        :return: The gpu_models of this GetMachineTypeResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._gpu_models

    @gpu_models.setter
    def gpu_models(self, gpu_models):
        """Sets the gpu_models of this GetMachineTypeResponse.


        :param gpu_models: The gpu_models of this GetMachineTypeResponse.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and gpu_models is None:
            raise ValueError("Invalid value for `gpu_models`, must not be `None`")  # noqa: E501

        self._gpu_models = gpu_models

    @property
    def min_vcpu_price_hr(self):
        """Gets the min_vcpu_price_hr of this GetMachineTypeResponse.  # noqa: E501


        :return: The min_vcpu_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._min_vcpu_price_hr

    @min_vcpu_price_hr.setter
    def min_vcpu_price_hr(self, min_vcpu_price_hr):
        """Sets the min_vcpu_price_hr of this GetMachineTypeResponse.


        :param min_vcpu_price_hr: The min_vcpu_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and min_vcpu_price_hr is None:
            raise ValueError("Invalid value for `min_vcpu_price_hr`, must not be `None`")  # noqa: E501

        self._min_vcpu_price_hr = min_vcpu_price_hr

    @property
    def max_vcpu_price_hr(self):
        """Gets the max_vcpu_price_hr of this GetMachineTypeResponse.  # noqa: E501


        :return: The max_vcpu_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._max_vcpu_price_hr

    @max_vcpu_price_hr.setter
    def max_vcpu_price_hr(self, max_vcpu_price_hr):
        """Sets the max_vcpu_price_hr of this GetMachineTypeResponse.


        :param max_vcpu_price_hr: The max_vcpu_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and max_vcpu_price_hr is None:
            raise ValueError("Invalid value for `max_vcpu_price_hr`, must not be `None`")  # noqa: E501

        self._max_vcpu_price_hr = max_vcpu_price_hr

    @property
    def min_memory_gib_price_hr(self):
        """Gets the min_memory_gib_price_hr of this GetMachineTypeResponse.  # noqa: E501


        :return: The min_memory_gib_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._min_memory_gib_price_hr

    @min_memory_gib_price_hr.setter
    def min_memory_gib_price_hr(self, min_memory_gib_price_hr):
        """Sets the min_memory_gib_price_hr of this GetMachineTypeResponse.


        :param min_memory_gib_price_hr: The min_memory_gib_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and min_memory_gib_price_hr is None:
            raise ValueError("Invalid value for `min_memory_gib_price_hr`, must not be `None`")  # noqa: E501

        self._min_memory_gib_price_hr = min_memory_gib_price_hr

    @property
    def max_memory_gib_price_hr(self):
        """Gets the max_memory_gib_price_hr of this GetMachineTypeResponse.  # noqa: E501


        :return: The max_memory_gib_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._max_memory_gib_price_hr

    @max_memory_gib_price_hr.setter
    def max_memory_gib_price_hr(self, max_memory_gib_price_hr):
        """Sets the max_memory_gib_price_hr of this GetMachineTypeResponse.


        :param max_memory_gib_price_hr: The max_memory_gib_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and max_memory_gib_price_hr is None:
            raise ValueError("Invalid value for `max_memory_gib_price_hr`, must not be `None`")  # noqa: E501

        self._max_memory_gib_price_hr = max_memory_gib_price_hr

    @property
    def min_gpu_price_hr(self):
        """Gets the min_gpu_price_hr of this GetMachineTypeResponse.  # noqa: E501


        :return: The min_gpu_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._min_gpu_price_hr

    @min_gpu_price_hr.setter
    def min_gpu_price_hr(self, min_gpu_price_hr):
        """Sets the min_gpu_price_hr of this GetMachineTypeResponse.


        :param min_gpu_price_hr: The min_gpu_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and min_gpu_price_hr is None:
            raise ValueError("Invalid value for `min_gpu_price_hr`, must not be `None`")  # noqa: E501

        self._min_gpu_price_hr = min_gpu_price_hr

    @property
    def max_gpu_price_hr(self):
        """Gets the max_gpu_price_hr of this GetMachineTypeResponse.  # noqa: E501


        :return: The max_gpu_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._max_gpu_price_hr

    @max_gpu_price_hr.setter
    def max_gpu_price_hr(self, max_gpu_price_hr):
        """Sets the max_gpu_price_hr of this GetMachineTypeResponse.


        :param max_gpu_price_hr: The max_gpu_price_hr of this GetMachineTypeResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and max_gpu_price_hr is None:
            raise ValueError("Invalid value for `max_gpu_price_hr`, must not be `None`")  # noqa: E501

        self._max_gpu_price_hr = max_gpu_price_hr

    @property
    def min_vcpu_per_memory_gib(self):
        """Gets the min_vcpu_per_memory_gib of this GetMachineTypeResponse.  # noqa: E501


        :return: The min_vcpu_per_memory_gib of this GetMachineTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._min_vcpu_per_memory_gib

    @min_vcpu_per_memory_gib.setter
    def min_vcpu_per_memory_gib(self, min_vcpu_per_memory_gib):
        """Sets the min_vcpu_per_memory_gib of this GetMachineTypeResponse.


        :param min_vcpu_per_memory_gib: The min_vcpu_per_memory_gib of this GetMachineTypeResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and min_vcpu_per_memory_gib is None:
            raise ValueError("Invalid value for `min_vcpu_per_memory_gib`, must not be `None`")  # noqa: E501

        self._min_vcpu_per_memory_gib = min_vcpu_per_memory_gib

    @property
    def max_vcpu_per_memory_gib(self):
        """Gets the max_vcpu_per_memory_gib of this GetMachineTypeResponse.  # noqa: E501


        :return: The max_vcpu_per_memory_gib of this GetMachineTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._max_vcpu_per_memory_gib

    @max_vcpu_per_memory_gib.setter
    def max_vcpu_per_memory_gib(self, max_vcpu_per_memory_gib):
        """Sets the max_vcpu_per_memory_gib of this GetMachineTypeResponse.


        :param max_vcpu_per_memory_gib: The max_vcpu_per_memory_gib of this GetMachineTypeResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and max_vcpu_per_memory_gib is None:
            raise ValueError("Invalid value for `max_vcpu_per_memory_gib`, must not be `None`")  # noqa: E501

        self._max_vcpu_per_memory_gib = max_vcpu_per_memory_gib

    @property
    def min_vcpu_per_gpu(self):
        """Gets the min_vcpu_per_gpu of this GetMachineTypeResponse.  # noqa: E501


        :return: The min_vcpu_per_gpu of this GetMachineTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._min_vcpu_per_gpu

    @min_vcpu_per_gpu.setter
    def min_vcpu_per_gpu(self, min_vcpu_per_gpu):
        """Sets the min_vcpu_per_gpu of this GetMachineTypeResponse.


        :param min_vcpu_per_gpu: The min_vcpu_per_gpu of this GetMachineTypeResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and min_vcpu_per_gpu is None:
            raise ValueError("Invalid value for `min_vcpu_per_gpu`, must not be `None`")  # noqa: E501

        self._min_vcpu_per_gpu = min_vcpu_per_gpu

    @property
    def max_vcpu_per_gpu(self):
        """Gets the max_vcpu_per_gpu of this GetMachineTypeResponse.  # noqa: E501


        :return: The max_vcpu_per_gpu of this GetMachineTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._max_vcpu_per_gpu

    @max_vcpu_per_gpu.setter
    def max_vcpu_per_gpu(self, max_vcpu_per_gpu):
        """Sets the max_vcpu_per_gpu of this GetMachineTypeResponse.


        :param max_vcpu_per_gpu: The max_vcpu_per_gpu of this GetMachineTypeResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and max_vcpu_per_gpu is None:
            raise ValueError("Invalid value for `max_vcpu_per_gpu`, must not be `None`")  # noqa: E501

        self._max_vcpu_per_gpu = max_vcpu_per_gpu

    @property
    def count_clusters(self):
        """Gets the count_clusters of this GetMachineTypeResponse.  # noqa: E501


        :return: The count_clusters of this GetMachineTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_clusters

    @count_clusters.setter
    def count_clusters(self, count_clusters):
        """Sets the count_clusters of this GetMachineTypeResponse.


        :param count_clusters: The count_clusters of this GetMachineTypeResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_clusters is None:
            raise ValueError("Invalid value for `count_clusters`, must not be `None`")  # noqa: E501

        self._count_clusters = count_clusters

    @property
    def count_hosts(self):
        """Gets the count_hosts of this GetMachineTypeResponse.  # noqa: E501


        :return: The count_hosts of this GetMachineTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_hosts

    @count_hosts.setter
    def count_hosts(self, count_hosts):
        """Sets the count_hosts of this GetMachineTypeResponse.


        :param count_hosts: The count_hosts of this GetMachineTypeResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_hosts is None:
            raise ValueError("Invalid value for `count_hosts`, must not be `None`")  # noqa: E501

        self._count_hosts = count_hosts

    @property
    def count_hosts_active(self):
        """Gets the count_hosts_active of this GetMachineTypeResponse.  # noqa: E501


        :return: The count_hosts_active of this GetMachineTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_hosts_active

    @count_hosts_active.setter
    def count_hosts_active(self, count_hosts_active):
        """Sets the count_hosts_active of this GetMachineTypeResponse.


        :param count_hosts_active: The count_hosts_active of this GetMachineTypeResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_hosts_active is None:
            raise ValueError("Invalid value for `count_hosts_active`, must not be `None`")  # noqa: E501

        self._count_hosts_active = count_hosts_active

    @property
    def count_hosts_inactive(self):
        """Gets the count_hosts_inactive of this GetMachineTypeResponse.  # noqa: E501


        :return: The count_hosts_inactive of this GetMachineTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_hosts_inactive

    @count_hosts_inactive.setter
    def count_hosts_inactive(self, count_hosts_inactive):
        """Sets the count_hosts_inactive of this GetMachineTypeResponse.


        :param count_hosts_inactive: The count_hosts_inactive of this GetMachineTypeResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_hosts_inactive is None:
            raise ValueError("Invalid value for `count_hosts_inactive`, must not be `None`")  # noqa: E501

        self._count_hosts_inactive = count_hosts_inactive

    @property
    def min_vcpu(self):
        """Gets the min_vcpu of this GetMachineTypeResponse.  # noqa: E501


        :return: The min_vcpu of this GetMachineTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._min_vcpu

    @min_vcpu.setter
    def min_vcpu(self, min_vcpu):
        """Sets the min_vcpu of this GetMachineTypeResponse.


        :param min_vcpu: The min_vcpu of this GetMachineTypeResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and min_vcpu is None:
            raise ValueError("Invalid value for `min_vcpu`, must not be `None`")  # noqa: E501

        self._min_vcpu = min_vcpu

    @property
    def min_memory_gib(self):
        """Gets the min_memory_gib of this GetMachineTypeResponse.  # noqa: E501


        :return: The min_memory_gib of this GetMachineTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._min_memory_gib

    @min_memory_gib.setter
    def min_memory_gib(self, min_memory_gib):
        """Sets the min_memory_gib of this GetMachineTypeResponse.


        :param min_memory_gib: The min_memory_gib of this GetMachineTypeResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and min_memory_gib is None:
            raise ValueError("Invalid value for `min_memory_gib`, must not be `None`")  # noqa: E501

        self._min_memory_gib = min_memory_gib

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
        if issubclass(GetMachineTypeResponse, dict):
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
        if not isinstance(other, GetMachineTypeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetMachineTypeResponse):
            return True

        return self.to_dict() != other.to_dict()