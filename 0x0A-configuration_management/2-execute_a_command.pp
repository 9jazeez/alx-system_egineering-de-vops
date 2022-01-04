# Kill a program using puppet with pkill command

exec { 'Kill':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
