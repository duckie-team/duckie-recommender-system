# Quick Start
Clone repo and install [requirements.txt](https://github.com/sungbinland/duckie-recommender-system/blob/main/requirements.txt) in a Python >= 3.6 environment.  
(The developer of the project ran it on Python 3.10.)
```shell
$ git clone https://github.com/sungbinland/duckie-recommender-system.git
$ cd duckie-recommender-system
$ pip install -r requirments.txt

# Setting Config And Run Python Main Code.
$ uvicorn recommender_system/main:app --reload --host='0.0.0.0' --port=8000
```