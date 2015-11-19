import os
import sys
import subprocess

from cloudify import ctx


IS_WIN = os.name == 'nt'
# is this needed?
IS_DARWIN = (sys.platform == 'darwin')
PORT = ctx.node.properties['port']


def run_server():
    webserver_cmd = [sys.executable, '-m', 'SimpleHTTPServer', str(PORT)]
    if not IS_WIN:
        webserver_cmd.insert(0, 'nohup')

    ctx.logger.info('Running WebServer locally on port: {0}'.format(PORT))
    dn = open(os.devnull, 'wb')
    process = subprocess.Popen(webserver_cmd, stdout=dn, stderr=dn)

    if not IS_WIN:
        del webserver_cmd[0]
        get_pid = ['pidof', '-s']
        get_pid.extend(webserver_cmd)
        return int(subprocess.check_output(get_pid))
    else:
        return process.pid


def set_pid(pid):
    ctx.logger.info('Setting `pid` runtime property: {0}'.format(pid))
    ctx.instance.runtime_properties['pid'] = pid


pid = run_server()
set_pid(pid)
