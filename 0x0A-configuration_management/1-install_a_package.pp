# Install a package using puppet

package {'puppet-lint':
  install_options => ['-v', '2.5.0'],
  provider        => 'gem'
}
