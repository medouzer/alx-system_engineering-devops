#Execute a command killmenow

exec { 'killmenow':
command  => '/usr/bin/pkill killmenow',
}
