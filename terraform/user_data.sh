#!/bin/bash
set -e
exec > >(tee /var/log/user-data.log) 2>&1

apt update -y
apt upgrade -y || echo "apt upgrade had non-fatal errors, continuing anyway"

apt install -y git docker.io docker-compose-v2 curl
systemctl start docker
systemctl enable docker
usermod -aG docker ubuntu

apt install -y openjdk-21-jdk
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key | tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | tee /etc/apt/sources.list.d/jenkins.list > /dev/null
apt update -y
apt install -y jenkins
systemctl start jenkins
systemctl enable jenkins

usermod -aG docker jenkins
systemctl restart jenkins
systemctl restart docker

echo ">>> Bootstrap complete"