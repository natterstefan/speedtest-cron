# speedtest-cron w/ Alexa Command and ngrok on a RaspberryPi

[![GitHub stars](https://img.shields.io/github/stars/natterstefan/speedtest-cron.svg)](https://github.com/natterstefan/speedtest-cron/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/natterstefan/speedtest-cron.svg)](https://github.com/natterstefan/speedtest-cron/network)
[![GitHub issues](https://img.shields.io/github/issues/natterstefan/speedtest-cron.svg)](https://github.com/natterstefan/speedtest-cron/issues)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/natterstefan/speedtest-cron.svg?style=social)](https://twitter.com/intent/tweet?text=https://github.com/natterstefan/speedtest-cron)
[![Twitter Follow](https://img.shields.io/twitter/follow/natterstefan.svg?style=social&label=Follow)](https://twitter.com/natterstefan)

An easy to use and implement Alexa Command to get the latest results from your speedtest.

## System Requirements

A UNIX-like system with Python (at least 2.5) is required to run the scripts.

## Installation of Flask-Ask and Ngrok

First you need to install [Flask-Ask][flaskask] with:

`pip install flask-ask`

In the next step you need to go to [https://ngrok.com/download][ngrok] and download the latest Linux ARM build with:

`wget https://.../ngrok-stable-linux-arm.zip`

Now you can run your ngrok Server with:

`./ngrok http 5000`

Your Localhost-Server with an external accessible Domain is now running. The output of this command looks similar to this. To use this Alexa-Skill you need to copy the HTTPS-Address into the Amazon Developer Console later.

![ngrok Example](http://i.imgur.com/G4ArV3V.png)


## Run the Speedtest Code

_Note:_ We assume that you run the `speedtest_cron` script regularly. Because (_as of now_) we do not run another speedtest (as it would take time), we just grab the result from the last result and tell it to you. There is room to improve this, but currently we do it this way.



 [flaskask]: https://github.com/johnwheeler/flask-ask
 [ngrok]: https://ngrok.com/download