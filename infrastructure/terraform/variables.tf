# Project-wide variables
variable "project_id" {
  description = "The ID of the Google Cloud project"
  type        = string
}

variable "region" {
  description = "The default region for resources in the project"
  type        = string
  default     = "us-central1"
}

# Service-specific variables
variable "database_tier" {
  description = "The machine type to use for the database instance"
  type        = string
  default     = "db-f1-micro"
}

variable "storage_bucket_names" {
  description = "Names of the storage buckets to create"
  type        = list(string)
  default     = ["app-assets", "app-backups"]
}

# Environment-specific variables
variable "environment" {
  description = "The environment (e.g., 'production', 'development')"
  type        = string
  default     = "development"
}

variable "min_instance_count" {
  description = "Minimum number of instances in the app engine flexible environment"
  type        = number
  default     = 1
}

variable "max_instance_count" {
  description = "Maximum number of instances in the app engine flexible environment"
  type        = number
  default     = 5
}

# Networking variables
variable "network_name" {
  description = "The name of the VPC network"
  type        = string
  default     = "main-network"
}

variable "subnet_cidr" {
  description = "The CIDR range for the subnet"
  type        = string
  default     = "10.0.0.0/24"
}

variable "allowed_ip_ranges" {
  description = "List of IP ranges allowed to access the resources"
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

# HUMAN ASSISTANCE NEEDED
# The following variables might need adjustment based on specific project requirements:
# - Consider adding more granular controls for different services
# - Evaluate if default values are appropriate for your use case
# - Add any additional variables that might be needed for your specific infrastructure setup