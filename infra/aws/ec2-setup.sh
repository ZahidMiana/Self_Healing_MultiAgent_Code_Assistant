#!/bin/bash
# One-time EC2 setup script for Amazon Linux 2023

set -e

echo "==> Updating system..."
sudo dnf update -y

echo "==> Installing Docker..."
sudo dnf install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user

echo "==> Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "==> Installing AWS CLI..."
sudo dnf install awscli -y

echo "==> Creating app directory..."
mkdir -p ~/agentforge
cd ~/agentforge

echo "==> Done! Next steps:"
echo "  1. Copy docker-compose.prod.yml and .env.prod to ~/agentforge/"
echo "  2. Run: docker compose -f docker-compose.prod.yml up -d"
