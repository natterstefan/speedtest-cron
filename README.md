# speedtest-cron

[![GitHub stars](https://img.shields.io/github/stars/natterstefan/speedtest-cron.svg)](https://github.com/natterstefan/speedtest-cron/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/natterstefan/speedtest-cron.svg)](https://github.com/natterstefan/speedtest-cron/network)
[![GitHub issues](https://img.shields.io/github/issues/natterstefan/speedtest-cron.svg)](https://github.com/natterstefan/speedtest-cron/issues)
[![Inspired by J0s3f](https://img.shields.io/badge/Inspired%20by-J0s3f-blue.svg)](https://gitgud.io/J0s3f/speedtest_cron)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/natterstefan/speedtest-cron.svg?style=social)](https://twitter.com/intent/tweet?text=https://github.com/natterstefan/speedtest-cron)
[![Twitter Follow](https://img.shields.io/twitter/follow/natterstefan.svg?style=social&label=Follow)](https://twitter.com/natterstefan)


An easy to use script test the speed (down-, upload and ping) of your ISP regularly (cronjob). [Inspired (Forked) by J0s3f's speedtest_cron on gitgud.io][jsspcr].


## Idea

To run speedtests we use [speedtest-cli by Matt Martz][spcli]. For consistent results, always use the same test server. Regular tests can be used to identify trends.

The tests should be performed as close to the modem / router as possible. In any case I recommend you use a Ethernet (network) cable.

Ideal would be the execution directly on your router. If it has a storage for storing the measurement data and has enough power to run Python, you should run the code on the router. Otherwise I recommend to use a RaspberryPi or similar, which is connected by cable to the router.


## System Requirements

A UNIX-like system with Python (at least 2.5) is required to run the scripts.

### Submodule

if the folder speedtest_cli is empty run ```git submodule update --init```


## Installation

### speedtest_cron

With `./speedtest_cron` you run the test. But before you run the script you should change the speedtest server.

The current server is ```5351``` (*UPC (Vienna, Austria)*). You can get a list of available servers by running ```./speedtest_cli/speedtest_cli.py --list```. Replace the serverId with the one you would like to use. In order to find the best one, I suggest you run a speedtest on [speedtest.net](speedtest) first and use the server they use.

With ``` `/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'` ``` we get your current IP-Address and use it as the source for the speedtest. If you run into problems you can remove ```--source `/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'` ``` though.

### speedtest_crontab

_speedtest_cron_ should run regularly to be able to analyse trends. To do so you should add a cronjob to `/etc/crontab` or ```crontab -e```. Take a look at the _speedtest_crontab_ file and replace ```/path/to/this/folder/``` with the actual path.

### speedtest_csv

With ```./speedcsv > results.csv``` you generate a file of the generated results (one file per test in the speedtests folder). You can then further evaluate the results in a spreadsheet.

### speedtest_ifttt

After reading the "[Use Raspberry Pi to Measure Broadband Speeds to Hold Your ISP Accountable][iftttmaker]" article I decided to implemented [Aallan's work][gistaallan] here too. Because I would like to get either a push notification when the internet speed drops or add the result to a Google Spreadsheet automatically. This is how you use it:

- rename ```example.cfg``` to ```speedtest.cfg```
- setup the [maker channel on IFTTT][maker]
- add an Applet [like this one][ifapplet]
- add the secret key and event name to the `speedtest.cfg`
- run the script ```./speedtest_ifttt```

## Development

Improvements, suggestions or bug fixes are very welcome. Just create a pull request.


## Similar projects

There are other projects available, like [speedtest-cli-extras by HenrikBengtsson][spclix], [speedtest-cron by vwillcox][vwillcox] or [speedtest-cron by brainTrain][brainTrain]. The last one makes use of [Google Spreadsheets and IFTTT's Maker][iftttmaker].


 [spcli]: https://github.com/sivel/speedtest-cli
 [spclix]: https://github.com/HenrikBengtsson/speedtest-cli-extras
 [vwillcox]: https://github.com/vwillcox/speedtest-cron
 [brainTrain]: https://github.com/brainTrain/speedtest-cron
 [speedtest]: http://www.speedtest.net/
 [jsspcr]: https://gitgud.io/J0s3f/speedtest_cron
 [iftttmaker]: http://makezine.com/projects/send-ticket-isp-when-your-internet-drops/
 [gistaallan]: https://gist.github.com/aallan/bafc70a347f3b9526d30
 [ifapplet]: https://ifttt.com/applets/49618185d-log-speedtest-results-to-spreadsheet
 [maker]: https://ifttt.com/maker
