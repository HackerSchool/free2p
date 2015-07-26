# What is free2p?

free2p is a Raspberry Pi based solution that allows you to know if a bathroom is occupied or not via a web browser.<br>
<img src="https://github.com/HackerSchool/free2p/blob/master/media/5free2p.PNG" width="350" >
<img src="https://github.com/HackerSchool/free2p/blob/master/media/6busy2p.PNG" width="350" >

# Making the server run at boot

To make the server when the Raspberry Pi boots add the following line to your `/etc/rc.local` file before the `exit 0` line:

`(sleep 10; python3 path/to/server/folder/server.py) &`

As an example, if the folder for the server is inside `/usr/bin` the you would add the line `(sleep 10; python3 /usr/bin/free2p/server.py) &`.

# Wiring
<table>
    <tr>
        <td><img src="https://github.com/HackerSchool/free2p/blob/master/help.png" height="280" ></td>
        <td>You can check how to wire the sensor any time by adding `/help.png` to the end of the free2p URL or address.</td>
    </tr>
</table>

# Our physical setup
We used a Raspberry A+ with a Wi-Fi dongle and connected it to the local network:
<img src="https://github.com/HackerSchool/free2p/blob/master/media/1raspAplus.jpg" height="250">

Our "door locked" sensor consists of two springs installed with screws that connect via two wires to the raspberry pi:<br>
<img src="https://github.com/HackerSchool/free2p/blob/master/media/2Lock.jpg" height="280">
<img src="https://github.com/HackerSchool/free2p/blob/master/media/3Inside.jpg" height="280">
<img src="https://github.com/HackerSchool/free2p/blob/master/media/4Outside.jpg" height="280">
(The raspberry pi is inside the white box. The spring wires go trough the wall and straight into the box)
