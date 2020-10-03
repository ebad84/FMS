<?php

$email = $_POST['email'];
$subject = $_POST['subject'];
$sender = $_POST['sender'];
$text = $_POST['text'];
$headers = $_POST['headers'];



if (mail($email,$subject,$text,$headers)){
    echo("sucess");
    } 
else {
    echo("error");
    }
    
?>