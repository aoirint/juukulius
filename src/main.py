import os
import sys
from pathlib import Path
import re
import subprocess
import tempfile

JULIUS_DICTATION_KIT_ROOT = os.environ.get('JULIUS_DICTATION_KIT_ROOT')
assert JULIUS_DICTATION_KIT_ROOT

JULIUS_DICTATION_KIT_ROOT = Path(JULIUS_DICTATION_KIT_ROOT)

JULIUS_DICTATION_KIT_PATH = JULIUS_DICTATION_KIT_ROOT / 'run-linux-dnn.sh'

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('wavfile', type=str)
    parser.add_argument('-cutsilence', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    wavfile = args.wavfile
    cutsilence = args.cutsilence
    verbose = args.verbose

    with tempfile.NamedTemporaryFile(mode='w') as fp:
        fp.write(wavfile)
        fp.flush()

        cmd = [
            JULIUS_DICTATION_KIT_PATH,
            '-input',
            'file',
            '-filelist',
            fp.name,
        ]

        if cutsilence:
            cmd += [ '-cutsilence' ]

        proc = subprocess.Popen(
            cmd,
            cwd=JULIUS_DICTATION_KIT_ROOT,
            stdout=subprocess.PIPE,
            # stderr=subprocess.PIPE,
            encoding='utf-8',
        )

        pat = re.compile(r'^sentence.*:\s*(.*)$')
        while True:
            line = proc.stdout.readline()

            if verbose:
                sys.stdout.write(line)
                sys.stdout.flush()

                # errline = proc.stderr.readline()
                # sys.stderr.write(errline)
                # sys.stderr.flush()

            m = pat.match(line)
            if m:
                print(m.group(1))

            if not line and proc.poll() is not None:
                break
