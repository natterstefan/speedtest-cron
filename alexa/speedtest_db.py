import sqlite3

import subprocess
import os, sys
import json

conn = sqlite3.connect('example.db') #TODO Change name
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS speedtests
             (id integer primary key, timestamp datetime, ping real, download real, upload real)''')

# Get the Data
parentscript=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path=parentscript + "/speedtest_cli/speedtest.py"
json_data = json.loads(subprocess.check_output([sys.executable, path, "--json --secure"])) ## TODO add --server ... Docu: http://stackoverflow.com/a/30664497/1238150

# Insert a row of data
c.execute('INSERT INTO speedtests (timestamp, ping, download, upload) VALUES (?,?,?,?)', (json_data['timestamp'], json_data['ping'], json_data['download'], json_data['upload'])) #http://stackoverflow.com/a/29087022/1238150

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
