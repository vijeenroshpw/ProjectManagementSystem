<html>
<head></head>
<style type="text/css">
body {
	background-color:#cfcfcf;
} 
</style>
<body>
<?php
require_once("../classes/showusers.class.php");
echo "<h1 align =center>Uncommited Changes by $_GET[uname]</h1>"; 
$user = new ShowUsers($_GET['uname']);
$user->show_files($_GET['uname']);
?>
</body>
</html>
