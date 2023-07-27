
What is this?
=============

This is a *very* simple HTTP service that waits for PUTs of image files.

It doesn't care what the URL path is, and will try to resize the image to fit the display.

Setup
=====

Check out the code somewhere on your Pi. The add a line to /etc/rc.local to start the server at boot. Adjust your path as needed.

```
python3 /root/inky7-httpd/i7httpd/i7httpd.py 2>&1 > /var/log/i7httpd.log &
```

