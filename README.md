# What is free2p?

free2p is a Raspberry Pi based solution that allows you to know if a bathroom is occupied or not via a web browser.
<br>
<img src="https://github.com/HackerSchool/free2p/blob/master/media/5free2p.PNG" width="350" >
Pee at will :)
<br>
<img src="https://github.com/HackerSchool/free2p/blob/master/media/6busy2p.PNG" width="350" >
Do not come in here!

# But, why free2p?

Following up on a long-term relationship with [Landing.jobs](https://landing.jobs) we decided they needed a proper WC warning system as their ranks grow in our hometown: good old Lisbon.

The Landing.jobs team lost count on the amount of times someone got up from their desk space to go to the WC only to find out someone else was occupying the "Brain room" and, therefore, they called in the A-team. Sorry, [HackerSchool](http://hackerschool.io) for the win :)

Final result? See for yourself, check the [Landing.jobs' WC status](http://wc.landing.jobs).

Go ahead and setup your own free2p installation.

# Chrome extension installation

The Chrome extension adds an icon next to Chrome's search bar, indicating the bathroom's occupation status.

<img src="https://github.com/HackerSchool/free2p/blob/master/media/chrome-extension.png">

The installation is simple:

1. [Download](https://github.com/HackerSchool/free2p/archive/master.zip) the code and unzip it
2. Go to Settings -> Extensions
3. Activate "Developer mode" checkbox
4. Click "Load unpacked extension..."
5. Select the "chrome-extension" folder from the code you downloaded
6. Click on the link "Options" on the newly added "free2p" section
7. Make sure the API URL is correct
8. Enjoy! (but only when it's green :b)

# The physical setup

We used a Raspberry A+ with a Wi-Fi dongle and connected it to the local network:
<img src="https://github.com/HackerSchool/free2p/blob/master/media/1raspAplus.jpg" height="250">

Our "door locked" sensor consists of two springs installed with screws that connect via two wires to the raspberry pi:
<br>
<img src="https://github.com/HackerSchool/free2p/blob/master/media/2Lock.jpg" height="250">
<img src="https://github.com/HackerSchool/free2p/blob/master/media/3Inside.jpg" height="250">
<img src="https://github.com/HackerSchool/free2p/blob/master/media/4Outside.jpg" height="250">
<br>
(The raspberry pi is inside the white box. The spring wires go trough the wall and straight into the box)

# Wiring setup

<table>
    <tr>
        <td><img src="https://github.com/HackerSchool/free2p/blob/master/help.png" height="280" ></td>
        <td>You can check how to wire the sensor any time by adding `/help.png` to the end of the free2p URL or address.</td>
    </tr>
</table>

# Making the server run at boot

To make the server run when the Raspberry Pi boots add the following line to your `/etc/rc.local` file before the `exit 0` line:

`(sleep 10; python3 path/to/server/folder/server.py) &`

As an example, if the folder for the server is inside `/usr/bin` then you would add the line `(sleep 10; python3 /usr/bin/free2p/server.py) &`.

# License

Released under the [GNU Affero General Public License v3.0](http://choosealicense.com/licenses/agpl-3.0/).
