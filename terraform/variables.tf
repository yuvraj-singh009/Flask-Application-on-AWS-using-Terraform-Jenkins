variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

variable "project_name" {
  type    = string
  default = "two-tier-flask-app"
}

variable "my_ip" {
  description = "Your public IP in CIDR notation, e.g. 49.36.12.100/32"
  type        = string
}

variable "root_volume_size" {
  type    = number
  default = 20
}