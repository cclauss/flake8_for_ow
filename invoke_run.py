import json
import os
import subprocess
import sys

class invoke(object):
    def run(self, args, env):
        def error(msg):
            # fall through (exception and else case are handled the same way)
            sys.stdout.write('%s\n' % msg)
            return (502, {'error': 'The action did not return a dictionary.'})

        try:
            input = json.dumps(args)
            p = subprocess.Popen(
                [self.binary, input],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env)
        except Exception as e:
            return error(e)

        # run the process and wait until it completes.
        # stdout/stderr will always be set because we passed PIPEs to Popen
        (o, e) = p.communicate()

        # stdout/stderr may be either text or bytes, depending on Python
        # version.   In the latter case, decode to text.
        if not isinstance(o, str):
            o = o.decode('utf-8')
        if not isinstance(e, str):
            e = e.decode('utf-8')

        # get the last line of stdout, even if empty
        process_output_lines = o.strip().split('\n')
        last_line = process_output_lines[-1]
        for line in process_output_lines[:-1]:
            sys.stdout.write('%s\n' % line)

        if e:
            sys.stderr.write(e)

        try:
            json_output = json.loads(last_line)
            if isinstance(json_output, dict):
                return (200, json_output)
            else:
                return error(last_line)
        except Exception:
            return error(last_line)

print(sys.version)
i = invoke()
print(i.run('snowy_version_python2.py', os.environ))
print(i.run('snowy_version_python3.py', os.environ))
