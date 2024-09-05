**First things first. You need to change three things to make this work:**

1. Line 35 – Insert the path to your batch file that opens your VPN client (ignore this if you are on the same network as your EFA).
2. Line 92/95 – Insert your username/password for your EFA. Alternatively, use environmental variables for increased security.
3. Line 124 – Insert the URL address/IP of your EFA

This program has been tested and is fully functional on EFA-3.0.2.4 and EFA-3.0.2.6, but it should work on all or most versions.

For EFA to learn spam, a human must manually identify spam messages, open them, and make 5 clicks to mark them as spam. This task can be quite annoying if you work for a larger company.
That's why I made this program. If you have to manually click on 100 spam messages per day and then make another 5 clicks for each one, it's no fun.

**How does this work?**
1) Log in to VPN (if you are outside the network).
2) Open EFA (the program will navigate you directly to the email folder).
3) Find spam messages and open them in new tabs (a maximum of 50 tabs are allowed at once).
4) Click "Learn All As Spam" and all opened messages will be marked as spam.
5) Once it is finished, simply click "Close All Tabs" to close all tabs except the main one (the email folder).

I am using threading, so the ctkinter window doesn’t freeze while the process runs.
