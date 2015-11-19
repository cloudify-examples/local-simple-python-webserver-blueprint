import os
import sys
import subprocess

from cloudify import ctx


IS_WIN = os.name == 'nt'

port = ctx.node.properties['port']

webserver_cmd = [sys.executable, '-m', 'SimpleHTTPServer', str(port)]
if not IS_WIN:
    webserver_cmd.insert(0, 'nohup')

DN = open(os.devnull, 'wb')
ctx.logger.info('Running WebServer on port: {0}'.format(port))
process = subprocess.Popen(webserver_cmd, shell=False, stdout=DN, stderr=DN)

if not IS_WIN:
    del webserver_cmd[0]
    get_pid = ['pidof', '-s']
    get_pid.extend(webserver_cmd)
    pid = int(subprocess.check_output(get_pid))

ctx.logger.info('Setting `pid` runtime property: {0}'.format(pid))
ctx.instance.runtime_properties['pid'] = pid
