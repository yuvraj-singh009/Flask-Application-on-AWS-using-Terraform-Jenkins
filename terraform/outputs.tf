output "instance_public_ip" {
  value = aws_instance.app_server.public_ip
}
output "ssh_command" {
  value = "ssh -i ${var.project_name}-key.pem ubuntu@${aws_instance.app_server.public_ip}"
}
output "jenkins_url" {
  value = "http://${aws_instance.app_server.public_ip}:8080"
}
output "flask_app_url" {
  value = "http://${aws_instance.app_server.public_ip}:5000"
}

