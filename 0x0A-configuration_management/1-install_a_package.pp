# install flask -v2.1.0 from pip3


exec { 'install python packages':
     command   => 'pip3 install --force Flask==2.1.0 flask_restful apiai',
     path => ['/usr/bin/'],
     unless  => '/usr/bin/test -f /usr/local/lib/python3.2/dist-packages/flask/app.py'
}
