# 0x17. Web stack debugging #3

## Background Context
<p>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png">
</p>

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company 
Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Requirements
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* Your Puppet manifests must pass `puppet-lint` without any errors (version >= 1.1.0):
* Your Puppet manifests must run without error
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* Your Puppet manifests files must end with the extension `.pp`
* Files will be checked with Puppet v3.4

### Install `puppet-lint`
```
gem install puppet-lint -v 1.1.0
```
---


root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

```

websites