# What is free2p?

free2p is a Raspberry Pi based solution that allows you to know if a bathroom is occupied or not via a web browser.

# Making the server run at boot

To make the server when the Raspberry Pi boots add the following line to your `/etc/rc.local` file before the `exit 0` line:

`(sleep 10; python3 path/to/server/folder/server.py) &`

As an example, if the folder for the server is inside `/usr/bin` the you would add the line `(sleep 10; python3 /usr/bin/free2p/server.py) &`.

# Wiring

You can check how to wire the sensor any time by adding `/help.png` to the end of the free2p URL or address.

