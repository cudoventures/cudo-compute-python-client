import cudo_compute as cudo
import os
import importlib.metadata

home = os.path.expanduser("~")


def client():
    configuration = cudo.Configuration()
    key, err = get_api_key()

    if err:
        return None, err

    configuration.api_key['Authorization'] = key
    # configuration.debug = True
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    configuration.host = "https://rest.compute.cudo.org"

    client = cudo.ApiClient(configuration)
    version = ''
    try:
        version = importlib.metadata.version('cudo-compute')
    except:
        pass

    client.user_agent = 'cudo-compute-python-client/' + version
    return client, None


def get_api_key():
    key_config, context_config, error = cudo.AuthConfig.load_config(home + '/.config/cudo/cudo.yml', "")
    if not error:
        return key_config['key'], None
    else:
        return None, error


def get_project_id():
    key_config, context_config, error = cudo.AuthConfig.load_config(home + '/.config/cudo/cudo.yml', "")
    if not error:
        if 'project' in context_config:
            return context_config['project'], None
        else:
            return None, Exception('No project set in configuration (cudo.yml)')
    else:
        return None, error


def project_id():
    p, e = get_project_id()
    if e is None:
        return p
    return ''


def project_id_throwable():
    p, e = get_project_id()
    if e is None:
        return p
    else:
        raise e


# APIs
def api_keys():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.APIKeysApi(c)


def disks():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.DisksApi(c)


def networks():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.NetworksApi(c)


def object_storage():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.ObjectStorageApi(c)


def permissions():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.PermissionsApi(c)


def projects():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.ProjectsApi(c)


def ssh_keys():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.SSHKeysApi(c)


def search():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.SearchApi(c)


def user():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.UserApi(c)


def virtual_machines():
    c, err = client()
    if err:
        raise Exception(err)
    return cudo.VirtualMachinesApi(c)
