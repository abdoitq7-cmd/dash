<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Allow-Headers: Content-Type");

$data = json_decode(file_get_contents("php://input"), true);

if (!isset($data['message']) || trim($data['message']) === "") {
    http_response_code(400);
    echo json_encode([
        "status" => "error",
        "message" => "Message is required"
    ]);
    exit;
}

$message = $data['message'];

// هنا تحط أي API أو AI logic
$response = "Hello from PHP API, you said: " . $message;

echo json_encode([
    "status" => "success",
    "response" => $response
]);
