#!/usr/bin/expect

set timeout 20

spawn "./pytest.py"

expect "Enter the number1 : " { send "12\r" }
expect "Enter the number2 : " { send "23\r" }

interact
