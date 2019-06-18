# Bi-directional Attention Flow for Machine Comprehension
Based on Paper Bidirectional Attention Flow for Machine Comprehension
by-
Minjoon Seo, Aniruddha Kembhavi, Ali Farhadi, Hannaneh Hajishirzi
## 0. Requirements
#### General
- Python (developed on 3.5.2)
- unzip

#### Python Packages
- tensorflow (deep learning library, verified on r0.11,r0.12)
- nltk (NLP tools, verified on 3.2.1)
- tqdm (progress bar, verified on 4.7.4)
- jinja2 (for visaulization; if you only train and test, not needed)
- flask

## 1. Pre-processing
First, prepare data. Donwload SQuAD data and GloVe and nltk corpus
(~850 MB, this will download files to `$HOME/data`):
```
chmod +x download.sh; ./download.sh
```

Second, Preprocess Stanford QA dataset (along with GloVe vectors) and save them in `$PWD/data/squad` (~5 minutes):
```
python -m squad.prepro
```


## 2. Test
To test, run:
```
python -m basic.cli
```

Similarly to training, you can give the optimization flags to speed up test (5 minutes on dev data):
```
python -m basic.cli --len_opt --cluster
```

This command loads the most recently saved model during training and begins testing on the test data.
After the process ends, it prints F1 and EM scores, and also outputs a json file (`$PWD/out/basic/00/answer/test-####.json`,
where `####` is the step # that the model was saved).
Note that the printed scores are not official (our scoring scheme is a bit harsher).
To obtain the official number, use the official evaluator (copied in `squad` folder) and the output json file:

```
python squad/evaluate-v1.1.py $HOME/data/squad/dev-v1.1.json out/basic/00/answer/test-####.json
```



## 3. Run demo
For demo, run:
```
python run-demo.py
```
Then you can see demo webpage on localhost:1995



