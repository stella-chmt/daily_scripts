#!/usr/bin/expect  
set timeout 5
set server  [lindex $argv 0]
set name 你的用户名
set pw 你的密码

spawn ssh ${name}@跳板机ip
expect {
    "*password:*" {  
        send "${pw}\r";  
        exp_continue;  
    }  
    "*${name}@oahost172*" {  
        send "ssh -p58422 ${name}@$server\r";  
        exp_continue;  
    } 
    "*yes/no*" {  
        send "yes\n";  
        exp_continue;  
    }   
    "password:" {  
        send "${pw}\r";  
    }    

}      
interact 
