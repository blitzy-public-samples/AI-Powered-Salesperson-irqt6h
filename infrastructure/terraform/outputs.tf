# Output definitions for important resource information

# Cloud Run service URL
output "cloud_run_service_url" {
  description = "The URL of the deployed Cloud Run service"
  value       = google_cloud_run_service.main.status[0].url
}

# Database connection information
output "database_connection_name" {
  description = "The connection name of the Cloud SQL instance"
  value       = google_sql_database_instance.main.connection_name
}

output "database_ip" {
  description = "The IP address of the Cloud SQL instance"
  value       = google_sql_database_instance.main.ip_address.0.ip_address
}

# Storage bucket names and URLs
output "main_storage_bucket_name" {
  description = "The name of the main storage bucket"
  value       = google_storage_bucket.main.name
}

output "main_storage_bucket_url" {
  description = "The URL of the main storage bucket"
  value       = google_storage_bucket.main.url
}

# AI Platform model endpoints
output "ai_model_endpoint" {
  description = "The endpoint of the deployed AI Platform model"
  value       = google_ai_platform_model.main.default_version[0].deployment_uri
}

# Load balancer IP addresses
output "load_balancer_ip" {
  description = "The IP address of the load balancer"
  value       = google_compute_global_address.default.address
}

# Other relevant resource identifiers or connection details
output "vpc_network_name" {
  description = "The name of the VPC network"
  value       = google_compute_network.main.name
}

output "cloud_function_trigger_url" {
  description = "The trigger URL for the main Cloud Function"
  value       = google_cloudfunctions_function.main.https_trigger_url
}

output "pubsub_topic_id" {
  description = "The ID of the main Pub/Sub topic"
  value       = google_pubsub_topic.main.id
}

output "kms_keyring_name" {
  description = "The name of the main KMS keyring"
  value       = google_kms_key_ring.main.name
}

# HUMAN ASSISTANCE NEEDED
# The following outputs may need to be adjusted based on the specific resources created in your Terraform configuration.
# Please review and modify as necessary to match your infrastructure setup.

output "redis_instance_host" {
  description = "The hostname of the Redis instance"
  value       = google_redis_instance.cache.host
}

output "container_registry_url" {
  description = "The URL of the Container Registry"
  value       = "${google_container_registry.registry.location}-docker.pkg.dev/${var.project_id}/${google_container_registry.registry.repository_id}"
}

output "service_account_email" {
  description = "The email of the main service account"
  value       = google_service_account.main.email
}