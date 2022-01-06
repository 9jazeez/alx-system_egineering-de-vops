#Comment for puppet file

sshkey { 'ubuntu': 
  name => ubuntu@918-web-01
  ensure => present
  options => {
    'PasswordAuthentication' => 'no'
    'IdentityFile' => '~/.ssh/school'
    'PubKeyAuthentication' => 'yes'
     	}
  provider => ssh-rsa
  target => ~/.ssh/school
  type => ssh-rsa
} 
