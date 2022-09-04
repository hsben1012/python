#!/usr/bin/python3

import json, sys, shutil, os, tarfile

def text(firstParameter, secondParameter=None):
    # Generate tmp directory, tmpDir, for storing submission.json.
    getHomeDir = os.getenv("HOME")
    tmpDir = f"{getHomeDir}/tmp"
    if not os.path.exists(tmpDir):
        os.mkdir(tmpDir)

    # Open tarfile and extract to tmpDir.
    with tarfile.open(firstParameter, 'r') as fl:
        fl.extract("submission.json", tmpDir)

    # Open submission.json in tmpDir.
    with open(f"{tmpDir}/submission.json") as f:
        p = json.load(f)

        testsRun = len(p["results"]) # Count item numbers in submission.json

        # Count numbers of test results show skip, fail and pass
        statusSkip = 0
        statusFail = 0
        statusPass = 0
        duration = 0
        listFail = []
        for i in range(testsRun):
            status = p["results"][i]["status"]
            duration += p["results"][i]["duration"]
            if status == "skip":
                statusSkip += 1
            elif status == "fail":
                statusFail += 1
                listFail.append(p["results"][i]["id"])
            elif status == "pass":
                statusPass += 1

        # Without --json optional argument.
        if secondParameter != "--json":
            print("Version tested:", p["distribution"]["description"])
            print("Number of tests run:", testsRun)
            percentSkip = 100 * (statusSkip/testsRun)
            percentFail = 100 * (statusFail/testsRun)
            percentPass = 100 * (statusPass/testsRun)
            skip = f"{percentSkip:.0f}"
            fail = f"{percentFail:.0f}"
            pss = f"{percentPass:.0f}"
            percentageSkip = skip + "%"
            percentageFail = fail + "%"
            percentagePass = pss + "%"
            print("Outcome:")
            print("  - skip: {skip} ({num1})".format(skip=statusSkip, num1=percentageSkip))
            print("  - fail: {fail} ({num2})".format(fail=statusFail, num2=percentageFail))
            print("  - pass: {pss} ({num3})".format(pss=statusPass, num3=percentagePass))
            print(f"Total run duration: {duration:.2f} seconds")

            print(f"List of failed tests: ")
            for j in range(statusFail):
                print(f"  - {listFail[j]}")

        # With --json optional argument.
        elif secondParameter == "--json":
            listJsonKey = ["version", "nb_skip", "nb_fail", "nb_pass", "total_duration", "failed_tests"]
            listJsonValue = [p["distribution"]["description"], statusSkip, statusFail, statusPass, f"{duration:.2f}", listFail]
            listJson = zip(listJsonKey, listJsonValue)
            print(dict(listJson))

    # Delete tmpDir with contents.
    shutil.rmtree(tmpDir, ignore_errors=True)


# Without --json optional argument.
if len(sys.argv) == 2:
    text(sys.argv[1])

# With --json optional argument.
elif len(sys.argv) > 2 and sys.argv[2] == "--json":
   text(sys.argv[1], sys.argv[2])

# If there were no parameters in optional argument.
else:
    print("Please enter file or correct parameters (--json).")
