# ConnectWise SecureConnect Authentication Bypass Vulnerability
An exploit proof of concept for ConnectWise SecureConnect authentication bypass vulnerability.

## Blog Post
More details here:
[https://www.horizon3.ai/attack-research/red-team/connectwise-screenconnect-auth-bypass-deep-dive/](https://www.horizon3.ai/attack-research/red-team/connectwise-screenconnect-auth-bypass-deep-dive/)

## Usage
Running this script will overwrite the existing administrative user credentials.

```
% python3 ScreenConnect-AuthBypass.py -h                          
usage: ScreenConnect-AuthBypass.py [-h] -t TARGET -u USERNAME -p PASSWORD

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        The base URL of the target
  -u USERNAME, --username USERNAME
                        The username to add
  -p PASSWORD, --password PASSWORD
                        The new password
```

## Follow the Horizon3.ai Attack Team on Twitter for the latest security research:
*  [Horizon3 Attack Team](https://twitter.com/Horizon3Attack)
*  [James Horseman](https://twitter.com/JamesHorseman2)
*  [Zach Hanley](https://twitter.com/hacks_zach)

## Disclaimer
This software has been created purely for the purposes of academic research and for the development of effective defensive techniques, and is not intended to be used to attack systems except where explicitly authorized. Project maintainers are not responsible or liable for misuse of the software. Use responsibly.
