from roboflow import Roboflow
rf = Roboflow(api_key="lEab6RLbYcfcIpIQEGhE")
project = rf.workspace("frato-xazo-xyz").project("clothing-olr9p-g15wf")
version = project.version(1)
dataset = version.download("yolov8")
                