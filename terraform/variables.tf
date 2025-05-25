variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The GCP zone"
  type        = string
  default     = "us-central1-a"
}

variable "machine_type" {
  description = "The GCP machine type"
  type        = string
  default     = "e2-micro"
}

variable "bucket_name" {
  description = "The name of the GCS bucket"
  type        = string
  default     = "devsecops-test-bucket"
} 