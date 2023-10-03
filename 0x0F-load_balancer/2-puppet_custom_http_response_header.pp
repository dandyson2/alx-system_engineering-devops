# Description: Puppet manifest to automate the creation of a custom HTTP header response in Nginx

# Ensure the system packages are updated
exec {'update_packages':
  command => '/usr/bin/apt-get update',
}

# Ensure Nginx is installed and configured with a custom HTTP header
package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

# Restart Nginx service to apply configuration changes
exec {'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}
