<?php
phpinfo();
// include_once("pdo_mysql.php");

// $host = 'localhost';
// $db   = 'db1';
// $user = 'root';
// $pass = '12345';
// $charset = 'utf8';

// try {
//     $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
//     $db = new PDO($dsn, $user, $pass);
// } catch (PDOException $e) {
//     echo $e->getMessage()."<br>";
//     die();
// }
// $sql = 'SELECT * from shapes';
// foreach($db->query($sql) as $row) {
//     echo $row['shape']." ".row['size']."<br>";
// }
// $db = null;

// $dbhost = "localhost";
// $dbuser = "root";
// $dbpass = "12345";
// $dbname = "db1";

// // // if($_SERVER['REQUEST_METHOD'] == "POST"){

// $shape;
// $color;
// $size;
// $pos;

// // Get values
// if (isset($_POST['shape'])) {
//     $shape = $_POST['shape'];
// } else {
//     $shape = 0;
// }
// if (isset($_POST['color'])) {
//     $color = $_POST['color'];
// } else {
//     $color = 0;
// }
// if (isset($_POST['size'])) {
//     $size = $_POST['size'];
// } else {
//     $size = 0;
// }
// if (isset($_POST['pos'])) {
//     $pos = $_POST['pos'];
// } else {
//     $pos = 0;
// }

// // Escape User Input to help prevent SQL Injection
// $shape = mysql_real_escape_string($shape);
// $color = mysql_real_escape_string($color);
// $size = mysql_real_escape_string($size);
// $pos = mysql_real_escape_string($pos);

//Connect to MySQL Server
// $conn = pdo_connect($dbhost, $dbuser, $dbpass);

// // //Select Database
// pdo_select_db($dbname) or die(mysql_error());

// // //Insert into db
// $sql = "INSERT INTO shapes (id, shape, color, size, pos) VALUES (Null, 3, 3, 3, 3)";

// $retval = pdo_query($sql, $conn);

// if(! $retval ) {
//    die('Could not enter data: ' . mysql_error());
// }

// echo "Entered data successfully\n";

// pdo_close($conn);
// // }

// // $shapes[] = array($shape, $color, $size, $pos);

?>

<!-- <html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <p>
1234<br>
4312<br>
4321<br>
 </p>
 </body>
</html> -->