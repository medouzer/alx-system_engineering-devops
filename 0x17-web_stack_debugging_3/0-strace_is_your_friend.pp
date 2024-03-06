#Strace is your friend

exec { 'command':
  command  => 'sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php',
  provider => 'shell',
}
