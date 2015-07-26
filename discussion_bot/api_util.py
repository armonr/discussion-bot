import socket
import errno
import urllib
import requests
from discussion_bot import settings
from discussion_bot.settings import SLACK_TOKEN, SLACK_CHANNEL, SLACK_BOT_USERNAME


def create_content(api_url, site_id, content_type, content_data, user_id,
                   container_type=None, container_id=None):
    """
    Creates content for given site and of given type authored by user_id
    """
    path = get_write_path(site_id, content_type, container_type, container_id)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/hal+json',
               'X-Wikia-UserId': user_id}
    return write_content(path, api_url, content_data, headers=headers)


def write_content(path, api_url, body, headers={}):
    return http_request('{api_url}{path}'.format(api_url=api_url, path=path),
                        method='POST', body=body, headers=headers)


def http_request(url, method='GET', body=None, headers={}):
    try:
        if method == 'GET':
            resp = requests.get(url, headers=headers)
        elif method == 'POST':
            resp = requests.post(url, body, headers=headers)
        elif method == 'PUT':
            resp = requests.put(url, body, headers=headers)
        elif method == 'DELETE':
            resp = requests.delete(url, headers=headers)
        else:
            raise Exception(errno.ENOTSUP, 'HTTP method not supported!')
        status = resp.status_code
        reason = resp.reason
        check_response(status, reason)

        payload = resp.text
    except socket.gaierror as err:
        raise Exception(
            err.errno, "Possible network/DNS error connecting %s" % url)
    except socket.error as err:
        if err.errno != errno.ECONNREFUSED:
            raise err
        raise Exception(err.errno, "%s is unavailable" % url)

    return status, reason, payload


def get_write_path(site_id, content_type, container_type=None, container_id=None):
    if container_id is not None and content_type is not None:
        path = '/{site_id}/{container_type}s/{container_id}/{content_type}s'.format(
            site_id=site_id, container_type=container_type, container_id=container_id,
            content_type=content_type)
    else:
        path = '/{site_id}/{content_type}s'.format(site_id=site_id, content_type=content_type)
    return path


def check_response(status, reason):
    if status >= 400:
        raise Exception(status, reason)


def api_url():
    scheme, host, port, path = discussion_api_location()
    if port == 80:
        port = ''
    else:
        port = ':{port}'.format(port=port)
    x = '{scheme}{host}{port}{path}'.format(scheme=scheme, host=host, port=port, path=path)
    return x


def discussion_api_location():
    """
    Returns Discussion API's host, port, path tuple
    """
    scheme = settings.DISCUSSION_API_SCHEME
    host = settings.DISCUSSION_API_HOST
    port = int(settings.DISCUSSION_API_PORT)
    api_path = settings.DISCUSSION_API_PATH
    return scheme, host, port, api_path


def slack_post(text):
    if SLACK_TOKEN:
        params = {'token': SLACK_TOKEN, 'channel': SLACK_CHANNEL, 'text': text,
                  'username': SLACK_BOT_USERNAME}
        return requests.get(
            'https://slack.com/api/chat.postMessage?{params}'.format(params=urllib.urlencode(params)))
    else:
        print 'Add a Slack token in settings to also get bot posts on the slack channel'
