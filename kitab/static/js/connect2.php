<?php
session_start();
{
$Username = $_POST['Username'];
$Email = $_POST['Email'];
$Password = $_POST['Password'];

//DATABASE CONNECTION

$conn = new mysqli("localhost","root","","register");
$s = "SELECT * FROM `registration` where Username ='$Username'";


$result = mysqli_query($conn, $s);


if($result && mysqli_num_rows($result) > 0){
    echo"Username already taken";
}
    else{
        $regi = "insert into registration(Username,Email,Password) values('$Username','$Email','$Password')";
        mysqli_query($conn, $regi);
        echo"Registration Sucessful...";
    }
}
?>