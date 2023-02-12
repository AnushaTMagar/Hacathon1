<?php
session_start();

$Username = $_POST['Username'];
$Password = $_POST['Password'];

//DATABASE CONNECTION

$conn = new mysqli("localhost","root","","register");

$s = "SELECT * FROM `registration` where Username ='$Username' &&Password='$Password' ";


$result = mysqli_query($conn, $s);


if($result && mysqli_num_rows($result) > 0){
     header('location:index.html'); 
}
    else{
       header('location:account.html'); 
    }

?>

