# Puppet manifest to optimize Nginx server for increased traffic handling

# Increase the ULIMIT of the default file for Nginx
exec { 'fix--for-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx to apply the changes
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d/'
}
