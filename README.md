# TOC Project 2020

[![Maintainability](https://api.codeclimate.com/v1/badges/dc7fa47fcd809b99d087/maintainability)](https://codeclimate.com/github/NCKU-CCS/TOC-Project-2020/maintainability)

[![Known Vulnerabilities](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020/badge.svg)](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020)


Template Code for TOC Project 2020

A Line bot based on a finite state machine

More details in the [Slides](https://hackmd.io/@TTW/ToC-2019-Project#) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3.6
* line Page and App
* HTTPS Server

#### Install Pygraphviz(For visualizing Finite State Machine)
```sh
sudo apt-get install graphviz libgraphviz-dev pkg-config

sudo apt-get install python3.6-dev

pip3 install pygraphviz

```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env` file`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
```sh
download the ngrok by below link

unzip /path/to/ngrok.zip

./ngrok authtoken <YOUR_AUTH_TOKEN> 
```
* [ Donwload ngrok link](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.


## Finite State Machine
![fsm](./fsm.png)

## Usage
The initial state is set to `user`.

Below is the all states and its menaing
```sh
The State Meaning
```
* user (state)		
    * Input:"start"
    * Reply:![](https://i.imgur.com/Py2cMeM.jpg)
* start (state)
    * Input:information
    * Reply:![](https://i.imgur.com/GgFHern.jpg)
    * Input: regfood
    * Reply: ![](https://i.imgur.com/eBt1frP.jpg)
    * Input: showsuggest
    * Reply: ![](https://i.imgur.com/33bejLn.jpg)
    * Input: showfsm
    * Reply: ![](https://i.imgur.com/XE0SuRK.jpg)

* information (state)
    * function: deal with input information
* height (state)
    * Input:身高數值(int)
    * Reply:![](https://i.imgur.com/GgFHern.jpg)
* weight (state)
    * Input:體重數值(int)
    * Reply:![](https://i.imgur.com/0nBPJIq.jpg)
* money (state)
    * Input:預算數值(int)
    * Reply:![](https://i.imgur.com/aMvQlIP.jpg)
* age (state)
    * Input:年齡數值(int)
    * Reply:![](https://i.imgur.com/bBIAz3n.jpg)
* regfood (state)
    * Input:breakfast
    * Reply: ![](https://i.imgur.com/6DGsKL3.jpg)
    * Input:lunch
    * Reply: ![](https://i.imgur.com/M00WJzG.jpg)
    * Input:dinner
    * Reply: ![](https://i.imgur.com/hDmJ83X.jpg)
    * Input:showeat
    * Reply: ![](https://i.imgur.com/wsEMywb.jpg)
    * Input:"1"
    * Reply: ![](https://i.imgur.com/eBt1frP.jpg)
* breakfast (state)
    * Input:
        * hamegg
        * chiomelet
        * riceroll
    * Reply:![](https://i.imgur.com/90LOoCa.jpg)
* nextbreakfast (state)
    * for read the breakfast price input
* lunch(state)
    * Input:
        * subway
        * friedrice
        * noodles
        * boxedlunch
    * Reply:![](https://i.imgur.com/90LOoCa.jpg)
* nextlunch (state)
    * for read the lunch price input
* dinner(state)
    * Input:
        * chickenrice
        * oden
        * coldnoodle
        * chilipork
    * Reply:![](https://i.imgur.com/90LOoCa.jpg)
* nextdinner (state)
    * for read the dinner and price input
* showeat (state)
    * Input:"1"
    * Reply![](https://i.imgur.com/2AnWV4h.jpg)
* showsuggest (state)
    * Input:"1"
    * Reply:![](https://i.imgur.com/TPH6OTY.jpg)
* showfsm (state)
    * Input:"1"
    * Reply:![](https://i.imgur.com/bBIAz3n.jpg)
* money_check (state)
    * check the money is small than setting 
* calorie_check (state)
    * check the calorie is small than setting 
* starch_check (state)
    * check the starch is small than setting 
* money_deny (state)
   * deny the money  
* calorie_deny (state)
    * deny the money  
* starch_deny (state)
    * deny the starch  
* regtostart (state)
   * regfood go to start 
* showback (state)
   * go to regfood
```sh
The Screenshot Demo the Project
```
## Deploy
Setting to deploy webhooks on AWS CLOUD server.

### Connect to AWS

1. Register AWS Educate: https://aws.amazon.com/tw/education/awseducate/

2. Create EC2 Service:
    Services > Compute > EC2

3. Launch Instance

4. Choose Ubuntu 18.04 AMI

5. Create and Download SSH key pair 

6. Use ssh login AWS server
```sh
mv ~/Downloads/MyKeyPair.pem ~/.ssh/MyKeyPair.pem

chmod 400 ~/.ssh/MyKeyPair.pem

ssh -i ~/.ssh/MyKeyPair.pem ubuntu@ip
```



### Run project on AWS CLOUD PLATFORM

1. Install the python3 environment

2. run ngrok http

	./ngrok http 8000

3. run the app.py
    python3 app.py

## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
