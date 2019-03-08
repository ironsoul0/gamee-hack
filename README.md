<p align="center">
  <a href="http://ant.design">
    <img width="200" src="https://lh3.googleusercontent.com/sGQFOfOfbA5uYNRc5eoeMT9_KxL4ofl6YFEKQdnyZrCxgc1UOwku0PVgdudgYMro_xsv">
  </a>
</p>

<h1 align="center">Gamee Hack proxy</h1>

<p align="center">Simple proxy server for hacking <bold>Gamee</bold> games</p>

## 🔨 Usage

1. You first have to [install Python](https://www.python.org/downloads/) on your machine
2. After installing Python, you should be able to run the following in the command line:

```console
root@root:~$ pip install mitmproxy
```

3. Now in order to run proxy successfully, you have to configure your browser's proxy settings. You should set both `HTTP` and `HTTPS` protocols to the following Web Proxy Server: `localhost:8000`. Use the following steps to configure Proxy setting for your browser.

- If you use Mac, you should [configure Safari](https://support.portswigger.net/customer/portal/articles/1783070-Installing_Configuring%20your%20Browser%20-%20Safari.html). If you successfully configure Safari, all browsers will use the same proxy, so they do not need additional configuration.
- If you do not use Mac and your browser is [Chrome](https://support.portswigger.net/customer/portal/articles/1783065-configuring-chrome-to-work-with-burp) or [Firefox](https://support.portswigger.net/customer/portal/articles/1783066-configuring-firefox-to-work-with-burp).

4. Once you have installed all necessary packages and configured your proxy settings, route to the project folder and change the value of `desired_score` variable in `main.py` file to the score you want. By default, it is set to 1000.

5. Now run the following in the command line:

```console
root@root:~$ mitmdump -s main.py
```
5. Play any game and once you finish to play, your score will change to a `desired_score`

6. When you finish playing the game, set your browser Proxy settings to default
