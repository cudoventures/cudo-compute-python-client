# Cudo Compute
To use this client install cudoctl and run ``./cudoctl init`` follow the steps to enter your API key and choose your project.  

Then when you call cudo_api in python it will grab your API key from the yaml file created by cudoctl.

```bash
pip install cudo-compute
```

To use the api key and project set in cudoctl command line tool:
```python


vm_api = cudo_api.virtual_machines()
vms = vm_api.list_vms(cudo_api.project_id())
```

If you don't want to use the automatic key you can supply your own, but you must also supply the project id manually too.
```python
from cudo_compute import cudo_api

api_key = "s8dhap8dha8a98a9e88ewe90w9e"
project = "my-project"    
vm_api = cudo_api.virtual_machines(api_key)
vms = vm_api.list_vms(project_id)
```

More examples of various api calls can be found in ``examples``. 



## Documentation for API Endpoints

How to create each API, methods are below:
```python
from cudo_compute import cudo_api

key_api = cudo_api.api_keys()
billing_api = cudo_api.billing()
dc_api = cudo_api.data_centers()
disk_api = cudo_api.disks()
mt_api = cudo_api.machine_types()
net_api = cudo_api.networks()
store_api = cudo_api.object_storage()
perm_api = cudo_api.permissions
projects_api = cudo_api.projects()
ssh_api = cudo_api.ssh_keys()
search_api = cudo_api.search()
vm_api = cudo_api.virtual_machines()
def_api = cudo_api.default()
```

