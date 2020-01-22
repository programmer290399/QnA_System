# How to Setup :

## Clone the Repo 
```bash
$ git clone https://github.com/programmer290399/QnA_System.git
```
## Install the Dependencies 
```bash
$ cd QnA_System/
$ conda create -n QnA_system_test python=3.6
$ source activate QnA_system_test
$ sudo -H pip install -r requirements.txt
```

```bash
$ python
>>> import nltk
>>> nltk.download('punkt')
>>> exit()
```
## Launch the App 
```bash
$ python app.py
```
## You can see the app running on  [http://127.0.0.1:5000/](http://127.0.0.1:5000/ ) in your browser.
