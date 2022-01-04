# This puppet manuscript creates a file at
# /tmp.
# With specified owner, group and contents

file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data'

}
