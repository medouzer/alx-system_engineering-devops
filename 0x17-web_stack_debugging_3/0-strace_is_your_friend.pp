#Strace is your friend

exec { 'fix_phpp':
	command	=> 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	provider => 'shell',
}
