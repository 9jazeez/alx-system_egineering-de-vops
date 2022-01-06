#Comment for puppet file

ssh_authorized_key { 'ubuntu@918-web-01':
  ensure   => present,
  options  => {
    'PasswordAuthentication' => 'no',
    'IdentityFile'           => '~/.ssh/school',
    'PubKeyAuthentication'   => 'yes'
       },
  provider => ssh-rsa,
  user     => 'ubuntu',
  target   => '~/.ssh/school',
  type     => ssh-rsa
}
