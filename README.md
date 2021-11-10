# End to end store tests

This is repository containing end-to-end tests example preformed on [automation practice page](http://automationpractice.com/)  
Recording of execution of tests is uploaded here: [tests execution recording](https://youtu.be/lljtMUfXUhA)

### Execution on local machine

#### Requirements

* [Python 3.8](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)
* [ChromeDriver](https://chromedriver.chromium.org/home)
* [Chrome browser](https://www.google.com/intl/pl/chrome/)
#### How to setup

* Make a [virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/), 
  where your test framework can run
* Install required libraries with:

```console
pip3 install -r requirements.txt
``` 
* Install [Chrome](https://www.google.com/intl/pl/chrome/) browser 
* Install [Chromedriver](https://chromedriver.chromium.org/home), on macOS, if you have homeBrew installed you can use
```
brew install --cask chromedriver
```

#### How to use

To run all tests use:

```console
python3 -m behave store_tests/
```
To run single scenario use ```-n``` flag, for example:
```
python3 -m behave store_tests/ -n "User sorts bestsellers by highest to lowest price"
```
To run single feature use ```-i``` flag, for example:
```
python3 -m behave store_tests/ -i search.feature
```