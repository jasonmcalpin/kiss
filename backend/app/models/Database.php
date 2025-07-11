<?php
// rest of classes will talk to this to access the database to keep the code consolidated.
class Database {
    private $pdo;
    
    public function __construct() {
        // Database connection
    }
    
    public function query($sql, $params = []) {
        // Execute queries
    }
}
?>