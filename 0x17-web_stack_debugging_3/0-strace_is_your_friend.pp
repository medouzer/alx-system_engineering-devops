#Strace is your friend

exec{'fix_error_phpp':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path => '/usr/local/bin/:/bin/'
}
