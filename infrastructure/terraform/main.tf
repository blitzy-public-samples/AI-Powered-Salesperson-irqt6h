# Main Terraform configuration file for provisioning Google Cloud Platform resources

# Provider configuration for Google Cloud
provider "google" {
  project = var.project_id
  region  = var.region
}

# Resource definitions for Google Cloud Run
resource "google_cloud_run_service" "app" {
  name     = "chatbot-app"
  location = var.region

  template {
    spec {
      containers {
        image = var.app_image
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Resource definitions for Google Cloud SQL
resource "google_sql_database_instance" "main" {
  name             = "chatbot-db-instance"
  database_version = "POSTGRES_13"
  region           = var.region

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "database" {
  name     = "chatbot_db"
  instance = google_sql_database_instance.main.name
}

# Resource definitions for Google Cloud Storage
resource "google_storage_bucket" "data" {
  name     = "chatbot-data-bucket"
  location = var.region
}

# Resource definitions for Google Cloud AI Platform
resource "google_ai_platform_model" "chatbot_model" {
  name        = "chatbot-model"
  description = "AI model for chatbot"
  regions     = [var.region]
}

# Network and security group configurations
resource "google_compute_network" "vpc_network" {
  name                    = "chatbot-vpc-network"
  auto_create_subnetworks = "true"
}

resource "google_compute_firewall" "allow_http" {
  name    = "allow-http"
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
}

# Output definitions for important resource information
output "cloud_run_url" {
  value = google_cloud_run_service.app.status[0].url
}

output "database_connection" {
  value = google_sql_database_instance.main.connection_name
}

output "storage_bucket_url" {
  value = google_storage_bucket.data.url
}

output "ai_model_name" {
  value = google_ai_platform_model.chatbot_model.name
}

# HUMAN ASSISTANCE NEEDED
# The following areas may require additional configuration or validation:
# 1. Ensure that the Google Cloud provider credentials are properly set up.
# 2. Verify that the specified variables (var.project_id, var.region, var.app_image) are defined in a separate variables.tf file.
# 3. Review and adjust the resource configurations (e.g., database tier, storage bucket settings) based on specific project requirements.
# 4. Implement proper IAM roles and permissions for the created resources.
# 5. Consider adding more detailed network and security configurations based on the project's security requirements.
# 6. Evaluate the need for additional Google Cloud services or resources not covered in this configuration.