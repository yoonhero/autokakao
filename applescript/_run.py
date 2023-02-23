import os
import subprocess

class Result:
    code = None
    out = None
    err = None

    def __init__(self,code,out,err):
        self.code = code
        self.out = out.decode("utf-8").rstrip()
        self.err = err.decode("utf-8").rstrip()

def _run(script):
    """run script file/string"""
    args = ["osascript", "-"]
    kwargs = dict(stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    proc = subprocess.Popen(args,**kwargs)
    cmd = open(script).read() if os.path.exists(script) else script
    out, err = proc.communicate(input=cmd.encode("utf-8"))
    return Result(proc.returncode,out, err)