# Puppet code that find out why Apache is returni g a 500 error and fixes it using Strace.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