All URIs are relative to *https://rest.compute.cudo.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIKeysApi* | [**delete_api_key**](docs/APIKeysApi.md#delete_api_key) | **DELETE** /v1/api-keys/{name} | Delete
*APIKeysApi* | [**generate_api_key**](docs/APIKeysApi.md#generate_api_key) | **POST** /v1/api-keys | Generate
*APIKeysApi* | [**list_api_keys**](docs/APIKeysApi.md#list_api_keys) | **GET** /v1/api-keys | List
*BillingApi* | [**create_billing_account**](docs/BillingApi.md#create_billing_account) | **POST** /v1/billing-accounts | Create a billing account
*BillingApi* | [**create_billing_account_credit_payment**](docs/BillingApi.md#create_billing_account_credit_payment) | **POST** /v1/billing-accounts/{id}/credit | Add credit to billing account
*BillingApi* | [**delete_billing_account**](docs/BillingApi.md#delete_billing_account) | **DELETE** /v1/billing-accounts/{id} | Delete billing account
*BillingApi* | [**get_billing_account**](docs/BillingApi.md#get_billing_account) | **GET** /v1/billing-accounts/{id} | Get a billing account
*BillingApi* | [**get_billing_account_details**](docs/BillingApi.md#get_billing_account_details) | **GET** /v1/billing-accounts/{id}/details | Get billing account details
*BillingApi* | [**get_billing_account_payment_methods**](docs/BillingApi.md#get_billing_account_payment_methods) | **GET** /v1/billing-accounts/{id}/payment-methods | Get payment methods
*BillingApi* | [**get_billing_account_setup_intent**](docs/BillingApi.md#get_billing_account_setup_intent) | **GET** /v1/billing-accounts/{id}/setup-intent | Get setup intent
*BillingApi* | [**get_billing_account_spend_details**](docs/BillingApi.md#get_billing_account_spend_details) | **GET** /v1/billing-accounts/{billingAccountId}/spend/details | Get spend details
*BillingApi* | [**list_billing_account_credit_balance_transactions**](docs/BillingApi.md#list_billing_account_credit_balance_transactions) | **GET** /v1/billing-accounts/{id}/credit-balance-transactions | List credit balance transactions on a billing account
*BillingApi* | [**list_billing_account_invoices**](docs/BillingApi.md#list_billing_account_invoices) | **GET** /v1/billing-accounts/invoices | List invoices
*BillingApi* | [**list_billing_account_transactions**](docs/BillingApi.md#list_billing_account_transactions) | **GET** /v1/billing-accounts/{id}/transactions | List transactions on a billing account
*BillingApi* | [**list_billing_accounts**](docs/BillingApi.md#list_billing_accounts) | **GET** /v1/billing-accounts | List billing accounts
*BillingApi* | [**list_outstanding_invoices**](docs/BillingApi.md#list_outstanding_invoices) | **GET** /v1/billing-accounts/invoices/outstanding | Get outstanding invoices
*BillingApi* | [**remove_billing_account_payment_method**](docs/BillingApi.md#remove_billing_account_payment_method) | **DELETE** /v1/billing-accounts/{id}/payment-methods/{paymentMethodId} | Remove payment method
*BillingApi* | [**set_billing_account_default_payment_method**](docs/BillingApi.md#set_billing_account_default_payment_method) | **POST** /v1/billing-accounts/{id}/payment-methods/{paymentMethodId}/set-default | Set default payment method
*BillingApi* | [**update_billing_account**](docs/BillingApi.md#update_billing_account) | **PATCH** /v1/billing-accounts/{billingAccount.id} | Update billing account
*DataCentersApi* | [**count_hosts**](docs/DataCentersApi.md#count_hosts) | **GET** /v1/data-centers/{dataCenterId}/host-count | Get host count
*DataCentersApi* | [**create_data_center**](docs/DataCentersApi.md#create_data_center) | **POST** /v1/data-centers | Create data center
*DataCentersApi* | [**delete_data_center**](docs/DataCentersApi.md#delete_data_center) | **DELETE** /v1/data-centers/{id} | Delete data center
*DataCentersApi* | [**get_data_center**](docs/DataCentersApi.md#get_data_center) | **GET** /v1/data-centers/{id} | Get data center
*DataCentersApi* | [**get_data_center_live_utilization**](docs/DataCentersApi.md#get_data_center_live_utilization) | **GET** /v1/data-centers/{id}/live-utilization | Get live utilization
*DataCentersApi* | [**get_data_center_revenue_by_resource**](docs/DataCentersApi.md#get_data_center_revenue_by_resource) | **GET** /v1/data-centers/{id}/revenue-by-resource | Get revenue by resource
*DataCentersApi* | [**get_data_center_revenue_time_series**](docs/DataCentersApi.md#get_data_center_revenue_time_series) | **GET** /v1/data-centers/{id}/revenue | Get revenue time series
*DataCentersApi* | [**list_clusters**](docs/DataCentersApi.md#list_clusters) | **GET** /v1/data-centers/{dataCenterId}/clusters | List clusters
*DataCentersApi* | [**list_data_centers**](docs/DataCentersApi.md#list_data_centers) | **GET** /v1/data-centers | List data centers
*DataCentersApi* | [**list_hosts**](docs/DataCentersApi.md#list_hosts) | **GET** /v1/data-centers/{dataCenterId}/hosts | List hosts
*DataCentersApi* | [**update_data_center**](docs/DataCentersApi.md#update_data_center) | **PATCH** /v1/data-centers/{dataCenter.id} | Update data center
*DisksApi* | [**attach_storage_disk**](docs/DisksApi.md#attach_storage_disk) | **PATCH** /v1/projects/{projectId}/disk/{id}/attach | Attach storage disk to VM
*DisksApi* | [**create_disk_snapshot**](docs/DisksApi.md#create_disk_snapshot) | **POST** /v1/projects/{projectId}/disks/{id}/snapshots | Create Disk Snapshot
*DisksApi* | [**create_storage_disk**](docs/DisksApi.md#create_storage_disk) | **POST** /v1/projects/{projectId}/disks | Create storage disk
*DisksApi* | [**delete_disk_snapshot**](docs/DisksApi.md#delete_disk_snapshot) | **DELETE** /v1/projects/{projectId}/disks/{id}/snapshots | Delete Disk Snapshots
*DisksApi* | [**delete_storage_disk**](docs/DisksApi.md#delete_storage_disk) | **DELETE** /v1/projects/{projectId}/disks/{id} | Delete storage disk
*DisksApi* | [**detach_storage_disk**](docs/DisksApi.md#detach_storage_disk) | **PUT** /v1/projects/{projectId}/disk/{id}/detach | Detach storage disk from VM
*DisksApi* | [**get_disk**](docs/DisksApi.md#get_disk) | **GET** /v1/projects/{projectId}/disks/{id} | List disks
*DisksApi* | [**list_disk_snapshots**](docs/DisksApi.md#list_disk_snapshots) | **GET** /v1/projects/{projectId}/disks/{id}/snapshots | List Disk Snapshots
*DisksApi* | [**list_disks**](docs/DisksApi.md#list_disks) | **GET** /v1/projects/{projectId}/disks | List disks
*DisksApi* | [**revert_disk**](docs/DisksApi.md#revert_disk) | **POST** /v1/projects/{projectId}/disks/{id}/revert | Revert Disk to Snapshot
*MachineTypesApi* | [**get_machine_type**](docs/MachineTypesApi.md#get_machine_type) | **GET** /v1/data-centers/{dataCenterId}/machine-types/{machineType} | Get a machine type in a data center
*MachineTypesApi* | [**get_machine_type_live_utilization**](docs/MachineTypesApi.md#get_machine_type_live_utilization) | **GET** /v1/data-centers/{dataCenterId}/machine-types/{machineType}/live-utilization | Get the utilization for a machine type in a data center
*MachineTypesApi* | [**list_machine_types**](docs/MachineTypesApi.md#list_machine_types) | **GET** /v1/data-centers/{dataCenterId}/machine-types | List machine types for a data center
*NetworksApi* | [**create_network**](docs/NetworksApi.md#create_network) | **POST** /v1/projects/{projectId}/networks | Create network
*NetworksApi* | [**create_security_group**](docs/NetworksApi.md#create_security_group) | **POST** /v1/projects/{securityGroup.projectId}/networks/security-groups | Create security group
*NetworksApi* | [**delete_network**](docs/NetworksApi.md#delete_network) | **DELETE** /v1/projects/{projectId}/networks/{id} | Delete network
*NetworksApi* | [**delete_security_group**](docs/NetworksApi.md#delete_security_group) | **DELETE** /v1/projects/{projectId}/networks/security-groups/{id} | Delete security group
*NetworksApi* | [**get_network**](docs/NetworksApi.md#get_network) | **GET** /v1/projects/{projectId}/networks/{id} | Get network
*NetworksApi* | [**get_security_group**](docs/NetworksApi.md#get_security_group) | **GET** /v1/projects/{projectId}/networks/security-groups/{id} | Get a security group
*NetworksApi* | [**list_networks**](docs/NetworksApi.md#list_networks) | **GET** /v1/projects/{projectId}/networks | List networks
*NetworksApi* | [**list_security_groups**](docs/NetworksApi.md#list_security_groups) | **GET** /v1/projects/{projectId}/networks/security-groups | List security groups
*NetworksApi* | [**start_network**](docs/NetworksApi.md#start_network) | **POST** /v1/projects/{projectId}/networks/{id}/start | Start network
*NetworksApi* | [**stop_network**](docs/NetworksApi.md#stop_network) | **POST** /v1/projects/{projectId}/networks/{id}/stop | Stop network
*NetworksApi* | [**update_security_group**](docs/NetworksApi.md#update_security_group) | **PATCH** /v1/projects/{securityGroup.projectId}/networks/security-groups/{securityGroup.id} | Update security group
*ObjectStorageApi* | [**activate**](docs/ObjectStorageApi.md#activate) | **POST** /v1/projects/{projectId}/object-storage/activate/{dataCenterId} | Allow the use of S3 compatible storage in a project
*ObjectStorageApi* | [**create_object_storage_user**](docs/ObjectStorageApi.md#create_object_storage_user) | **POST** /v1/projects/{projectId}/object-storage/users/{dataCenterId} | Create user that stores keys for storage buckets
*ObjectStorageApi* | [**delete_object_storage_key**](docs/ObjectStorageApi.md#delete_object_storage_key) | **DELETE** /v1/projects/{projectId}/object-storage/users/{dataCenterId}/{id}/keys/{accessKey} | Delete object storage user key
*ObjectStorageApi* | [**delete_object_storage_user**](docs/ObjectStorageApi.md#delete_object_storage_user) | **DELETE** /v1/projects/{projectId}/object-storage/users/{dataCenterId}/{id} | Delete object storage user
*ObjectStorageApi* | [**generate_object_storage_key**](docs/ObjectStorageApi.md#generate_object_storage_key) | **POST** /v1/projects/{projectId}/object-storage/users/{dataCenterId}/{id} | Generate access key for storage buckets
*ObjectStorageApi* | [**get_object_storage_bucket**](docs/ObjectStorageApi.md#get_object_storage_bucket) | **GET** /v1/projects/{projectId}/object-storage/buckets/{dataCenterId}/{id} | Get details for a bucket
*ObjectStorageApi* | [**get_object_storage_session_key**](docs/ObjectStorageApi.md#get_object_storage_session_key) | **GET** /v1/projects/{projectId}/object-storage/session-key/{dataCenterId} | Generate temporary key for storage bucket access
*ObjectStorageApi* | [**get_object_storage_user**](docs/ObjectStorageApi.md#get_object_storage_user) | **GET** /v1/projects/{projectId}/object-storage/users/{dataCenterId}/{userId} | Get details about an object storage user
*ObjectStorageApi* | [**list_object_storage_buckets**](docs/ObjectStorageApi.md#list_object_storage_buckets) | **GET** /v1/projects/{projectId}/object-storage/buckets | List buckets
*ObjectStorageApi* | [**list_object_storage_users**](docs/ObjectStorageApi.md#list_object_storage_users) | **GET** /v1/projects/{projectId}/object-storage/users | List storage users
*PermissionsApi* | [**add_billing_account_user_permission**](docs/PermissionsApi.md#add_billing_account_user_permission) | **POST** /v1/billing-accounts/{billingAccountId}/add-user-permission | Add billing account user
*PermissionsApi* | [**add_data_center_user_permission**](docs/PermissionsApi.md#add_data_center_user_permission) | **POST** /v1/data-centers/{dataCenterId}/add-user-permission | Add data center user
*PermissionsApi* | [**add_project_user_permission**](docs/PermissionsApi.md#add_project_user_permission) | **POST** /v1/projects/{projectId}/add-user-permission | Add project user
*PermissionsApi* | [**list_user_permissions**](docs/PermissionsApi.md#list_user_permissions) | **GET** /v1/auth/permissions | List
*PermissionsApi* | [**remove_billing_account_user_permission**](docs/PermissionsApi.md#remove_billing_account_user_permission) | **POST** /v1/billing-accounts/{billingAccountId}/remove-user-permission | Remove billing account user
*PermissionsApi* | [**remove_data_center_user_permission**](docs/PermissionsApi.md#remove_data_center_user_permission) | **POST** /v1/data-centers/{dataCenterId}/remove-user-permission | Remove data center user
*PermissionsApi* | [**remove_project_user_permission**](docs/PermissionsApi.md#remove_project_user_permission) | **POST** /v1/projects/{projectId}/remove-user-permission | Remove project user
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /v1/projects | Create
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /v1/projects/{id} | Delete
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /v1/projects/{id} | Get
*ProjectsApi* | [**list_project_ssh_keys**](docs/ProjectsApi.md#list_project_ssh_keys) | **GET** /v1/project/{projectId}/ssh-keys | List SSH keys
*ProjectsApi* | [**list_projects**](docs/ProjectsApi.md#list_projects) | **GET** /v1/projects | List
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PATCH** /v1/projects/{project.id} | Update
*SSHKeysApi* | [**create_ssh_key**](docs/SSHKeysApi.md#create_ssh_key) | **POST** /v1/ssh-keys | Create
*SSHKeysApi* | [**delete_ssh_key**](docs/SSHKeysApi.md#delete_ssh_key) | **DELETE** /v1/ssh-keys/{id} | Delete
*SSHKeysApi* | [**get_ssh_key**](docs/SSHKeysApi.md#get_ssh_key) | **GET** /v1/ssh-keys/{id} | Get
*SSHKeysApi* | [**list_ssh_keys**](docs/SSHKeysApi.md#list_ssh_keys) | **GET** /v1/ssh-keys | List
*SearchApi* | [**list_regions**](docs/SearchApi.md#list_regions) | **GET** /v1/regions | Regions
*UserApi* | [**create_identity_verification_session**](docs/UserApi.md#create_identity_verification_session) | **GET** /v1/auth/create-identity-verification-session | Get identity verification session
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /v1/auth | Delete
*UserApi* | [**get**](docs/UserApi.md#get) | **GET** /v1/auth | Get
*VirtualMachinesApi* | [**attach_security_group**](docs/VirtualMachinesApi.md#attach_security_group) | **PATCH** /v1/projects/{projectId}/vm/{id}/security-group/attach | Attach security group to VM
*VirtualMachinesApi* | [**connect_vm**](docs/VirtualMachinesApi.md#connect_vm) | **GET** /v1/projects/{projectId}/vms/{id}/connect | Connect via VNC
*VirtualMachinesApi* | [**count_vms**](docs/VirtualMachinesApi.md#count_vms) | **GET** /v1/projects/{projectId}/count-vms | Count
*VirtualMachinesApi* | [**create_private_vm_image**](docs/VirtualMachinesApi.md#create_private_vm_image) | **POST** /v1/projects/{projectId}/images | Create private VM image
*VirtualMachinesApi* | [**create_vm**](docs/VirtualMachinesApi.md#create_vm) | **POST** /v1/projects/{projectId}/vm | Create virtual machine
*VirtualMachinesApi* | [**delete_private_vm_image**](docs/VirtualMachinesApi.md#delete_private_vm_image) | **DELETE** /v1/projects/{projectId}/images/{id} | Delete private VM image
*VirtualMachinesApi* | [**detach_security_group**](docs/VirtualMachinesApi.md#detach_security_group) | **PATCH** /v1/projects/{projectId}/vm/{id}/security-group/detach | Attach security group to VM
*VirtualMachinesApi* | [**get_private_vm_image**](docs/VirtualMachinesApi.md#get_private_vm_image) | **GET** /v1/projects/{projectId}/images/{id} | Get private VM image
*VirtualMachinesApi* | [**get_vm**](docs/VirtualMachinesApi.md#get_vm) | **GET** /v1/projects/{projectId}/vms/{id} | Get
*VirtualMachinesApi* | [**list_private_vm_images**](docs/VirtualMachinesApi.md#list_private_vm_images) | **GET** /v1/projects/{projectId}/images | List private VM images
*VirtualMachinesApi* | [**list_public_vm_images**](docs/VirtualMachinesApi.md#list_public_vm_images) | **GET** /v1/vms/public-images | List public VM images
*VirtualMachinesApi* | [**list_vm_data_centers**](docs/VirtualMachinesApi.md#list_vm_data_centers) | **GET** /v1/vms/data-centers | List data centers
*VirtualMachinesApi* | [**list_vm_disks**](docs/VirtualMachinesApi.md#list_vm_disks) | **GET** /v1/projects/{projectId}/vms/{id}/disks | List disks attached to VM
*VirtualMachinesApi* | [**list_vm_gpu_models**](docs/VirtualMachinesApi.md#list_vm_gpu_models) | **GET** /v1/vms/gpu-models | List GPU models
*VirtualMachinesApi* | [**list_vm_machine_types2**](docs/VirtualMachinesApi.md#list_vm_machine_types2) | **GET** /v1/vms/machine-types-2 | List machine types v2
*VirtualMachinesApi* | [**list_vms**](docs/VirtualMachinesApi.md#list_vms) | **GET** /v1/projects/{projectId}/vms | List
*VirtualMachinesApi* | [**monitor_vm**](docs/VirtualMachinesApi.md#monitor_vm) | **GET** /v1/projects/{projectId}/vms/{id}/monitor | Monitor
*VirtualMachinesApi* | [**reboot_vm**](docs/VirtualMachinesApi.md#reboot_vm) | **POST** /v1/projects/{projectId}/vms/{id}/reboot | Reboot
*VirtualMachinesApi* | [**resize_vm**](docs/VirtualMachinesApi.md#resize_vm) | **POST** /v1/projects/{projectId}/vms/{id}/resize | Resize vCPU and memory of VM
*VirtualMachinesApi* | [**resize_vm_disk**](docs/VirtualMachinesApi.md#resize_vm_disk) | **PATCH** /v1/projects/{projectId}/vms/{id}/disks | Resize a VM&#39;s disk
*VirtualMachinesApi* | [**start_vm**](docs/VirtualMachinesApi.md#start_vm) | **POST** /v1/projects/{projectId}/vms/{id}/start | Start
*VirtualMachinesApi* | [**stop_vm**](docs/VirtualMachinesApi.md#stop_vm) | **POST** /v1/projects/{projectId}/vms/{id}/stop | Stop
*VirtualMachinesApi* | [**terminate_vm**](docs/VirtualMachinesApi.md#terminate_vm) | **POST** /v1/projects/{projectId}/vms/{id}/terminate | Terminate
*VirtualMachinesApi* | [**update_private_vm_image**](docs/VirtualMachinesApi.md#update_private_vm_image) | **POST** /v1/projects/{projectId}/images/{id} | Update private VM image
*VirtualMachinesApi* | [**update_vm_metadata**](docs/VirtualMachinesApi.md#update_vm_metadata) | **POST** /v1/projects/{projectId}/vm/{id}/metadata | Update VM metadata
*DefaultApi* | [**get_data_center_commitment_schedule**](docs/DefaultApi.md#get_data_center_commitment_schedule) | **GET** /v1/data-centers/{dataCenterId}/commitment-schedule | 
*DefaultApi* | [**get_data_center_commitment_time_series**](docs/DefaultApi.md#get_data_center_commitment_time_series) | **GET** /v1/data-centers/{dataCenterId}/commitment-time-series | 
*DefaultApi* | [**list_billing_account_projects**](docs/DefaultApi.md#list_billing_account_projects) | **GET** /v1/billing-accounts/{id}/projects | 
*DefaultApi* | [**list_data_center_machine_type_prices**](docs/DefaultApi.md#list_data_center_machine_type_prices) | **GET** /v1/data-centers/{dataCenterId}/machine-type-prices | 
*DefaultApi* | [**list_vm_machine_types**](docs/DefaultApi.md#list_vm_machine_types) | **GET** /v1/vms/machine-types | 
*DefaultApi* | [**search_resources**](docs/DefaultApi.md#search_resources) | **GET** /v1/resources/search | 
*DefaultApi* | [**track**](docs/DefaultApi.md#track) | **POST** /v1/auth/track | 
*DefaultApi* | [**update_vm_expire_time**](docs/DefaultApi.md#update_vm_expire_time) | **POST** /v1/projects/{projectId}/vm/{id}/expire-time | 
*DefaultApi* | [**update_vm_password**](docs/DefaultApi.md#update_vm_password) | **POST** /v1/projects/{projectId}/vm/{id}/password | 


## Documentation For Models

 - [ActivateBody](docs/ActivateBody.md)
 - [AddBillingAccountUserPermissionBody](docs/AddBillingAccountUserPermissionBody.md)
 - [AddDataCenterUserPermissionBody](docs/AddDataCenterUserPermissionBody.md)
 - [AddProjectUserPermissionBody](docs/AddProjectUserPermissionBody.md)
 - [ApiKey](docs/ApiKey.md)
 - [AttachSecurityGroupResponse](docs/AttachSecurityGroupResponse.md)
 - [AttachStorageDiskResponse](docs/AttachStorageDiskResponse.md)
 - [BillingAccount](docs/BillingAccount.md)
 - [BillingAccountPaymentMethod](docs/BillingAccountPaymentMethod.md)
 - [BillingAccountPaymentMethods](docs/BillingAccountPaymentMethods.md)
 - [BillingAccountProject](docs/BillingAccountProject.md)
 - [BillingAccountResult](docs/BillingAccountResult.md)
 - [BillingAccountSetupIntent](docs/BillingAccountSetupIntent.md)
 - [BillingAccountSpendRow](docs/BillingAccountSpendRow.md)
 - [BillingAccountState](docs/BillingAccountState.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [Charge](docs/Charge.md)
 - [Cluster](docs/Cluster.md)
 - [CommitmentTerm](docs/CommitmentTerm.md)
 - [ConnectVMResponse](docs/ConnectVMResponse.md)
 - [CountHostsResponse](docs/CountHostsResponse.md)
 - [CountVMsResponse](docs/CountVMsResponse.md)
 - [CpuTopology](docs/CpuTopology.md)
 - [CreateBillingAccountCreditPaymentResponse](docs/CreateBillingAccountCreditPaymentResponse.md)
 - [CreateBillingAccountRequest](docs/CreateBillingAccountRequest.md)
 - [CreateDiskSnapshotBody](docs/CreateDiskSnapshotBody.md)
 - [CreateDiskSnapshotResponse](docs/CreateDiskSnapshotResponse.md)
 - [CreateNetworkBody](docs/CreateNetworkBody.md)
 - [CreateNetworkResponse](docs/CreateNetworkResponse.md)
 - [CreateObjectStorageUserBody](docs/CreateObjectStorageUserBody.md)
 - [CreatePrivateVMImageResponse](docs/CreatePrivateVMImageResponse.md)
 - [CreateSecurityGroupResponse](docs/CreateSecurityGroupResponse.md)
 - [CreateStorageDiskBody](docs/CreateStorageDiskBody.md)
 - [CreateStorageDiskResponse](docs/CreateStorageDiskResponse.md)
 - [CreateVMBody](docs/CreateVMBody.md)
 - [CreateVMRequestNIC](docs/CreateVMRequestNIC.md)
 - [CreateVMResponse](docs/CreateVMResponse.md)
 - [CreditBalanceRecharge](docs/CreditBalanceRecharge.md)
 - [CreditBalanceTransaction](docs/CreditBalanceTransaction.md)
 - [DataCenterCommitment](docs/DataCenterCommitment.md)
 - [DataCenterCommitmentInterval](docs/DataCenterCommitmentInterval.md)
 - [DataCenterMachineType](docs/DataCenterMachineType.md)
 - [DataCenterRevenueResource](docs/DataCenterRevenueResource.md)
 - [DataCenterTimeRevenue](docs/DataCenterTimeRevenue.md)
 - [Decimal](docs/Decimal.md)
 - [DeleteDiskSnapshotResponse](docs/DeleteDiskSnapshotResponse.md)
 - [DeleteNetworkResponse](docs/DeleteNetworkResponse.md)
 - [DeletePrivateVMImageResponse](docs/DeletePrivateVMImageResponse.md)
 - [DeleteSecurityGroupResponse](docs/DeleteSecurityGroupResponse.md)
 - [DeleteStorageDiskResponse](docs/DeleteStorageDiskResponse.md)
 - [DetachSecurityGroupResponse](docs/DetachSecurityGroupResponse.md)
 - [DetachStorageDiskResponse](docs/DetachStorageDiskResponse.md)
 - [Disk](docs/Disk.md)
 - [DiskResult](docs/DiskResult.md)
 - [DiskState](docs/DiskState.md)
 - [DiskStorageClass](docs/DiskStorageClass.md)
 - [DiskStoragePriceHr](docs/DiskStoragePriceHr.md)
 - [DiskType](docs/DiskType.md)
 - [GenerateApiKeyRequest](docs/GenerateApiKeyRequest.md)
 - [GetBillingAccountDetailsResponse](docs/GetBillingAccountDetailsResponse.md)
 - [GetBillingAccountSpendDetailsResponse](docs/GetBillingAccountSpendDetailsResponse.md)
 - [GetDataCenterCommitmentScheduleResponse](docs/GetDataCenterCommitmentScheduleResponse.md)
 - [GetDataCenterCommitmentTimeSeriesRequestInterval](docs/GetDataCenterCommitmentTimeSeriesRequestInterval.md)
 - [GetDataCenterCommitmentTimeSeriesResponse](docs/GetDataCenterCommitmentTimeSeriesResponse.md)
 - [GetDataCenterLiveUtilizationResponse](docs/GetDataCenterLiveUtilizationResponse.md)
 - [GetDataCenterRevenueByResourceResponse](docs/GetDataCenterRevenueByResourceResponse.md)
 - [GetDataCenterRevenueTimeSeriesRequestInterval](docs/GetDataCenterRevenueTimeSeriesRequestInterval.md)
 - [GetDataCenterRevenueTimeSeriesResponse](docs/GetDataCenterRevenueTimeSeriesResponse.md)
 - [GetDiskResponse](docs/GetDiskResponse.md)
 - [GetMachineTypeLiveUtilizationResponse](docs/GetMachineTypeLiveUtilizationResponse.md)
 - [GetMachineTypeResponse](docs/GetMachineTypeResponse.md)
 - [GetNetworkResponse](docs/GetNetworkResponse.md)
 - [GetObjectStorageSessionKeyResponse](docs/GetObjectStorageSessionKeyResponse.md)
 - [GetPrivateVMImageResponse](docs/GetPrivateVMImageResponse.md)
 - [GetResponse](docs/GetResponse.md)
 - [GetSecurityGroupResponse](docs/GetSecurityGroupResponse.md)
 - [GetVMResponse](docs/GetVMResponse.md)
 - [GpuModel](docs/GpuModel.md)
 - [Host](docs/Host.md)
 - [IdentityVerificationSession](docs/IdentityVerificationSession.md)
 - [Image](docs/Image.md)
 - [ImageResult](docs/ImageResult.md)
 - [Invoice](docs/Invoice.md)
 - [LastPaymentError](docs/LastPaymentError.md)
 - [ListApiKeysResponse](docs/ListApiKeysResponse.md)
 - [ListBillingAccountCreditBalanceTransactionsResponse](docs/ListBillingAccountCreditBalanceTransactionsResponse.md)
 - [ListBillingAccountInvoicesResponse](docs/ListBillingAccountInvoicesResponse.md)
 - [ListBillingAccountProjectsResponse](docs/ListBillingAccountProjectsResponse.md)
 - [ListBillingAccountTransactionsResponse](docs/ListBillingAccountTransactionsResponse.md)
 - [ListBillingAccountsResponse](docs/ListBillingAccountsResponse.md)
 - [ListClustersResponse](docs/ListClustersResponse.md)
 - [ListDataCenterMachineTypePricesResponse](docs/ListDataCenterMachineTypePricesResponse.md)
 - [ListDataCenterMachineTypePricesResponseMachineTypePrice](docs/ListDataCenterMachineTypePricesResponseMachineTypePrice.md)
 - [ListDataCentersResponse](docs/ListDataCentersResponse.md)
 - [ListDiskSnapshotsResponse](docs/ListDiskSnapshotsResponse.md)
 - [ListDisksResponse](docs/ListDisksResponse.md)
 - [ListHostsResponse](docs/ListHostsResponse.md)
 - [ListMachineTypesResponse](docs/ListMachineTypesResponse.md)
 - [ListNetworksResponse](docs/ListNetworksResponse.md)
 - [ListObjectStorageBucketsResponse](docs/ListObjectStorageBucketsResponse.md)
 - [ListObjectStorageUsersResponse](docs/ListObjectStorageUsersResponse.md)
 - [ListOutstandingInvoicesResponse](docs/ListOutstandingInvoicesResponse.md)
 - [ListPrivateVMImagesResponse](docs/ListPrivateVMImagesResponse.md)
 - [ListProjectSshKeysResponse](docs/ListProjectSshKeysResponse.md)
 - [ListProjectsResponse](docs/ListProjectsResponse.md)
 - [ListPublicVMImagesResponse](docs/ListPublicVMImagesResponse.md)
 - [ListRegionsResponse](docs/ListRegionsResponse.md)
 - [ListSecurityGroupsResponse](docs/ListSecurityGroupsResponse.md)
 - [ListSshKeysResponse](docs/ListSshKeysResponse.md)
 - [ListUserPermissionsResponse](docs/ListUserPermissionsResponse.md)
 - [ListVMDataCentersResponse](docs/ListVMDataCentersResponse.md)
 - [ListVMDisksResponse](docs/ListVMDisksResponse.md)
 - [ListVMGpuModelsResponse](docs/ListVMGpuModelsResponse.md)
 - [ListVMMachineTypes2Response](docs/ListVMMachineTypes2Response.md)
 - [ListVMMachineTypes2ResponseVMMachineType](docs/ListVMMachineTypes2ResponseVMMachineType.md)
 - [ListVMMachineTypesResponse](docs/ListVMMachineTypesResponse.md)
 - [ListVMMachineTypesResponseVMMachineType](docs/ListVMMachineTypesResponseVMMachineType.md)
 - [ListVMsResponse](docs/ListVMsResponse.md)
 - [MonitorVMResponse](docs/MonitorVMResponse.md)
 - [Network](docs/Network.md)
 - [NetworkPriceHr](docs/NetworkPriceHr.md)
 - [NetworkResult](docs/NetworkResult.md)
 - [NetworkState](docs/NetworkState.md)
 - [ObjectStorageBucket](docs/ObjectStorageBucket.md)
 - [ObjectStorageKey](docs/ObjectStorageKey.md)
 - [ObjectStorageUser](docs/ObjectStorageUser.md)
 - [Package](docs/Package.md)
 - [PaymentIntent](docs/PaymentIntent.md)
 - [PaymentMethodCard](docs/PaymentMethodCard.md)
 - [PaymentMethodPaypal](docs/PaymentMethodPaypal.md)
 - [PaymentTerms](docs/PaymentTerms.md)
 - [Point](docs/Point.md)
 - [PrivateImage](docs/PrivateImage.md)
 - [Profile](docs/Profile.md)
 - [Project](docs/Project.md)
 - [ProjectResult](docs/ProjectResult.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RebootVMResponse](docs/RebootVMResponse.md)
 - [Region](docs/Region.md)
 - [RegionDataCenter](docs/RegionDataCenter.md)
 - [RemoveBillingAccountPaymentMethodResponse](docs/RemoveBillingAccountPaymentMethodResponse.md)
 - [RemoveBillingAccountUserPermissionBody](docs/RemoveBillingAccountUserPermissionBody.md)
 - [RemoveDataCenterUserPermissionBody](docs/RemoveDataCenterUserPermissionBody.md)
 - [RemoveProjectUserPermissionBody](docs/RemoveProjectUserPermissionBody.md)
 - [ResizeVMDiskResponse](docs/ResizeVMDiskResponse.md)
 - [ResizeVMResponse](docs/ResizeVMResponse.md)
 - [Result](docs/Result.md)
 - [RevertDiskResponse](docs/RevertDiskResponse.md)
 - [Role](docs/Role.md)
 - [Rule](docs/Rule.md)
 - [RuleProtocol](docs/RuleProtocol.md)
 - [RuleRuleType](docs/RuleRuleType.md)
 - [SearchResourcesResponse](docs/SearchResourcesResponse.md)
 - [SecurityGroup](docs/SecurityGroup.md)
 - [SecurityGroup1](docs/SecurityGroup1.md)
 - [SecurityGroupRule](docs/SecurityGroupRule.md)
 - [SecurityGroupRuleProtocol](docs/SecurityGroupRuleProtocol.md)
 - [SecurityGroupRuleRuleType](docs/SecurityGroupRuleRuleType.md)
 - [SetBillingAccountDefaultPaymentMethodResponse](docs/SetBillingAccountDefaultPaymentMethodResponse.md)
 - [Snapshot](docs/Snapshot.md)
 - [SshKey](docs/SshKey.md)
 - [SshKeySource](docs/SshKeySource.md)
 - [StartNetworkResponse](docs/StartNetworkResponse.md)
 - [StartVMResponse](docs/StartVMResponse.md)
 - [Status](docs/Status.md)
 - [StopNetworkResponse](docs/StopNetworkResponse.md)
 - [StopVMResponse](docs/StopVMResponse.md)
 - [StripeCustomer](docs/StripeCustomer.md)
 - [SyncResponse](docs/SyncResponse.md)
 - [Task](docs/Task.md)
 - [TaxId](docs/TaxId.md)
 - [TerminateVMResponse](docs/TerminateVMResponse.md)
 - [TrackRequest](docs/TrackRequest.md)
 - [Transaction](docs/Transaction.md)
 - [Unit](docs/Unit.md)
 - [UpdateBillingAccountBody](docs/UpdateBillingAccountBody.md)
 - [UpdateBillingAccountBodyBillingAccount](docs/UpdateBillingAccountBodyBillingAccount.md)
 - [UpdateDataCenterBody](docs/UpdateDataCenterBody.md)
 - [UpdateDataCenterBodyDataCenter](docs/UpdateDataCenterBodyDataCenter.md)
 - [UpdateHostResponse](docs/UpdateHostResponse.md)
 - [UpdateImageResponse](docs/UpdateImageResponse.md)
 - [UpdateNetResponse](docs/UpdateNetResponse.md)
 - [UpdatePrivateVMImageResponse](docs/UpdatePrivateVMImageResponse.md)
 - [UpdateProjectBody](docs/UpdateProjectBody.md)
 - [UpdateProjectBodyProject](docs/UpdateProjectBodyProject.md)
 - [UpdateSecurityGroupResponse](docs/UpdateSecurityGroupResponse.md)
 - [UpdateVMExpireTimeBody](docs/UpdateVMExpireTimeBody.md)
 - [UpdateVMExpireTimeResponse](docs/UpdateVMExpireTimeResponse.md)
 - [UpdateVMMetadataBody](docs/UpdateVMMetadataBody.md)
 - [UpdateVMMetadataResponse](docs/UpdateVMMetadataResponse.md)
 - [UpdateVMPasswordBody](docs/UpdateVMPasswordBody.md)
 - [UpdateVMPasswordResponse](docs/UpdateVMPasswordResponse.md)
 - [UpdateVMResponse](docs/UpdateVMResponse.md)
 - [UserPermission](docs/UserPermission.md)
 - [V1DataCenter](docs/V1DataCenter.md)
 - [V1VRouterSize](docs/V1VRouterSize.md)
 - [VM](docs/VM.md)
 - [VMDataCenter](docs/VMDataCenter.md)
 - [VMDataCenterStorageClass](docs/VMDataCenterStorageClass.md)
 - [VMDataCenterVRouterSize](docs/VMDataCenterVRouterSize.md)
 - [VMMachineTypeMachineTypePrice](docs/VMMachineTypeMachineTypePrice.md)
 - [VMMonitoringItem](docs/VMMonitoringItem.md)
 - [VMNIC](docs/VMNIC.md)
 - [VMPrice](docs/VMPrice.md)
 - [VirtualMachineResult](docs/VirtualMachineResult.md)
 - [VmState](docs/VmState.md)




# Advanced Users / Development
The code is generated by swagger codegen cli.

Most code is generated in github actions see .github/workflows the generated code is put into a /src/cudo_compute directory
The code gets modified and the helpers get copied in from /helpers.

``./codegen.sh`` generates docs directory with source code and documentation.

If you wish to customise how the API key or project is selected see the code in the helpers directory.

Install the latest test version:
```shell
pip install --upgrade --index-url https://test.pypi.org/simple/ cudo-compute
```