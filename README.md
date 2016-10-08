SmartGarage is a simple Raspberry Pi app that monitors an email account for simple 
commands such as Open, Close, Check and Kill. Any mobile phone can send a message to 
the email account (specified in email_scraper.php) with the above commands.

When a command is received, the RaspberryPi outputs a high signal for two seconds which, 
when accompanied by a transistor, shorts a garage door remote and opens/closes the door.

By using an IR Range Sensor attached to the door, this project is also able to determine 
if the garage door is open or closed, which is crucial for implementing the open/close command
(don't want to short the remote on an 'Open' command if it's already open)

A summary of the commands can be seen here:

'Check' - Replies with if the garage door is currently open or closed.
'Open' - Opens the garage door if it's closed, does nothing if it's open.
'Close' - Closes the garage door if it's open, does nothing if it's closed.
'Kill' - Kills the script.