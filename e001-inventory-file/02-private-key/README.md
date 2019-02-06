## Generate SSH key pair

```sh
ssh-keygen -b 4096 -f ~/ansible-exercise-key
```

## Copy SSH key pair to remote server

change the `192.168.32.135` to your ansible-target IP address. default password is `1234`

```sh
ssh-copy-id -i ~/ansible-exercise-key ansible@192.168.44.128
```


## Test the hosts file

(no password needed)

```sh
ansible -m ping -i hosts server
```

