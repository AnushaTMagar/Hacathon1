<?php
session_start();
{
$Username = $_POST['Username'];
$Password = $_POST['Password'];

//DATABASE CONNECTION

$conn = new mysqli("localhost","root","","register");
    
   
    
	if($conn->connect_error){
		die("Failed to connect : ".$conn->connect_error);
	}else{
		$stmt=$conn->prepare ("select * from registration where Username =?");
        $stmt->bind_param("s",$Username);
        $stmt->execute();
        $stmt_result = $stmt->get_result()->fetch_assoc();
        if($stmt_result ->num_rows > 0)
        {
            $data=$stmt_result->fetch_assoc();
        }
    if($data['Password']===$Password)
    {
        header('location:index.html'); 
    }
        else{
            header('location:account.html'); 
        }
    }
}
?>
    
