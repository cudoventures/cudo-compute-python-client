# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from src.cudo_compute.api_client import ApiClient


class PermissionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_billing_account_user_permission(self, billing_account_id, body, **kwargs):  # noqa: E501
        """Add billing account user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_billing_account_user_permission(billing_account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_account_id: (required)
        :param Body1 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_billing_account_user_permission_with_http_info(billing_account_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_billing_account_user_permission_with_http_info(billing_account_id, body, **kwargs)  # noqa: E501
            return data

    def add_billing_account_user_permission_with_http_info(self, billing_account_id, body, **kwargs):  # noqa: E501
        """Add billing account user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_billing_account_user_permission_with_http_info(billing_account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_account_id: (required)
        :param Body1 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_account_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_billing_account_user_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'billing_account_id' is set
        if self.api_client.client_side_validation and ('billing_account_id' not in params or
                                                       params['billing_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `billing_account_id` when calling `add_billing_account_user_permission`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `add_billing_account_user_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'billing_account_id' in params:
            path_params['billingAccountId'] = params['billing_account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/billing-accounts/{billingAccountId}/add-user-permission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_data_center_user_permission(self, data_center_id, body, **kwargs):  # noqa: E501
        """Add data center user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_data_center_user_permission(data_center_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :param Body3 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_data_center_user_permission_with_http_info(data_center_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_data_center_user_permission_with_http_info(data_center_id, body, **kwargs)  # noqa: E501
            return data

    def add_data_center_user_permission_with_http_info(self, data_center_id, body, **kwargs):  # noqa: E501
        """Add data center user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_data_center_user_permission_with_http_info(data_center_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :param Body3 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_center_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_data_center_user_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_center_id' is set
        if self.api_client.client_side_validation and ('data_center_id' not in params or
                                                       params['data_center_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_center_id` when calling `add_data_center_user_permission`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `add_data_center_user_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_center_id' in params:
            path_params['dataCenterId'] = params['data_center_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/data-centers/{dataCenterId}/add-user-permission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_project_user_permission(self, project_id, body, **kwargs):  # noqa: E501
        """Add project user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_project_user_permission(project_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param Body5 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_project_user_permission_with_http_info(project_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_project_user_permission_with_http_info(project_id, body, **kwargs)  # noqa: E501
            return data

    def add_project_user_permission_with_http_info(self, project_id, body, **kwargs):  # noqa: E501
        """Add project user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_project_user_permission_with_http_info(project_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param Body5 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_project_user_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `add_project_user_permission`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `add_project_user_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/projects/{projectId}/add-user-permission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_permissions(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_permissions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id:
        :param str data_center_id:
        :param str billing_account_id:
        :return: ListUserPermissionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_user_permissions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_user_permissions_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_user_permissions_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_user_permissions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id:
        :param str data_center_id:
        :param str billing_account_id:
        :return: ListUserPermissionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'data_center_id', 'billing_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_permissions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in params:
            query_params.append(('projectId', params['project_id']))  # noqa: E501
        if 'data_center_id' in params:
            query_params.append(('dataCenterId', params['data_center_id']))  # noqa: E501
        if 'billing_account_id' in params:
            query_params.append(('billingAccountId', params['billing_account_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/auth/permissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListUserPermissionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_billing_account_user_permission(self, billing_account_id, body, **kwargs):  # noqa: E501
        """Remove billing account user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_billing_account_user_permission(billing_account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_account_id: (required)
        :param Body2 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_billing_account_user_permission_with_http_info(billing_account_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_billing_account_user_permission_with_http_info(billing_account_id, body, **kwargs)  # noqa: E501
            return data

    def remove_billing_account_user_permission_with_http_info(self, billing_account_id, body, **kwargs):  # noqa: E501
        """Remove billing account user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_billing_account_user_permission_with_http_info(billing_account_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str billing_account_id: (required)
        :param Body2 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_account_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_billing_account_user_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'billing_account_id' is set
        if self.api_client.client_side_validation and ('billing_account_id' not in params or
                                                       params['billing_account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `billing_account_id` when calling `remove_billing_account_user_permission`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `remove_billing_account_user_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'billing_account_id' in params:
            path_params['billingAccountId'] = params['billing_account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/billing-accounts/{billingAccountId}/remove-user-permission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_data_center_user_permission(self, data_center_id, body, **kwargs):  # noqa: E501
        """Remove data center user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_data_center_user_permission(data_center_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :param Body4 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_data_center_user_permission_with_http_info(data_center_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_data_center_user_permission_with_http_info(data_center_id, body, **kwargs)  # noqa: E501
            return data

    def remove_data_center_user_permission_with_http_info(self, data_center_id, body, **kwargs):  # noqa: E501
        """Remove data center user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_data_center_user_permission_with_http_info(data_center_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_center_id: (required)
        :param Body4 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_center_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_data_center_user_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_center_id' is set
        if self.api_client.client_side_validation and ('data_center_id' not in params or
                                                       params['data_center_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_center_id` when calling `remove_data_center_user_permission`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `remove_data_center_user_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_center_id' in params:
            path_params['dataCenterId'] = params['data_center_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/data-centers/{dataCenterId}/remove-user-permission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_project_user_permission(self, project_id, body, **kwargs):  # noqa: E501
        """Remove project user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_project_user_permission(project_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param Body11 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_project_user_permission_with_http_info(project_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_project_user_permission_with_http_info(project_id, body, **kwargs)  # noqa: E501
            return data

    def remove_project_user_permission_with_http_info(self, project_id, body, **kwargs):  # noqa: E501
        """Remove project user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_project_user_permission_with_http_info(project_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param Body11 body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_project_user_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if self.api_client.client_side_validation and ('project_id' not in params or
                                                       params['project_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `project_id` when calling `remove_project_user_permission`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `remove_project_user_permission`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/projects/{projectId}/remove-user-permission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
