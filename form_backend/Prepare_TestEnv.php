<?php
$folder_path = "../testscript_uploads/"; 
   
// List of name of files inside 
// specified folder 
$fil2 = glob($folder_path.'/*');  
   
// Deleting all the files in the list 
foreach($fil2 as $fil1) { 
   
    if(is_file($fil1))  
    
        // Delete the given file 
        unlink($fil1);  
} 

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the new checkbox title from the form
    $newCheckbox = $_POST["checkboxes"];
    foreach ($newCheckbox as $name){ 
        echo '<script type="text/javascript">alert("'.$name.'")</script>';
    }

    if(isset($_POST['submit'])) {
        $files = $_FILES['fileUpload'];
        for($i=0; $i<count($files['name']); $i++){


        if (isset($files["name"][$i]) && $files["error"][$i] == 0) {
            $targetDir = "../testscript_uploads/";
            $targetFile = $targetDir . basename($files["name"][$i]);
            $fileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));
    
            // Check if the file is a Python file
            if ($fileType == "py") {
                // If it's a Python file, move it to the uploads directory
                if (move_uploaded_file($files["tmp_name"][$i], $targetFile)) {
                    echo "File uploaded successfully: " . htmlspecialchars(basename($files["name"][$i]));
                } else {
                    echo '<script type="text/javascript">alert("Error uploading file.")</script>';
                    echo "<script type='text/javascript'>window.location.href='../index.php'</script>";
                }
            } else {
                echo '<script type="text/javascript">alert("Only Python files are allowed.")</script>';
                echo "<script type='text/javascript'>window.location.href='../index.php'</script>";
            }
        } else {
            echo '<script type="text/javascript">alert(Error: ' . $files["error"][$i].')</script>';
            echo "<script type='text/javascript'>window.location.href='../index.php'</script>";
        }
    }



   /* if(count($_FILES["fileUpload"]["name"]) > 0) {
        echo "<h3>Uploaded Python Files:</h3>";
        foreach($_FILES["fileUpload"]["name"] as $key => $name) {
            echo $name . "<br>";
        }
    
    else {
        echo "<p>No files uploaded.</p>";
    }*/
#shell_exec('C:/Users/SHREESHA/AppData/Local/Microsoft/WindowsApps/python3.10.exe "c:/xampp/htdocs/Selenium Website Testing/server/dynamicServer.py"');
$command='start cmd /k "python ../server/dynamicServer.py"';
exec($command);
$command = "powershell.exe -ExecutionPolicy Bypass -File ../flask_server_setup.ps1";
exec($command);
    echo "<script type='text/javascript'>window.location.href='../dashboard.php'</script>";

    // header("Location: ../dashboard.php");
    // exit();
}
}
?>
