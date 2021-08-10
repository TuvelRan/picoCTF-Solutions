## Description
Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:15931](Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:15931)

NOTE: The address may change in the future.

## Solution
- Open up the address on your browser.
- The first thing that comes to mind is to check the HTML source of the page.
You can check the source by using Element Inspector in your browser, but you can also add ``view-source:`` to the start of the page address.
After a quick look on the source I saw that there are two methods (GET & POST). The first thing that came to my mind is the ctf's header which called "GET aHEAD", so I thought maybe I can send a HEAD request to the URL.

So using the Terminal:
```
curl --head http://mercury.picoctf.net:15931/index.php
```
I have received the following output:
```
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_82880908}
Content-type: text/html; charset=UTF-8
```

And that's it! quick & easy!

#### picoCTF{r3j3ct_th3_du4l1ty_82880908}
