# ARLPass
爆破灯塔系统密码的脚本

原项目地址: [iak-ARL](https://github.com/nu0l/iak-ARL)

在项目中遇到资产灯塔系统，发现以前写的脚本较垃圾，花了点时间更新一个

### Use 
```
python3 arl_pass.py -u https://127.0.0.1:5003 -p pass.txt
python3 arl_pass.py -f file.txt -p pass.txt
```
<img width="800" alt="image" src="https://user-images.githubusercontent.com/54735907/181439149-577eed32-c282-409d-9771-2d62eaa710ab.png">


### Options
```
  -u URL, --url URL     Target URL (e.g. http://example.com)
  -f FILE, --file FILE  Select a target list url file (e.g. file.txt)
  -p PASSWD, --pass PASSWD
                        Select a password dictionary file (e.g. pass.txt)
  -h, --help            Show help message and exit
```
<img width="800" alt="image" src="https://user-images.githubusercontent.com/54735907/181437836-173781f4-08bd-42a4-9476-4a252e3b1826.png">
