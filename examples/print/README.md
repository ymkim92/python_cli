There are three files in this folder.

- ``print_with_delay.py``

  It prints 0, 100, 200 with delay and then it prints same numbers in the same line.
  I hope you run this file first to see how this script works.

- ``print.sh``

  When you run ``print_with_delay.py`` from ssh remote command, it won't have any environment settings.
  So this file set environment by activating conda in my case. 
  Then it runs ``print_with_delay.py`` with full path and ``-u`` option.
  You need to change the full path name for you system.
  ``-u`` option is important because this option flushes ``sysout`` 
  whenever the called Python script prints something.

- ``cmdflush.py``

  It has two commands: ``local_command`` and ``ssh_command``.
  You need to install ssh server in your computer before you run ``ssh_command``. 
  Then you need to change ``host_user`` to your ID in the file.
  Then you can follow how two commands work to display outputs in realtime.
  