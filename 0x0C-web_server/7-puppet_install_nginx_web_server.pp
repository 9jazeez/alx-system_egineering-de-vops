#File uses puppet language to install Nginx 
# Redirect using a 301 moved Permanently

package { 'nginx':
  ensure => installed,
  name   => 'nginx'
}

file { '/var/www/html/index.html':
  content => 'Hello World',
  path    => 'var/www/html/index.html'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  line     => 'rewrite ^/redirect_me https://www.google.com'
  multiple => true
}
