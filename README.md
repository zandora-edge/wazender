
![Logo](https://raw.githubusercontent.com/zandora-space/zanx/main/zanx.png)


# Wazender : Powerful Bulk Message Sender

It's an python module to send whatsapp messages in bulk with or without attachments to as many users as needed.


## Badges

![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)

![Python](https://img.shields.io/badge/python-v3.7-blue?)

![PyPi](https://img.shields.io/badge/pypi-v0.0.3-blue?)

## Features

- You can send bulk messages using whatsapp.
- You can send messages with or without attachments.
- No need of whastapp business official api to send bulk mesaages.
- Developed mainly for Digital Marketers.
- Easy to use.

## Installation

Install my-project with pip

```bash
  pip install wazender
```
    
## Dependency


Wazender requires following programs to run properly :

- selenium

Install selenium using pip command :

```bash
pip install selenium
```



## Usage 1 - To Send Only Message

```python
import wazender

path = r'YOUR_DRIVER_PATH'

wazender.sendmsg('users.txt', 'msg.txt', path=path)

```


## Usage 2 - To Send Message with Attachment

```python
import wazender

path = r'YOUR_DRIVER_PATH'
attach = r'FILE_PATH'

wazender.sendmsg('users.txt', 'msg.txt', path=path, attach=attach)

```


## Roadmap

- Make it more simple to use

- Add GUI Option


## Authors

- [@zandora-space](https://www.github.com/zandora-space)
- [@Ram-zandora](https://github.com/Ram-zandora)


## Support

For support, email professor@zandora.space or follow our Instagram Page @zanx.coders


## Feedback/Issues

If you have any feedback, please reach out to us at professor@zandora.space

If you have facing any issues, please report via 
[Report Issues](https://github.com/zandora-space/wazender/issues)

## License

[MIT](https://github.com/zandora-space/wazender/blob/main/LICENSE)

