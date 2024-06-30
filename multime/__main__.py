import time
import sys, os
import subprocess


try:
    from multime import __VERSION__
except ImportError:
    __VERSION__ = "0.0.1"

PROG = os.path.basename(sys.argv[0])


def error(msg: str):
    print(f"{PROG}: error: {msg}", file=sys.stderr)
    exit(1)


def time_cmd(cmd: list[str]):
    start = time.perf_counter()
    code = subprocess.call(cmd, stdout=subprocess.DEVNULL)
    total = time.perf_counter() - start
    return total


def run_all(cmd: list[str], amount: int):
    results = []
    for ii in range(amount):
        results.append(time_cmd(cmd))
    return results


def usage():
    pass


def main():
    if len(sys.argv) == 1:
        usage()
        error("no arguments provided.")

    cmd: str | None = None
    count: int | None = None

    idx = 1
    while idx < len(sys.argv):
        arg = sys.argv[idx]
        idx += 1

        if arg == "--":
            if cmd is not None:
                error("multiple commands given.")
            cmd = " ".join(sys.argv[idx : len(sys.argv)])
            idx = len(sys.argv)  # stop iterating through the arguments
        elif arg.isnumeric():
            if count is not None:
                error("multiple counts given.")
            count = int(arg)
        else:
            error(f"unknown flag {arg}.")

    if cmd is None:
        error("No command given")

    if count is None:
        count = 10

    results = run_all(cmd, count)
    average = sum(results) / len(results)
    print(f"'{cmd}' took an average of {average*1000} milliseconds to run.")


if __name__ == "__main__":
    main()
