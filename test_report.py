import json
import tarfile
import os
import shutil

tmp = "C:/Users/aalan/codes/python/tmp"
if not os.path.exists(tmp):
    os.mkdir(tmp)

a = "C:/Users/aalan/Desktop/Take_Home_Test/checkbox_submission_technical_assignment.tar.xz"
b = f"{tmp}/checkbox_submission_technical_assignment.tar"

with tarfile.open(a, 'r') as f:
    f.extract("submission.json", tmp)

with open(f"{tmp}/submission.json") as fil:
        p = json.load(fil)
        print("Version tested:", p["distribution"]["description"])
    #    print("Number of tests run:", p["results"][0]["id"])
        testsRun = len(p["results"])
        print("Number of tests run:", testsRun)

        statusSkip = 0
        statusFail = 0
        statusPass = 0
        for i in range(testsRun):
            status = p["results"][i]["status"]
            if status == "skip":
                statusSkip += 1
            elif status == "fail":
                statusFail += 1
            elif status == "pass":
                statusPass += 1
        percentSkip = 100 * (statusSkip/testsRun)
        f"{percentSkip}"
        percentageSkip = str(percentSkip) + "%"
        print("Outcome:")
#    print("  - skip: {skip} ({num1:f})".format(skip=statusSkip, num1=percentageSkip))
shutil.rmtree(tmp, ignore_errors=True)
